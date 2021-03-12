import pandas as pd

def get_total_data():
    df = pd.read_csv('./Telematik_Events.csv', sep=';')
    # print(df)
    data = df[['lat','lon','dur']].dropna()

    return data.values

# t = get_total_data()
# print(t)

