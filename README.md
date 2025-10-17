# Video Reel Creator

An automated Python tool for creating and uploading Instagram reels. This project handles audio trimming, video clipping, caption overlays, and automated Instagram uploads.

## Features

- **Audio Trimming** (`audiocut.py`): Extract specific segments from audio files
- **Video Clipping** (`clipper.py`): Separate videos into shorter subclips and download videos from YouTube at up to 1080p
- **Reel Creation** (`editor.py`): Combine random video clips, overlay captions, and sync with audio
- **Auto Upload** (`upload.py`): Automatically upload finished reels to Instagram using Selenium

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Instagram credentials:
```
USERNAME=your_username
PASSWORD=your_password
```

3. Organize your media:
```
project/
├── audio/          # Audio files for syncing
├── videos/         # Organized by folder (e.g., CURRY/, LEBRON/)
├── OUTPUT/         # Stores final edited video
└── FINAL/          # Temporary reel storage
```

## Usage

Run the main editor:
```bash
python editor.py
```

You'll be prompted to enter:
- Caption text (supports line breaks with `\n`)
- Video folder name
- Audio track name (headlock, killshot, night, tekit)
- Number of random videos to combine

The script generates a final video in `OUTPUT/final.mp4` and optionally uploads it to Instagram.

## Requirements

- Python 3.x
- moviepy, yt_dlp, Selenium, Pillow (see `requirements.txt`)