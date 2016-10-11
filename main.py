#!default/bin/python

from tornado import ioloop, web, httpserver
from watchdog import observers, events
import json
from audio_socket import AudioSocket
import vote_tracker
import live_config
import ioloop_helper

class WidgetHandler(web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        print(data)
        vote_tracker.voted(data['vote'])
        
class WatchdogHandler(events.FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == 'config/live.js':
            live_config.update()
        
live_config.update()

application = web.Application([
    (r"/widget", WidgetHandler),
    (r"/audio", AudioSocket)
])

http_server = httpserver.HTTPServer(application)
http_server.listen(7777)
main_loop = ioloop.IOLoop.instance()
ioloop.PeriodicCallback(ioloop_helper.tick, 1000).start()

observer = observers.Observer()
handler = WatchdogHandler()
observer.schedule(handler, 'config', recursive=True)
observer.start()

main_loop.start()
