class Helper():

    def strip_unicode(self, json):
        new_dict = {}
        for key in json:
            k = str(key)
            if isinstance(json[key], unicode):
                v = str(json[key])
            else:
                v = json[key]
            new_dict[k] = v
            # print type(k), type(v)
        return new_dict

    def convert_elections(self, elections):
        return_data = {}
        for i in range(len(elections)):
            temp_data = {}
            temp_data['name'] = elections[i].name
            temp_data['id'] = elections[i].id
            temp_data['options'] = elections[i].options
            return_data[i] = temp_data
        return return_data

    def return_election_data(self, election):

        election_hashes = []
        for chain in election.chain:
            chain_hashes = []
            for vote in chain.leaves:
                chain_hashes.append(vote.value)
            election_hashes.append(chain_hashes)

        election_active = []
        if len(election.active_tree.leaves) > 0:
            for vote in election.active_tree.leaves:
                election_active.append(vote.value)

        return_dict = {'name': election.name, 'id': election.id, 'options':election.options, 'chain':election_hashes, 'active':election_active}

        return return_dict
