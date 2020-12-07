from controllermodel import GenericController

import asyncio
import websockets
import jsonpickle

class WebsocketController(GenericController):
    def __init__(self, host, port):

        super().__init__() #! This is important! Initialize the base class or you will get an error upon startup!

        #Websocket asyncio setup. See https://websockets.readthedocs.io/en/stable/ for more information.
        self._loop = asyncio.get_event_loop()
        self.websocket = websockets.serve(self.handler, host, port)
        print("Server running at ws://{0}:{1}".format(host, port))
        self._loop.run_until_complete(self.websocket) 

    async def handler(self, ws, path, *args, **kw):
        """
        This is the function that gets called when a new websocket connection arrives.
        """
        await self.consumer_handler(ws, path, *args, **kw) # We only have a consumer handler here. For both a producer and consumer, see https://websockets.readthedocs.io/en/stable/intro.html#both

    async def consumer_handler(self, ws, path, *args, **kwargs):
        """
        The consumer_handler funciton will wait for data to be sent to us from the client, and try to find a corresponding action
        to execute, which will return data to the client.

        Send commands to this endpoint as `{ 'action': <<an action>>, 'data': { <<your keyword arguments>> } }`
        """
        async for message in ws:
            m = {} #Initialize our message dictionary
            try:
                m = jsonpickle.loads(message) # Load the (presumably) JSON message they sent
            except Exception:
                print("Error decoding message from " + str(ws.remote_address) + ". Message: " + str(message))
                send = jsonpickle.dumps({"error": "Couldn't parse JSON data!"}, unpicklable=False, make_refs=False)
                await ws.send(send)
            else:
                if(m != None):
                    action = m.get('action', None)
                    data = m.get('data', dict())

                    if action != None:
                        try:
                            r = self.execute_action(str(action), **data) # The main application will register functions to various commands. See if we can find one registered for the command sent.
                                                                         # Note, if no function is found, we will just JSON pickle `None` which will just send a `null` back to the client.
                                                                         # You may want to change this behavior by sending back an error message if the command recieved doesn't exist
                        except Exception as e:
                            r = {"error": str(e)}

                        r_json = jsonpickle.dumps(r, unpicklable=False, make_refs=False)
                        await ws.send(r_json) 
                    else:
                        send = jsonpickle.dumps({"error": "No command to process!"}, unpicklable=False, make_refs=False)
                        await ws.send(send)
                else:
                    send = jsonpickle.dumps({"error": "No data to parse!"}, unpicklable=False, make_refs=False)
                    await ws.send(send)