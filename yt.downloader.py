import youtube_dl

url = input("Enter url to start downloading your video : \n")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download([url])

# import youtube_dl

# url = input("Enter the URL of the YouTube video you want to download: \n")

# try:
#     with youtube_dl.YoutubeDL() as ydl:
#         ydl.download([url])
#         print("Download completed successfully!")
# except youtube_dl.DownloadError as e:
#     print(f"Error downloading video: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")



# import youtube_dl

# url = input("Enter url to start downloading your video : ")

# try:
#     with youtube_dl.YoutubeDL() as ydl:
#         ydl.download([url])
# except Exception as e:
#     print(e)
