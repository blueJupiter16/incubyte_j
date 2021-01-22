import pandas as pd

#Read files/tables - create initial databases
record_details = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/record_details.csv')
batch_df = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/batch_data/batch1_20210122',sep='|')
reference_df = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/reference_table.csv')

print(reference_df)
