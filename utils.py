import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

temp_df = pd.read_json("RyderStreamHist.json")
temp_df = temp_df.drop(['url', 'image', 'mbid', 'streamable'], axis=1)

#ARTIST 
temp_df[['temp1', 'temp2', 'artist']] = temp_df["artist"].apply(lambda x: pd.Series(str(x).split(":")))
temp_df = temp_df.drop(['temp1','temp2'], axis=1)
temp_df['artist'] = temp_df['artist'].str.replace('}','')
temp_df['artist'] = temp_df['artist'].str.replace("'",'')

#ALBUM
temp_df[['temp1', 'temp2', 'album', 'temp4']] = temp_df["album"].apply(lambda x: pd.Series(str(x).split(":")))
temp_df = temp_df.drop(['temp1', 'temp2', 'temp4'], axis=1)
temp_df['album'] = temp_df['album'].str.replace('}','')
temp_df['album'] = temp_df['album'].str.replace("'",'')

#DATE
temp_df[['temp1', 'date', 'time']] = temp_df["date"].apply(lambda x: pd.Series(str(x).split(",")))
temp_df = temp_df.drop(['temp1'], axis=1)
temp_df[['temp1', 'temp2', 'day', 'month', 'year']] = temp_df["date"].apply(lambda x: pd.Series(str(x).split(" ")))
temp_df = temp_df.drop(['temp1', 'temp2', 'date'], axis=1)
temp_df['time'] = temp_df['time'].str.replace('}','')
temp_df['time'] = temp_df['time'].str.replace("'",'')
temp_df['day'] = temp_df['day'].str.replace("'",'')

print(temp_df)

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