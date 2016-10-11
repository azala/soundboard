import random
import util
import live_config
from audio_socket import AudioSocket

votes_per_second = {}
cooldown_time = 0

def voted(n):
    t = util.ctime()
    if t not in votes_per_second:
        votes_per_second[t] = {}
    vps = votes_per_second[t]
    vps[n] = vps.get(n, 0) + 1

def count_votes():
    d = {}
    for t in votes_per_second:
        votes = votes_per_second[t]
        for index in votes:
            d[index] = d.get(index, 0) + votes[index]
    return d

def prune(n):
    t = util.ctime()
    l = [x for x in votes_per_second.keys()]
    for k in l:
        if k < t - n:
            del votes_per_second[k]

def get_winner():
    d = count_votes()
    m = live_config.d['min_votes']
    w = []
    for k in d:
        v = d[k]
        if v > m:
            w = [k]
            m = v
        elif v == m:
            w.append(k)
    if len(w) == 0:
        return None
    return random.choice(w)

def periodic_prune():
    if util.ctime() < cooldown_time:
        return
    prune(live_config.d['seconds_to_store'])
    w = get_winner()
    if w is not None:
        play(w)

def destroy_votes_for(n):
    for t in votes_per_second:
        votes = votes_per_second[t]
        if n in votes:
            del votes[n]

def play(n):
    global cooldown_time
    cooldown_time = util.ctime() + live_config.d['cooldown']
    destroy_votes_for(n)
    AudioSocket.play(n)
