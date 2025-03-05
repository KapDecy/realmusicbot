from yt_dlp import YoutubeDL

# url = f"https://www.youtube.com/watch?v={video_id}"
url = "https://www.youtube.com/watch?v=wp43OdtAAkM"
info = {}
# with YoutubeDL(params={"quiet": True, "format": str(itag), 'cookiesfrombrowser': ('vivaldi', None, None, None)}) as ydl:
with YoutubeDL(params={"proxy": "socks5://127.0.0.1:2080/", "quiet": True, 'cookiesfrombrowser': ('vivaldi', None, None, None)}) as ydl:
    info = ydl.extract_info(url, download=False)

print(info)

# author = info.get("uploader", "")
# if " - Topic" in author:
#     title = author.replace(" - Topic", "") + " - " + info.get("title", "")
# else:
#     title = info.get("title", "")

# duration = convert_duration(info.get("duration", 0))
# stream = info.get("url", "")

# return title, duration, stream, url