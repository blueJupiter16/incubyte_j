import pandas as pd
from datetime import datetime
import sys

#Read files/tables - create initial databases
record_details = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/record_details.csv')
batch_df = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/batch_data/batch1_20210122',sep='|')
reference_df = pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/inputs/reference_table.csv')


print("Read competed... Writing to stage layer")

#Write file to stg layer
batch_df.to_csv('/Users/junaidtinwala/Work/Projects/incubyte/outputs/stg_csv.csv')

print("Stage load completed... ")
#read from stage layer
stg_df=pd.read_csv('/Users/junaidtinwala/Work/Projects/incubyte/outputs/stg_csv.csv')
man_cols=record_details[record_details.Mandatory=='Y']['Column_Name'].values.tolist()

#check if load needs to be rejected
print("Check if Null values in the mandatory columns of Batch")
if stg_df[man_cols].isnull().values.any():
    print("Null values found in the batch.. Rejecting load")
    sys.exit()

print("No Null values found.. Proceeding with final table load")

#iterate the reference table to write to individual tables
all_countys = []
for index, row in reference_df.iterrows():
    countys=row['county_name'].split('|') #split the countys to the table
    all_countys = all_countys+countys #collect all countys
    table_name=row['table_name']
    output_file_name=table_name+"_"+datetime.now().strftime("%Y%m%d%H%M%S")
    write_df=stg_df[stg_df.Country.isin(countys)].drop(columns=['H'])
    print("Writing ",len(write_df.index)," records to ",table_name)
    write_df.to_csv('/Users/junaidtinwala/Work/Projects/incubyte/outputs/'+output_file_name,index=False)

#Remaining records go to default table
print("Writing remaining countys to default table....")
output_file_name="table_default_"+datetime.now().strftime("%Y%m%d%H%M%S")
write_df=stg_df[~stg_df.Country.isin(all_countys)].drop(columns=['H'])
write_df.to_csv('/Users/junaidtinwala/Work/Projects/incubyte/outputs/'+output_file_name,index=False)


