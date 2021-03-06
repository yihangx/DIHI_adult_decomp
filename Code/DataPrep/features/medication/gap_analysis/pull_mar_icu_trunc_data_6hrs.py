# Adult Decompensation Prediction
# 
# Copyright 2019 Ziyuan Shen, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC.
# 
# All Rights Reserved.

import os
import gc
import pandas as pd

def main():
    icu_adm_enc_6hrs_df = pd.read_csv('../../../../../Data/Processed/cohort/icu_adm_enc_6hrs.csv')
    icu_adm_enc_6hrs_df['6hrs_before_transfer'] = pd.to_datetime(icu_adm_enc_6hrs_df['6hrs_before_transfer'])
    for file_name in os.listdir('../../../../../Data/Raw/medications'):
        file = os.path.join('../../../../../Data/Raw/medications', file_name)
        df = pd.read_csv(file, encoding='cp1252')
        df = df.merge(icu_adm_enc_6hrs_df, left_on='pat_enc_csn_id', right_on='pat_enc_csn_id', how='inner')
        df['taken_time'] = pd.to_datetime(df['taken_time'], errors='coerce', utc=True)
        df = df.loc[df['taken_time']<df['6hrs_before_transfer']]
        df = df[['pat_enc_csn_id', 'medication_name']]
        df.to_csv(os.path.join('../../../../../Data/Processed/features/medications/gap_analysis/mar_icu_trunc_data_6hrs', file_name), index=False)
        del df
        gc.collect()


if __name__ == '__main__':
    main()