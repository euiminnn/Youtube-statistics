from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "PUTAPIKEYHERE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
        q = "PUTCHANNELNAMEHERE",
        order = "relevance",
        part = "snippet",
        maxResults = 50
        ).execute()

channel_id = search_response['items'][0]['id']['channelId']

playlists = youtube.playlists().list(
        channelId = channel_id,
        part = "snippet",
        maxResults = 20
        ).execute()

import pandas as pd

ids = []
titles = []
for i in playlists['items'] :
    ids.append(i['id'])
    titles.append(i['snippet']['title'])

df=pd.DataFrame([ids, titles]).T
df.columns=['PlayLists', 'Titles']

#print(df)

num=int(input())
playlist_selected=df['PlayLists'][num]
playlist_videos=youtube.playlistItems().list(
        playlistId= playlist_selected,
        part = "snippet",
        maxResults = 50,
        )
playlistitems_list_response = playlist_videos.execute()

video_names = []
video_ids = []
date = []

for v in playlistitems_list_response['items'] :
    video_names.append(v['snippet']['title'])
    video_ids.append(v['snippet']['resourceId']['videoId'])
    date.append(v['snippet']['publishedAt'])
vdf = pd.DataFrame([date, video_names, video_ids]).T
vdf.columns = ['Date', 'Title', 'IDS']

#print(vdf)

import re
category_id = []
views = []
likes = []
dislikes = []
comments = []
mins = []
seconds = []
title = []

for u in range(len(vdf)):
    request = youtube.videos().list(
            part = "snippet, contentDetails, statistics",
            id = vdf['IDS'][u]
            )
    response = request.execute()

    if response['items'] == [] :
        ids.append("-")
        category_id.append("-")
        views.append("-")
        likes.append("-")
        #dislikes.append("-")
        comments.append("-")
    else :
        title.append(response['items'][0]['snippet']['title'])
        category_id.append(response['items'][0]['snippet']['categoryId'])
        views.append(response['items'][0]['statistics']['viewCount'])
        likes.append(response['items'][0]['statistics']['likeCount'])
        #dislikes.append(response['items'][0]['statistics']['dislikeCount'])
        comments.append(response['items'][0]['statistics']['commentCount'])

sdf = pd.DataFrame([title, category_id, views, likes, comments]).T
sdf.columns = ['Title', 'Category_id', 'Views', 'Likes', 'Comments']

from tabulate import tabulate
#print(tabulate(df, headers='keys', tablefmt='psql'))
#print(tabulate(vdf, headers='keys', tablefmt='psql'))
print(tabulate(sdf, headers='keys', tablefmt='psql'))
