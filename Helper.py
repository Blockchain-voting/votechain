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
