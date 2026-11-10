# Video Downloader

A simple desktop app for downloading videos and audio from YouTube (and other sites supported by [yt-dlp](https://github.com/yt-dlp/yt-dlp)). Paste a link, pick a format, choose a folder, and click download.

Built with Python, [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and yt-dlp.

<!-- Add a screenshot: put it in assets/screenshot.png and uncomment the line below -->
<!-- ![Screenshot](assets/screenshot.png) -->

## Features

- Clean, modern GUI (CustomTkinter)
- Video formats: **MP4, MKV, WebM**
- Audio formats: **MP3, M4A, OGG**
- Optional **recode** to the selected format
- Choose where files are saved
- Checks that the link is valid before downloading
- Updates yt-dlp automatically each time the app starts

## Requirements

- **Windows** (the packaged `.exe` is Windows-only; running from source should work on other systems too)
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp#installation)** available on your PATH
- **[ffmpeg](https://ffmpeg.org/download.html)** available on your PATH (needed for MP3/M4A/OGG, recoding and merging video and audio)
- Python 3.8+ (only if you run from source)

> The app calls `yt-dlp` as a command, so yt-dlp and ffmpeg must be installed and on your PATH even if you use the `.exe`.

## Download

Grab the latest `videodownloader_v5.exe` from the [**Releases**](../../releases) page.

> Windows or your antivirus may show a warning because the app is unsigned. This is common for apps packaged with PyInstaller. The full source code is in this repo if you want to check it or build it yourself.

## Run from source

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install -r requirements.txt
python videodownloader_v5.py
```

## Usage

1. Paste a video link into the text box.
2. Pick a format from the dropdown (MP4, MKV, WebM, MP3, M4A, OGG).
3. Click the folder button and choose where to save.
4. Tick **recode video to wanted format** if you want the file converted (slower, needs ffmpeg).
5. Click **download video** and wait for the bar to finish.

## Build the .exe yourself

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --collect-all customtkinter videodownloader_v5.py
```

The executable will be in the `dist/` folder.

## Project structure

```
.
├── videodownloader_v5.py   # the app
├── requirements.txt        # Python dependencies
├── README.md
└── LICENSE
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `'yt-dlp' is not recognized` | Install yt-dlp and make sure it is on your PATH. |
| MP3/M4A/OGG fail or no sound in video | Install ffmpeg and add it to your PATH. |
| "video not downloaded retry" | Check the link, your internet connection, and that yt-dlp is up to date (`yt-dlp -U`). |
| Antivirus flags the .exe | False positive for unsigned PyInstaller apps. Build from source if unsure. |

## Legal disclaimer

This tool is for **personal use** with content you have the right to download. Downloading copyrighted material without permission, or in violation of a website's Terms of Service (including YouTube's), may be illegal. You are responsible for how you use this software. The author is not affiliated with YouTube or Google and accepts no liability for misuse.

## Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [ffmpeg](https://ffmpeg.org/)

## License

MIT. See [LICENSE](LICENSE). (Add a `LICENSE` file, or change this line to match the license you choose.)
