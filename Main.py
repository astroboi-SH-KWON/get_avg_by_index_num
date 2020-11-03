import time
import os
import platform

import Util
import Logic
import LogicPrep
############### start to set env ################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    pass
else:
    # DEV
    WORK_DIR = "D:/000_WORK/Ramu_JangHyeWon/20201103/WORK_DIR/"

hFAH_PE_Cutoff = "hFAH_PE_Cutoff.txt"

############### end setting env #################

def test():
    util = Util.Utils()
    logic_prep = LogicPrep.LogicPreps()
    logic = Logic.Logics()

    hFAH_PE_Cutoff_list = util.read_tsv_ignore_N_line(WORK_DIR + '/input/' + hFAH_PE_Cutoff)

    result_dict = logic_prep.make_list_to_dict(hFAH_PE_Cutoff_list, 4)

    logic.append_avg_to_val_list(result_dict)

    result_list = logic_prep.make_dict_to_list(result_dict)

    sorted_result_list = logic_prep.sort_list_by_ele(result_list, 4, False)

    header = "INDEX	Index_#				TTTT_Barcode	Spacer	RT-PBS	Original sequence	Edited sequence	Background_Original	Background_Edited	Background_Total	background %	Rep1_Original	Rep1_Edited	Rep1 Edited (norm)	Rep1_Total	Rep2 Total (norm)	PE effi%	Rep1 %	Rep2_Original	Rep2_Edited	Rep2 Edited (norm)	Rep2_Total	Rep2 Total (norm)	PE effici%	Rep2 %	Rep1+Rep2 Mean (mean value)".split('\t')
    header.append('Avrage Rep1+Rep2')
    util.make_excel(WORK_DIR + '/output/hFAH_PE_Cutoff', header, sorted_result_list)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    test()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))