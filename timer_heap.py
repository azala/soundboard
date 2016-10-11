import threading, heapq, time

heap = [] #(time, id) pairs
event_map = {} #id -> dict
_last_event_id = 0
_time = 0
_last_actual_time = None

def tick():
    global _time, _last_actual_time
    tt = time.time()
    if _last_actual_time:
        _time += tt - _last_actual_time
        check()
    _last_actual_time = tt

def check():
    t = _time
    while len(heap) > 0 and t >= heap[0][0]:
        eid = heapq.heappop(heap)[1]
        if eid in event_map:
            dostuff(eid)

def next_event_id():
    global _last_event_id
    _last_event_id += 1
    return _last_event_id

def add(event, dt):
    eid = next_event_id()
    event['event_id'] = eid
    event_map[eid] = event
    heapq.heappush(heap, (_time + dt, eid))
    return eid

def remove(eid):
    if eid in event_map:
        del event_map[eid]

def dostuff(eid):
    event = event_map[eid]
    remove(eid)
    event['callback'](event)
