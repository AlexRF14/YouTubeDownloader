from yt_dlp import YoutubeDL

def download_video(url):
    ydl_opts = {
        "outtmpl": "downloads/%(title)s [%(id)s].%(ext)s",
        "format": "bestvideo*+bestaudio/best",
        "js_runtimes": {"node": {}},
        "merge_output_format": "mp4"  # optional: merge into mp4
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    download_video(url)
    print("Download finished.")