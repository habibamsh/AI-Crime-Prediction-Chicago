import pandas as pd
import datetime

def get_week_of_year_from_string(timestamp_str):
    timestamp_format = "%m/%d/%Y %I:%M:%S %p"
    try:
        datetime_obj = datetime.datetime.strptime(timestamp_str, timestamp_format)
        week_number = datetime_obj.strftime("%U")
        return int(week_number)
    except ValueError:
        return None

df = pd.read_csv('/Users/manav/Desktop/cmpsc-497-fall-2023-final-project-ai-policing/implementation/crime_data_raw_2022C.csv')


x_to_name = {}
name_to_x = {}
# Iterate over DataFrame rows to create the mappings
for index, row in df.iterrows():
    x_to_name[row['IUCR']] = row['Primary Type']
    name_to_x[row['Primary Type']] = row['IUCR']
df['week_no'] = df['Date'].apply(get_week_of_year_from_string)
df = df.drop(columns=['Zip Codes', 'Date', 'Block', 'Primary Type', 'Beat','Location'])
df.to_csv('cleaned_dataset.csv', index=False)
