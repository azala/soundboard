from tornado import websocket
import json

class AudioSocket(websocket.WebSocketHandler):
    open_sockets = []
    
    def check_origin(self, origin):
        return True
    
    def open(self):
        AudioSocket.open_sockets.append(self)

    def on_close(self):
        AudioSocket.open_sockets.remove(self)

    def on_message(self, message):
        d = json.loads(message)
        getattr(self, 'cmd_'+d['m'])(d)

    @classmethod
    def play(cls, n):
        print('Playing sound: {}'.format(n))
        for sock in cls.open_sockets:
            sock.write_message(json.dumps({
                'm': 'play',
                'number' : n
            }))
