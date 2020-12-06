from controllermodel import GenericController

import asyncio
import websockets

class WebsocketController(GenericController):
    def __init__(self, host, port):
        self._loop = asyncio.get_event_loop()
        self.websocket = websockets.Serve()