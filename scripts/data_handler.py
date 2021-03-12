import pandas as pd

def get_total_data(event_name):
    df = pd.read_csv('../data/Telematik_Events.csv', sep=';')
    fata_exception =  df['type']==event_name
    filtered = df[fata_exception]
    # unique_events = df['type'].unique()
    data = filtered[['lat','lon','type']].dropna()

    return data.values

# t = get_total_data()
# print(t)


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