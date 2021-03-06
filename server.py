from flask import *
from json import *
from Handler import *
from Helper import *
from Vote import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# various server helper functions
helper = Helper()

# list of all elections held in the server
# much scalability!!! such safe!!!!!
Elections = []

@app.route('/hello', methods=['GET'])
def hello_world():
    print 'pinged by React'
    return jsonify(hello='world')

@app.route('/elections', methods=['GET', 'POST'])
def elections():
    if request.method == 'GET':
        # print 'returning %s Elections' % (len(Elections))
        return jsonify(helper.convert_elections(Elections))

    elif request.method == 'POST':
        if request.get_json:
            election_data = helper.strip_unicode(request.get_json())
        else:
            return jsonify({'error':"bad data",'response':400})
        el_handler = Handler(election_data['name'], (len(Elections) + 1), election_data['options'])
        Elections.append(el_handler)
        # need to get data out of this and create json to send back
        # print 'Election created with name %s and id of %s' % (el_handler.name, el_handler.id)
        return jsonify(helper.convert_elections(Elections))

@app.route('/elections/<int:election_id>', methods=['GET'])
def election_data_id(election_id):
    print "Election %s" % election_id
    election_temp = Elections[election_id - 1]
    election_data = helper.return_election_data(election_temp)
    return jsonify(election_data)

@app.route('/vote', methods=['POST'])
def vote():
    # create temporary dictionary item for vote
    vote_dict = helper.strip_unicode(request.get_json())
    # create Vote item for vote dictionary purely b/c I find it easier to work with objects that I can manipulate how I like
    # might remove this if it isn't repeated too much
    vote = Vote(vote_dict.get('election'), vote_dict.get('options'), vote_dict.get('signature'))
    # print "Vote created for election with id of %s with the choice of %s and public key of %s" % (vote.id, vote.choice, vote.signature)
    election = Elections[vote.id]
    # print 'vote request:', vote, election.name
    vote_hash = election.vote(vote)
    return jsonify(vote_hash)

@app.route('/count/<int:count_id>', methods=['GET'])
def count(count_id):
    print "count_id - %s" % count_id
    zerod_id = count_id - 1
    verify = Elections[zerod_id].count()
    return jsonify(verify)

if __name__ == '__main__':
    # app.run(host='0.0.0.0',debug=True)
    app.run(host='0.0.0.0')
