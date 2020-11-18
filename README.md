# BUILDING RECOMMENDATION SYSTEM FOR SPOTIFY PLAYLIST

 ### Objective :
  Given a playlist of Spotify tracks, our objective is to build a recommendation system that is be able to recommend a list of tracks that would constitue an appropriate extension of the playlist.

 ### Data collection and Preprocessing : 
 We us the  Spotify Million PLaylist Dataset (MPD). The file structure consists of 10,000 .json subfiles, with each subfile containing 1,000 playlists.Apart from the existing attributes for each song we extracted a few more features using the Spotify API.So, finally each track in the dataset includes the following attributes:
 -  Album name
 -   ID
 -   Artist
 -   Track duration
 -   Track name
 -  Danceability
 -   Instrumentalness 
 -   Loudness
 -   Speechiness 
 -   Valence
 -   Energy
 -    Mode 
 -    Tempo
 -  Liveness 
 -  Key 
 -  Acousticness
 ![](images/data.png "Optional title")

 ### Models :
- **Nearest Neighbour based approach** :This is our baseline approach. We used song to song similarity here. Initailly, in the dataset, we performed PCA with eight components as that was needed for retaining 95% variance. After PCA, we used cosine similarity as the metric on the numeric features.For a given set of tracks, we generated the recommended tracks as the ones having the highest cosine similarity value.In order to inject some randomness in the recommendation, for every set of recommended tracks we added a track randomly without bothering about the cosine similarity values. This increases the diversity of our recommendation.

![](images/pca.png "PCA ")




- **Collaborative Filtering based approach** : Collaborative filtering was the next approach.
- **Neural Collaborative Filtering**   :Out of the previous two models, we found the CF based approach better and decided to improve upon that.

 ### Evaluation metric : 
 Since there is no definite metric to evaluate the recommendations, we devised a metric which is as follows :
 - If the recommended track's Artist or Album name matches with that of the given input track(s), it is considered to be a good recommendation.
 - The difference between the values of the features of the recommended track and the given input track is less than a specified threshold (0.2), and this is true for six out of the eleven features that we use, the recommended track is considered to be a good one.
 

### Results :

**Team** :\
Meenu Menon\
Yash Upadhyay\
Lalitha Kameswari\
Dama Sravani




