import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ryder_df = pd.read_json("RyderStreamHist.json")
ryder_df = ryder_df.drop(['url', 'image', 'mbid', 'streamable'], axis=1)

#ARTIST 
ryder_df[['temp1', 'temp2', 'artist']] = ryder_df["artist"].apply(lambda x: pd.Series(str(x).split(":")))
ryder_df = ryder_df.drop(['temp1','temp2'], axis=1)
ryder_df['artist'] = ryder_df['artist'].str.replace('}','')
ryder_df['artist'] = ryder_df['artist'].str.replace("'",'')

#ALBUM
ryder_df[['temp1', 'temp2', 'album', 'temp4']] = ryder_df["album"].apply(lambda x: pd.Series(str(x).split(":")))
ryder_df = ryder_df.drop(['temp1', 'temp2', 'temp4'], axis=1)
ryder_df['album'] = ryder_df['album'].str.replace('}','')
ryder_df['album'] = ryder_df['album'].str.replace("'",'')
ryder_df['album'] = ryder_df['album'].str.replace('"','')

#DATE
ryder_df[['temp1', 'date', 'time']] = ryder_df["date"].apply(lambda x: pd.Series(str(x).split(",")))
ryder_df = ryder_df.drop(['temp1'], axis=1)
ryder_df[['temp1', 'temp2', 'day', 'month', 'year']] = ryder_df["date"].apply(lambda x: pd.Series(str(x).split(" ")))
ryder_df = ryder_df.drop(['temp1', 'temp2', 'date'], axis=1)
ryder_df['time'] = ryder_df['time'].str.replace('}','')
ryder_df['time'] = ryder_df['time'].str.replace("'",'')
ryder_df['day'] = ryder_df['day'].str.replace("'",'')

decoder = {'Jan' : 1 , 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec':12}
ser = ryder_df["month"]
for key in decoder:
    ser.replace(key, decoder[key], inplace=True)

print(ryder_df)

'''
"artist":{"mbid":"c98d40fd-f6cf-4b26-883e-eaa515ee2851","#text":"The Cranberries"},
"streamable":"0",
"image":[{"size":"small","#text":"https:\/\/lastfm.freetls.fastly.net\/i\/u\/34s\/87138bbda83bd0ae8b4da2b6cab9b66a.jpg"},
    {"size":"medium","#text":"https:\/\/lastfm.freetls.fastly.net\/i\/u\/64s\/87138bbda83bd0ae8b4da2b6cab9b66a.jpg"},
    {"size":"large","#text":"https:\/\/lastfm.freetls.fastly.net\/i\/u\/174s\/87138bbda83bd0ae8b4da2b6cab9b66a.jpg"},
    {"size":"extralarge","#text":"https:\/\/lastfm.freetls.fastly.net\/i\/u\/300x300\/87138bbda83bd0ae8b4da2b6cab9b66a.jpg"}],
"mbid":"null",
"album":{"mbid":"000b188f-549f-4c11-a5fb-024fbfdb7a13","#text":"Everybody Else Is Doing It, So Why Can't We?"},
"name":"Dreams",
"url":"https:\/\/www.last.fm\/music\/The+Cranberries\/_\/Dreams",
"date":{"uts":"1670278690","#text":"05 Dec 2022, 22:18"}
'''