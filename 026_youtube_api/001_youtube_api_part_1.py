from googleapiclient.discovery import build
# google api documentation
# https://github.com/googleapis/google-api-python-client

# pip install google-api-python-client

# youtube api documentation
# https://developers.google.com/youtube/v3

api_key = 'AIzaSyDNil9I4v0ZCSXerNPqkXNdCWbMrDtPwYc'

service = build('youtube', 'v3', developerKey=api_key)

request = service.channels().list(
    part='statistics',
    forUsername='visitestonia'
)
response = request.execute()
print(response)