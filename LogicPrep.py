
from astroboi_bio_tools.ToolLogicPrep import ToolLogicPreps
class LogicPreps(ToolLogicPreps):
    def make_list_to_dict(self, input_list, key_idx):
        result_dict = {}
        for tmp_arr in input_list:
            tmp_key = tmp_arr[key_idx]
            if tmp_key in result_dict:
                result_dict[tmp_key].append(tmp_arr)
            else:
                result_dict.update({tmp_key: [tmp_arr]})

        return result_dict

    def make_dict_to_list(self, result_dict):
        result_list = []
        for val_list in result_dict.values():
            for val_arr in val_list:
                result_list.append(val_arr)

        return result_list
