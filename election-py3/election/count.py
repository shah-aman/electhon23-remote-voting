from . import db
def add(election_id, candidate_id):
    db.insert_data(election_id, candidate_id)