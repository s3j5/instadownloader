# import yt_dlp
# import os

# DOWNLOAD_FOLDER = "app/static/downloads"

# if not os.path.exists(DOWNLOAD_FOLDER):
#     os.makedirs(DOWNLOAD_FOLDER)


# def download_video(url):
#     ydl_opts = {
#         'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
#         'format': 'best',
#         'noplaylist': True,
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         filename = ydl.prepare_filename(info)

#     # 👇 IMPORTANT FIX
#     file_name = os.path.basename(filename)
#     file_url = f"/static/downloads/{file_name}"

#     return {
#         "title": info.get("title"),
#         "file_url": file_url
#     }

import yt_dlp
import os

DOWNLOAD_FOLDER = "app/static/downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


# 🎥 VIDEO DOWNLOAD
# def download_video(url):
    # ydl_opts = {
    #     'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
    #     'format': 'bestvideo+bestaudio/best',
    #     'merge_output_format': 'mp4',
    #     'noplaylist': True,
    # }

    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     info = ydl.extract_info(url, download=True)
    #     filename = ydl.prepare_filename(info)

    # file_name = os.path.basename(filename)
    # file_url = f"/static/downloads/{file_name}"

    # return {
    #     "title": info.get("title"),
    #     "file_url": file_url
    # }

def download_instagram(url):
    import yt_dlp
    import os

    DOWNLOAD_FOLDER = "app/static/downloads"

    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'format': 'best',
        'noplaylist': True,

        # 🔥 FIXES
        'quiet': False,
        'nocheckcertificate': True,

        'http_headers': {
            'User-Agent': 'Mozilla/5.0',
            'Referer': 'https://www.instagram.com/',
        },

        # ⚡ timeout fix
        'socket_timeout': 10,
    }

    try:
        print("Downloading:", url)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            if not info:
                return {"status": "error", "message": "No data found"}

            filename = ydl.prepare_filename(info)

        file_name = os.path.basename(filename)
        file_url = f"/static/downloads/{file_name}"

        print("DONE")

        return {
            "status": "success",
            "title": info.get("title"),
            "file_url": file_url
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "status": "error",
            "message": str(e)
        }

        
def download_audio(url):
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',

        # ⚡ FASTEST METHOD
        'format': 'bestaudio[ext=m4a]/bestaudio',

        'noplaylist': True,

        # ❌ REMOVE conversion (slow)
        # no FFmpeg convert here
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    file_name = os.path.basename(filename)
    file_url = f"/static/downloads/{file_name}"

    return {
        "title": info.get("title"),
        "file_url": file_url
    }

# 🎵 AUDIO ONLY DOWNLOAD
# def download_audio(url):

    # ydl_opts = {
    #     'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
    #     'format': 'bestaudio',
    #     'noplaylist': True,

    #     # 👇 audio convert karega mp3 me
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '192',
    #     }],
    # }

    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     info = ydl.extract_info(url, download=True)
    #     filename = ydl.prepare_filename(info)

    # # 👇 extension change (mp3)
    # file_name = os.path.basename(filename).replace(".webm", ".mp3").replace(".m4a", ".mp3")
    # file_url = f"/static/downloads/{file_name}"

    # return {
    #     "title": info.get("title"),
    #     "file_url": file_url
    # }