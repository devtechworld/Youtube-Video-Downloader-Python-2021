from pytube import YouTube

url  = 'url of video here'

download_video = YouTube(url)

print(download_video.title)

print(download_video.thumbnail_url)

download_video = download_video.streams.get_highest_resolution()



download_video.download()


