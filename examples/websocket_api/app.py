from lib.websocket_endpoint import WebsocketController
from lib.data_model import DataModel

import asyncio

class Application:
    def __init__(self):
        self._loop = asyncio.get_event_loop()
        self.data_model = DataModel()
        self.websocket_api = WebsocketController("0.0.0.0", 7033)
        
        self.websocket_api.connect_instance(self.data_model)
        
        self._loop.run_forever()

if __name__ == '__main__':
    app = Application()