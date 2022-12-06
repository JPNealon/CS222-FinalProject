import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read in the raw, unprocessed data into a pandas dataframe
temp1_df = pd.read_json("JackStreamHist1.json")
temp2_df = pd.read_json("JackStreamHist2.json")
jack_df = pd.concat([temp1_df, temp2_df], ignore_index=True)

jack_df.fillna(np.nan, inplace=True)
jack_df[['Date','Time']] = jack_df.endTime.str.split(expand=True)
jack_df = jack_df.drop('endTime', axis=1)
jack_df['msPlayed'] = jack_df['msPlayed'] / 1000
#print(jack_df)
jack_df[['Year','Month','Day']] = jack_df.Date.str.split(pat='-', expand=True)
jack_df = jack_df.drop('Date', axis=1)
#print(jack_df)

temp3_df = pd.read_json("RyderStreamHist.json")
print(temp3_df)
temp3_df[["temp1", "temp2"]] = temp3_df.artist.str.split(expand=True)
print(temp3_df)

'''
To-do cleaning:
1. Add the artist's genre (using Dr. Sprints spotify artist-genre program/function)
1. Add a season column (use the date to correlate it's season)
1. Date the song/podcast was released ()
'''