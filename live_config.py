import json
import jsmin

d = {}

def update():
    global d
    with open('config/live.js') as f:
        d = json.loads(jsmin.jsmin(f.read()))
