# intialize evm
######### Assuming done ##############
import election.app as app
import sys

inp = sys.argv[1]
cmd = False

if "config" == inp:
    print("enter start/end: ")
    key = input()
    if key == "start":
        print("enter key to start")
        is_success = app.init(input())
        if is_success: cmd = True
    elif key == "end":
        print("enter keu to end")
        app.end(input())

elif "result" == inp:
    app.calculate_result()
    
while (cmd):    
    
    if cmd == "vote":
        print("election_id candidate_id to vote: ")
        election_id, candidate_id = input().split(" ")
        print(election_id, candidate_id)
        app.cast_vote(election_id, candidate_id)

    elif cmd == "break":
        break

    elif cmd == "end":
        print("enter key to end: ")
        key = input()
        app.end(key)
        break
    print("vote, end, break")
    cmd = input()


# start
# authorize
# set sart flag 
# intialize DB


# cast vote
# vote counter

# end election
# result caclulator

# send result 

# reset the evm