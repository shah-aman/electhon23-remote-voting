from . import db

_started = False

def init():
    init_db()
    init_flag()

def init_db():
    db.init()

def init_flag():
    global _started

    if _started: 
        print("Already started")
        return
    
    _started = True
    return

def flip_flag():
    global _started

    if not _started: 
        print("Already ended")
        return
    
    _started = False
    return