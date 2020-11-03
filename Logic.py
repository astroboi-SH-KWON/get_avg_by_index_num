
from astroboi_bio_tools.ToolLogic import ToolLogics
class Logics(ToolLogics):
    def append_avg_to_val_list(self, result_dict):
        for val_list in result_dict.values():
            len_val = len(val_list)
            if len_val == 1:
                continue
            else:
                sum = 0.0
                for val_arr in val_list:
                    sum += float(val_arr[-1])
                val_list[0].append(sum / len_val)
