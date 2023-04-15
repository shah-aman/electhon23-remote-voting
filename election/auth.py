# hard coding keys

START_KEY = "start"
END_KEY = "end"

def authorized_start(key):
    if not key: return
    # do some thing on keys
    if key == START_KEY:
        return True
    return False    


def authorized_end(key):
    if not key: return
    # do some thing on keys
    if key == END_KEY:
        return True
    return False    