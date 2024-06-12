import pytube
from pytube import Playlist
import keyboard


def downloadVideo(url):
    youtube = pytube.YouTube(url)

    i = 1
    for liste in youtube.streams.order_by('resolution'):
        try:
            print(liste)
            i += 1
        except:
            pass

    video = youtube.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').last()

    # Title of the video
    title = video.title
    print("Downloading : " + str(title))

    # Path of where to download
    video.download('./downloads/')

    print("Download succeed")


# Download full playlist
def downloadPlaylist(url_playlist):
    pl = Playlist(url_playlist)
    i = 1
    print("Initialisation")
    for video in (pl.videos):
        video.streams.filter(progressive=True, file_extension="mp4").order_by(
            'resolution').get_highest_resolution().download("D:/fun/youtube downloader")
        try:
            # Title of the video
            title = video.title
            print("Video " + str(i) + ": " + str(title) + " Download succeed")
            i += 1
        except:
            pass
            print("Error")


# Download a part of the playlist
def downloadPlaylistPart(url_playlist, start, end):
    pl = Playlist(url_playlist)
    i = 1
    print("Initialisation")
    for video in (pl.videos[start - 1:end:1]):
        # here we used start and end to specify wich part of the playlist if we don't want to download it all
        video.streams.filter(progressive=True, file_extension="mp4").order_by(
            'resolution').get_highest_resolution().download("path")
        try:
            # Title of the video
            title = video.title
            print("Video " + str(i) + ": " + str(title) + " Download succeed")
            i += 1
        except:
            pass
            print("Error")

link = str(input("Video link :\n"))
downloadVideo(link)
# downloadPlaylist("")
# downloadPlaylistPart("",10,13)



print("Press 'q' to quit.")

# Wait until 'q' is pressed
while True:
    if keyboard.is_pressed('q'):
        print("Exiting...")
        break

















