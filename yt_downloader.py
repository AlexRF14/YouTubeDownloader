import shutil
from yt_dlp import YoutubeDL
from cookies_helper import get_cookies_opts

def download_video(url, cookies_file=None):
    node_path = shutil.which("node")
    
    ydl_opts = {
        "outtmpl": "downloads/%(title)s [%(id)s].%(ext)s",
        "format": "bestvideo*+bestaudio/best/bestvideo+bestaudio/best",
        "merge_output_format": "mp4",  # optional: merge into mp4
        "allow_unplayable_formats": False,
        "remote_components": ["ejs:github"],
    }
    
    if node_path:
        print("Node.js on the device")
        ydl_opts["js_runtimes"] = {"node": {}}
    else:
        print("Node.js not on the device, slower donwload")

    ydl_opts.update(get_cookies_opts(cookies_file))

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    cookies_file = "cookies.txt"
    if url:
        download_video(url)
        print("Download finished.")
    else:
        print("URL no válida.")