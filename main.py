import pandas as pd
record_details = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/record_details.csv')
batch_df = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/batch_data/batch1_20210122',sep='|')

print(batch_df)
