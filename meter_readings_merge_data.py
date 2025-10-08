import os
import glob
import pandas as pd
os.chdir("extract")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
all_reading_df = pd.DataFrame(columns=['meter/customer/name','meter/serial','kilowatt_hours','heartbeat_end'])

for f in all_filenames:
    df = pd.read_csv(f)
    df['heartbeat_end'] = pd.to_datetime(df['heartbeat_end']).dt.date
    new_df = df[['meter/customer/name','meter/serial','kilowatt_hours','heartbeat_end']]
    total_df = new_df.groupby(['meter/customer/name','meter/serial','heartbeat_end']).agg({
    'kilowatt_hours': 'sum',
    })
    
    print(total_df)
    if not total_df.empty:
        total_df = total_df.reset_index()
        total_df['heartbeat_end'] = pd.to_datetime(total_df['heartbeat_end']).dt.date
        all_reading_df = pd.concat([all_reading_df, total_df], ignore_index=True)
 

all_reading_df.rename(columns={'meter/customer/name': 'Customer Name', 'meter/serial': 'Customer Meter Serial', 'kilowatt_hours': 'Total', 'heartbeat_end': 'Month_Year'}, inplace=True)
all_reading_df['sno'] = all_reading_df.reset_index().index
all_reading_df.to_csv("all_reading_df.csv", index=False, encoding='utf-8-sig')
#combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
#new_df = combined_csv[['meter/customer/name','meter/serial','kilowatt_hours','heartbeat_end']]
#new_df['heartbeat_end'] = pd.to_datetime(new_df['heartbeat_end']).dt.date
#total_df = new_df.groupby(['meter/customer/name','meter/serial','heartbeat_end']).agg({
#    'kilowatt_hours': 'sum',
#   
#})

#total_df = total_df['meter/customer/name','meter/serial','heartbeat_end','kilowatt_hours']
#print(total_df)
#total_df.to_csv("reading_new.csv",  index=False, encoding='utf-8-sig')
