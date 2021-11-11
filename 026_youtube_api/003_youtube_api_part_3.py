import re
from googleapiclient.discovery import build
from datetime import timedelta

api_key = 'AIzaSyDNil9I4v0ZCSXerNPqkXNdCWbMrDtPwYc'

service = build('youtube', 'v3', developerKey=api_key)

nextPageToken = None

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

play_list_length = 0
while True:
    new_request = service.playlistItems().list(
        part='contentDetails',
        playlistId='PLLPaxzl-wq-wkcRzzVhmgyIhozs6O3SNI',
        maxResults=50,
        pageToken=nextPageToken
    )

    new_response = new_request.execute()

    vid_id_list = []
    for video in new_response['items']:
        vid_id = video['contentDetails']['videoId']
        vid_id_list.append(vid_id)

    vid_request = service.videos().list(
        part='contentDetails',
        id=','.join(vid_id_list)
        )
    vid_response = vid_request.execute()


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

        print(length)
        print()

    nextPageToken = new_response.get('nextPageToken')
    if not nextPageToken:
        break

print(play_list_length)

play_list_length = int(play_list_length)

minutes, seconds = divmod(play_list_length, 60)
hours, minutes = divmod(minutes, 60)
print(f'Hours: {hours}, Minutes: {minutes}, Seconds {seconds}')