import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
"""
Programmers: Jack Nealon and Ryder Gallagher
Class: CPSC 222, Fall 2022, Dr. Gina Sprint
Final Project 
12/13/2022
Description: This file contains the functions necessary to read in data, clean the data,
             calculate statistics from the data, and display the data in a graph. I said 
             data a bunch but I'm leaving it because it makes sense. :D
""" 

def read_files():
    ryder_df = pd.read_json("RyderStreamHist.json")

    temp1_df = pd.read_json("JackStreamHist1.json")
    temp2_df = pd.read_json("JackStreamHist2.json")
    jack_df = pd.concat([temp1_df, temp2_df], ignore_index=True)
    return jack_df, ryder_df

def clean_jack_info(jack_df):
    jack_df.fillna(np.nan, inplace=True)
    jack_df[['Date','Time']] = jack_df.endTime.str.split(expand=True)
    jack_df = jack_df.drop('endTime', axis=1)
    jack_df['msPlayed'] = jack_df['msPlayed'] / 1000
    jack_df[['Year','Month','Day']] = jack_df.Date.str.split(pat='-', expand=True)
    jack_df = jack_df.drop('Date', axis=1)
    return jack_df

def clean_ryder_info(ryder_df):
    ryder_df.fillna(np.nan, inplace=True)
    ryder_df = ryder_df.drop(['url', 'image', 'mbid', 'streamable'], axis=1)

    #ARTIST 
    ryder_df[['temp1', 'temp2', 'artist']] = ryder_df["artist"].apply(lambda x: pd.Series(str(x).split(":")))
    ryder_df = ryder_df.drop(['temp1','temp2'], axis=1)
    ryder_df['artist'] = ryder_df['artist'].str.replace('}','',regex=True)
    ryder_df['artist'] = ryder_df['artist'].str.replace("'",'')

    #ALBUM
    ryder_df[['temp1', 'temp2', 'album', 'temp4']] = ryder_df["album"].apply(lambda x: pd.Series(str(x).split(":")))
    ryder_df = ryder_df.drop(['temp1', 'temp2', 'temp4'], axis=1)
    ryder_df['album'] = ryder_df['album'].str.replace('}','',regex=True)
    ryder_df['album'] = ryder_df['album'].str.replace("'",'')
    ryder_df['album'] = ryder_df['album'].str.replace('"','')

    #DATE
    ryder_df[['temp1', 'date', 'time']] = ryder_df["date"].apply(lambda x: pd.Series(str(x).split(",")))
    ryder_df = ryder_df.drop(['temp1'], axis=1)
    ryder_df[['temp1', 'temp2', 'day', 'month', 'year']] = ryder_df["date"].apply(lambda x: pd.Series(str(x).split(" ")))
    ryder_df = ryder_df.drop(['temp1', 'temp2', 'date'], axis=1)
    ryder_df['time'] = ryder_df['time'].str.replace('}','',regex=True)
    ryder_df['time'] = ryder_df['time'].str.replace("'",'')
    ryder_df['day'] = ryder_df['day'].str.replace("'",'')
    decoder = {'Jan' : 1 , 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May': 5, 'Jun': 6, 
            'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec':12}
    ser = ryder_df["month"]
    for key in decoder:
        ser.replace(key, decoder[key], inplace=True)

    return ryder_df

def graph_jack_monthly_plays(jack_df):
    month_df = jack_df["Month"].value_counts(sort=False)
    plt.bar(month_df.index, month_df)
    plt.xticks(ha="right", rotation=45)
    plt.title("Total Monthly Plays")
    plt.xlabel("Date")
    plt.ylabel("Number of Songs Played")
    plt.tight_layout()

def graph_jack_favorite_artists(jack_df):
    artists_df = jack_df["artistName"].value_counts()
    plt.bar(artists_df.index[0:24], artists_df[0:24])
    plt.xticks(rotation=45, ha="right")
    plt.title("Artist's total songs played")
    plt.xlabel("Artist")
    plt.ylabel("Times Played")
    plt.tight_layout()

def graph_ryder_monthly_plays(ryder_df):
    month_df = ryder_df["month"].value_counts(sort=False)
    plt.bar(month_df.index, month_df)
    plt.xticks(ha="right", rotation=45)
    plt.title("Total Monthly Plays")
    plt.xlabel("Date")
    plt.ylabel("Number of Songs Played")
    plt.tight_layout()

def graph_ryder_favorite_artists(ryder_df):
    artists_df = ryder_df["artist"].value_counts()
    plt.bar(artists_df.index[0:24], artists_df[0:24])
    plt.xticks(rotation=45, ha="right")
    plt.title("Artist's total songs played")
    plt.xlabel("Artist")
    plt.ylabel("Times Played")
    plt.tight_layout()

def get_jack_kNN(jack_df):

    X = jack_df.drop('Month', axis=1)
    y = jack_df.Month

    tree_clf = DecisionTreeClassifier(random_state=0, max_depth=3)

    tree_clf.fit(X, y)

    plt.figure(figsize=(16, 9))
    plot_tree(tree_clf, feature_names=X.columns, class_names={1: "survived", 0: "died"}, filled=True, fontsize=10)

    scaler = MinMaxScaler()
    scaler.fit(X)
    X_normalized = scaler.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, random_state=0, stratify=y)

    knn_clf = KNeighborsClassifier(n_neighbors=3)
    knn_clf.fit(X_train, y_train)