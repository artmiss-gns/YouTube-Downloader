# YouTube Downloader

This is a command line program for downloading YouTube videos written in Python. It provides a simple interface using Click.

## Usage

The downloader can be used to fetch a single video or full playlist.

To download a single video:

```
python main.py download [VIDEO_URL]
```

To download a full playlist: 

```
python main.py download [PLAYLIST_URL] 
```

By default videos will be saved to `~/Downloads` but a custom destination can be specified with the `-d` flag:

```
python main.py download -d /path/to/videos [URL]
```

## Requirements

This program requires Python 3 and the following Python packages:

- Click
- PyTube

Install requirements with `pip`:

```
pip install click pytube
```

## Implementation

The main entrypoint is `main.py` which provides a Click interface. This handles parsing commands and arguments.

The `YouTubeDownloader` class in `youtube_downloader.py` contains methods for fetching YouTube video data, downloading, and handling playlists.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Let me know if you would like me to explain or expand on any part of this README!