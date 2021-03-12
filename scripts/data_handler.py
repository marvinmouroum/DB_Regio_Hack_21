import pandas as pd
df = pd.read_csv ('../Telematik_Events.csv',sep=';')
# print(df)


event_type = df['type']
lat = df['lat']
lon = df['lon']
dur = df['dur']

print(event_type)
