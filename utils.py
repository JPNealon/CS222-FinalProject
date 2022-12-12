import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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