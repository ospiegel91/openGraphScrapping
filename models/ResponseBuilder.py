import json

class ResponseBuilder:

    def __init__(self, og_obj):
        self.og_obj = og_obj
        self.og_meta_list = og_obj.find_all_og_props();

    def find_2nd(self, string, substring):
        return string.find(substring, string.find(substring) + 1)

    def check_if_url(self, string):
        if string[:4] == 'http':
            return 'url'
        else:
            return 'main'

    def get_response_object_in_json(self):
        res_dict = {}
        handled_res_key_names = []
        for og_meta in self.og_meta_list:
            if og_meta["property"].count(":") > 1:
                res_key_name = og_meta["property"][3:self.find_2nd(og_meta["property"],":")]
                if res_key_name in handled_res_key_names:
                    continue
                res_dict[res_key_name] = []
                all_og_prop_extensions = self.og_obj.find_all_og_props_by_extension(res_key_name)
                child_dict = {}
                for og_prop_extension in all_og_prop_extensions:
                    name_2nd_og = og_prop_extension["property"][self.find_2nd(og_prop_extension["property"],":")+1:]
                    if name_2nd_og.count(":") > 0:
                        key_name = self.check_if_url(og_prop_extension["content"])
                        child_dict[key_name] = og_prop_extension["content"]
                    else:
                        child_dict[name_2nd_og] = og_prop_extension["content"]
                res_dict[res_key_name].append(child_dict)
                handled_res_key_names.append(res_key_name)

            else:
                res_key_name = og_meta["property"][3:]
                res_dict[res_key_name] = og_meta["content"]

        return json.dumps(res_dict)