import click
from youtube_downloader import YouTubeDownloader 

@click.group()
def commands() :
    pass

@click.command()
@click.option(
    "-d", "--destination",
    show_default=True,
    prompt="Download storing location: ",
    prompt_required=False,
    help="Storing address for downloaded file/files"
)
@click.argument(
    "url",
    required=True,
)
def download(url, destination="~/Downloads") :
    yt = YouTubeDownloader(destination, url)
    yt.download()



if __name__ == "__main__" :
    commands.add_command(download)

    commands()