import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read in the raw, unprocessed data into a pandas dataframe
jack_df = pd.read_json("JackStreamHistory.json")
jack_df.fillna(np.nan, inplace=True)
jack_df[['Date','Time']] = jack_df.endTime.str.split(expand=True)
jack_df = jack_df.drop('endTime', axis=1)
jack_df['msPlayed'] = jack_df['msPlayed'] / 1000
print(jack_df)