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

temp3_df = pd.read_json("RyderStreamHist.json")
print(temp3_df)