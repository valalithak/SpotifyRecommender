# -*- coding: utf-8 -*-
import os
import sys 
import pickle
import numpy as np 
import pandas as pd

input_from_ui = sys.argv[1]

input_song_names = input_from_ui.split(',')
print("final_list " , input_song_names)
# input_song_names  = sys.argv[1]
#input_song_names = ['Agar Tum Saath Ho', 'Humse Pyaar Kar Le Tu']

song_ids = []
with open('weights22kwithfeatures.pickle', 'rb') as f:
    model_weights = pickle.load(f)

playlist_matrix = model_weights[0]
songs_matrix = model_weights[1]

''' Weighting each feature 
 11 features : features = ['Danceability','Instrumentalness','Loudness','Speechiness','Valence','Energy','Mode','Tempo','Livenss','Key','Acousticness'] '''
weights=[0.75, 2, 2, 1, 1, 0.5, 0.05, 1, 0.5, 0.5, 0.75] 
songs_matrix_weighted = songs_matrix * weights[:np.newaxis]

def cosine_similarity(word_vectors,track_id,n):
  cosine_dict = {}
  word_list = []
  index = track_id -1 
  target = word_vectors[index,:]
  for i in range(0,word_vectors.shape[0]):
    curr = word_vectors[i]
    cos_sim = np.dot(curr,target)/(np.linalg.norm(curr)*np.linalg.norm(target))
    cosine_dict[i]=cos_sim
  dist_sort=sorted(cosine_dict.items(), key=lambda dist: dist[1],reverse = True)
  for item in dist_sort:
    word_list.append((item[0]+1,item[1]))
  return word_list[0:n]


train = pd.read_csv('22kPlaylist+features+songindex+artistindex.csv')
train.head()

for song_name in input_song_names:
  rows = train.loc[train['track_name'] == song_name]
  try:
    song_id = rows['trackindex'].to_list()[0]
    song_ids.append(song_id)
  except:
    song_id = -1

similar_song_ids = []
rec_ids = set()
for input_id in song_ids:
  # print(input_id)
  get = cosine_similarity(songs_matrix_weighted,input_id,5)
  for rec_id in get:
    if rec_id not in rec_ids:
      rec_ids.add(rec_id)
      temp = []
      temp.append(rec_id[1])
      temp.append(rec_id[0])  
      temp.append(input_id)
      if temp[1] != temp[2]: #input song and recommended song shouldn't be the same
        similar_song_ids.append(temp)
similar_song_ids.sort()


most_popular = ['HUMBLE', 'One Dance', 'Closer', 'Broccoli ft. Lil Yatchy', 'Congratulations', 'Bad and Boujee', 'Caroline', 'Bounce Back', 'Location', 'Mask Off', 'Despacito - Remix', "I'm the One", 'Toxic', 'Crazy In Love', 'Rock Your Body', "It Wasn't Me", 'Yeah!', 'My Boo', 'Buttons', 'Say My Name', 'Hey Ya! - Radio Mix / Club Mix']
output_list_1 = []
for track in similar_song_ids:
  inp_rows = train.loc[train['trackindex'] == track[2]]
  inp_song  = inp_rows['track_name'].tolist()[0]
  rows = train.loc[train['trackindex'] == track[1]]
  song_name = rows['track_name'].tolist()
  output_list_1.append(song_name[0])
if len(similar_song_ids) == 0:
  for song in most_popular:
    output_list_1.append(song)


with open('Artists-weights22kwithfeatures.pickle', 'rb') as f:
    model_weights = pickle.load(f)

artist_matrix = model_weights[0]
songs_matrix_2 = model_weights[1]

similar_song_ids = []
rec_ids = set()
for input_id in song_ids:
  # print(input_id)
  get = cosine_similarity(songs_matrix_2,input_id,5)
  for rec_id in get:
    if rec_id not in rec_ids:
      rec_ids.add(rec_id)
      temp = []
      temp.append(rec_id[1])
      temp.append(rec_id[0])  
      temp.append(input_id)
      if temp[1] != temp[2]: #input song and recommended song shouldn't be the same
        similar_song_ids.append(temp)
similar_song_ids.sort()


output_list_2 = []
for track in similar_song_ids:
  inp_rows = train.loc[train['trackindex'] == track[2]]
  inp_song  = inp_rows['track_name'].tolist()[0]
  rows = train.loc[train['trackindex'] == track[1]]
  song_name = rows['track_name'].tolist()
  output_list_2.append(song_name[0])
if len(similar_song_ids) == 0:
  for song in most_popular:
    output_list_2.append(song)


"""Final step: Combine both recommendations given by Artist and Playlist based representations"""
f = open('output.txt','w')
n1 = int(len(output_list_1)/2)-1
n2 = int(len(output_list_2)/2)-1
final_list = output_list_1[0:n1] + output_list_2[0:n2]
for song in final_list:
  print(song)
  song = song + '\n'
  f.write(song)
f.close()