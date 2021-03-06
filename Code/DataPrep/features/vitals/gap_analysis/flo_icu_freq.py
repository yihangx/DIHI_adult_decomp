# Adult Decompensation Prediction
# 
# Copyright 2019 Ziyuan Shen, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC.
# 
# All Rights Reserved.

import sys
sys.path.insert(0, '../../../../')

from utils.df_utils import sum_count

def main():
    input_file = "../../../../../Data/Processed/features/vitals/gap_analysis/flo_icu_freq_temp.csv"
    output_file = "../../../../../Data/Processed/features/vitals/gap_analysis/flo_icu_freq.csv"
    sum_count(input_file, output_file, 'flo_meas_name')
    return None

if __name__ == '__main__':
    main()