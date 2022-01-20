from googleapiclient.discovery import build

DEVELOPER_KEY = "PUTAPIKEYHERE"
channel_name = "PUTCHANNELNAMEHERE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
        q = channel_name,
        type = "channel",
        order = "relevance",
        part = "snippet",
        maxResults = 50
        ).execute()

channel_id = search_response['items'][0]['id']['channelId']

playlists = youtube.playlists().list(
        channelId = channel_id,
        part = "snippet",
        maxResults = 50
        ).execute()

ids = []
for i in playlists['items'] :
    ids.append(i['id'])

num=int(input())
if num > (len(ids) - 1) or num < 0 :
        print("Input a playlist index of %s." %channel_name)
        print("The range of the input is from %d to %d." % (0, len(ids)-1))
        exit()
playlist_selected=ids[num]
playlistitems_list_response = youtube.playlistItems().list(
        playlistId= playlist_selected,
        part = "snippet",
        maxResults = 50,
        ).execute()

video_ids = []
for v in playlistitems_list_response['items'] :
    video_ids.append(v['snippet']['resourceId']['videoId'])

title = []
views = []
likes = []
comments = []

for u in range(len(video_ids)):
    request = youtube.videos().list(
            part = "snippet, statistics",
            id = video_ids[u]
            )
    response = request.execute()

    if not response['items'] == [] :
        title.append(response['items'][0]['snippet']['title'])
        views.append(response['items'][0]['statistics']['viewCount'])
        likes.append(response['items'][0]['statistics']['likeCount'])
        comments.append(response['items'][0]['statistics']['commentCount'])

import pandas as pd

df = pd.DataFrame([title, views, likes, comments]).T
df.columns = ['Title', 'Views', 'Likes', 'Comments']

from tabulate import tabulate

print(tabulate(df, headers='keys', tablefmt='psql'))