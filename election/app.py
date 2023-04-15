from . import start_stop, count, auth, result, send_result

def init(key):
    if not key:
        print("No key provided")
        return
    is_authorized = auth.authorized_start(key)
    
    # auth
    if not is_authorized: 
        print("Person Not authrized to start")
        return
    
    # start
    start_stop.init()
    return True

def end(key):
    if not key:
        print("No key provided")
        return
    
    is_authorized = auth.authorized_end(key)

     # auth
    if not is_authorized: 
        print("Person Not authrized to end")
        return
    
    start_stop.flip_flag()
    print('election ended')

def cast_vote(election_id, candidate_id):
    count.add(election_id, candidate_id)


def calculate_result(send=True):
    
    data = result.caculate()

    if send:
        send_result(data)
    

def send_result(data):
    # TODO: display qr code
    print(data)