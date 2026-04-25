# YouTube video downloader

This is a simple YouTube video downloader written in Python. It uses the `pytube` library to download videos from YouTube. The script prompts the user for a YouTube URL and then downloads the video to the current working directory.

To use this script, you need to have Python installed on your Linux system. You also need to install the `pytube` library, which can be done using pip:

# How to run it
Use requirements.txt file to install dependencies on your venv

```bash
pip install -r requirements.txt
```

Here is how you run it:

```bash
python yt_downloader.py
```

Make sure to enter a valid YouTube URL when prompted. The video will be downloaded in the highest resolution available. After the download is complete, a message will be printed to the console.
Note: This script does not handle errors gracefully and may crash if there are issues with the YouTube video or network connectivity. You should always check the output of the script for any errors before proceeding with

# For Windows users:

To run it on Windows, you must have this downloaded:
https://www.gyan.dev/ffmpeg/builds/

# Node.js

If you have node.js it will download faster.