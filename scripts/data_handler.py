import pandas as pd

def get_total_data():
    df = pd.read_csv('../data/Telematik_Events.csv', sep=';')
    # print(df)

    event_type = df['type']
    lat = df['lat']
    lon = df['lon']
    dur = df['dur']

    return df[['lat','lon','dur']].values

#get_total_data()