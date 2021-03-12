import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy import stats 

def get_total_data(event_name):
    df = pd.read_csv('../data/Telematik_Events.csv', sep=';')
    fata_exception =  df['type']==event_name
    filtered = df[fata_exception]
    # unique_events = df['type'].unique()
    
    data = filtered[['lat','lon','dur']].dropna()
    data['z_score']=stats.zscore(data['lat'])
    clean = data.loc[data['z_score'].abs()<=3]

    # data[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

    arr = clean.values

    if arr.size == 0:
        return []

    mean = np.mean(arr,0)
    std = np.std(arr,0)

    arr_m = arr-mean
    arr_m_s = arr_m/std
    return arr_m_s, mean, std

#t = get_total_data('DECEL')
#print(t)

def plot_3D(X,pred_y, ax=None):
    if ax is None:
        ax = plt.axes(projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=pred_y, cmap='viridis', linewidth=0.5);

    plt.show()

    return ax


#  Unique events 
# ['ECO LEERLAUFZEITÜBERSCHREITUNG' 'TÜRE 2 GEÖFFNET' 'LEERLAUFZEIT 5M'
#  'LEERLAUFZEIT 5M, KÜHLMITTELTEMP. 40C' 'TÜRE 1 GEÖFFNET' 'PDI'
#  'LEERLAUFZEITÜBERSCHREITUNG TEST' 'ACCEL' 'DECEL' 'ECO DREHZAHL'
#  'DRIVER TRAINING: FUEL, SPEED AND TRIP RULE' 'ENTSPANNTES FAHREN'
#  'ECO GESCHWINDIGKEIT' 'FAHRDYNAMIK BUS' 'DECEL_018G_30KMH_45KMH'
#  'HOHE VERZÖGERUNG' 'DECEL_016G_45KMH_60KMH' 'ECO BREMSEN'
#  'DECEL_012G_75KMH' 'DECEL_020G_15KMH_30KMH' 'ECO BESCHLEUNIGUNG'
#  'BESCHLEUNIGUNG 0.18' 'ECO KOMFORT' 'ENGINE FAULT EXCEPTION'
#  'ADBLUE_FILLUP' 'ÖKO-STEUERPFLICHTIG' 'UNERLAUBTES ENTFERNEN DES GERÄTS'
#  'FUEL_FILLUP' 'TÜRE 3 GEÖFFNET' 'DECEL_014G_60KMH_75KMH'
#  'TÜRE 4 GEÖFFNET' 'WARNLICHT ROT' 'BATTERIESPANNUNG 24V' 'WARNLICHT GELB'
#  'PRÜFREGEL FEHLERKENNUNG SOC' 'ALTES EVENT DREHZAHL' 'INNERHALB STANDORT'
#  'INNERHALB NIEDERLASSUNG' 'INNERHALB DEUTSCHLAND' 'IN BETRIEB'
#  'INNERHALB DB WERKSTATT' 'BREMSBELÄGE 1 ACHSE LINKS'
#  'BREMSBELÄGE 3 ACHSE RECHTS' 'BREMSBELÄGE 1 ACHSE RECHTS'
#  'BREMSBELÄGE 3 ACHSE LINKS' 'BREMSBELÄGE 2 ACHSE LINKS'
#  'BREMSBELÄGE 2 ACHSE RECHTS' 'FAHRDYNAMIK KLEINBUS' 'ABS AKTIV'
#  'INNERHALB EXTERNER WERKSTATT' 'MÖGLICHE KOLLISION'
#  'HOHE MOTORTEMPERATUR']
