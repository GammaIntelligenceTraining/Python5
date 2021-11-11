import os
import re
from googleapiclient.discovery import build
from datetime import timedelta

api_key = 'AIzaSyDNil9I4v0ZCSXerNPqkXNdCWbMrDtPwYc'

service = build('youtube', 'v3', developerKey=api_key)

request = service.channels().list(part='contentDetails, statistics', forUsername='visitestonia')

pl_request = service.playlists().list(
    part='contentDetails, snippet',
    channelId='UCw8wdYrQcit2Aqj79ZZefww'
)

new_request = service.playlistItems().list(
    part='contentDetails',
    playlistId='PLLPaxzl-wq-wgZmKemIUi4XvX8WQjlLQJ'
)

response = request.execute()
pl_response = pl_request.execute()
new_response = new_request.execute()
#
# print(response)
# print(pl_response)
# for item in pl_response['items']:
#     print(item)
#     print()

vid_id_list = []
for video in new_response['items']:
    vid_id = video['contentDetails']['videoId']
    vid_id_list.append(vid_id)

vid_request = service.videos().list(
    part='contentDetails',
    id=','.join(vid_id_list)
    )
vid_response = vid_request.execute()

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

# for item in vid_response['items']:
#     duration = item['contentDetails']['duration']
#     print(duration)
#     print()

play_list_length = 0
for item in vid_response['items']:
    duration = item['contentDetails']['duration']

    hours = hours_pattern.search(duration)
    minutes = minutes_pattern.search(duration)
    seconds = seconds_pattern.search(duration)

    hours = int(hours.group(1)) if hours else 0
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1)) if seconds else 0

    length = timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()
    play_list_length += length

    print(hours, minutes, seconds)
print(timedelta(seconds=219))