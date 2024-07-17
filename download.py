import yt_dlp
import os
import parameters as p


def clear_youtube_files():
    files = os.listdir(p.video_location)
    verified_files = [file for file in files if '.mkv' in file]
    for file in files:
        if file not in verified_files:
            os.remove('%s%s' % (p.video_location, file))


def format_title(title):
	return title.lower().replace(' ', '_').replace('_-', '')


def youtube(url, alternate_title = 'a'):
    title = alternate_title
    if alternate_title == 'a':
        with yt_dlp.YoutubeDL({'quiet' : True}) as ydl:
            title = format_title(ydl.extract_info(url, download = False)['title'])
    ydl_opts = {
        'format'               : 'bestvideo+bestaudio/best',
        'outtmpl'              : f'{p.video_location}{title}.%(ext)s',
        'prefer_ffmpeg'        : True,
        'keepvideo'            : True,
        'merge_output_format'  : 'mkv'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    clear_youtube_files()


def youtube_music(url, alternate_title = 'a'):
    title = alternate_title
    if alternate_title == 'a':
        with yt_dlp.YoutubeDL({'quiet' : True}) as ydl:
            title = format_title(ydl.extract_info(url, download = False)['title'])
    ydl_opts = {
        'format'  : 'bestaudio/best',
        'outtmpl' : f'{p.music_location}/{title}.%(ext)s',
        'postprocessors' : [{
            'key'              : 'FFmpegExtractAudio',
            'preferredcodec'   : 'mp3',
            'preferredquality' : '192'
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])