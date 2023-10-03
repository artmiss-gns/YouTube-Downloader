import pytube
from pytube.cli import on_progress

import re
from termcolor import colored


class YouTubeDownloader:
    def __init__(self, destination: str, url: str) -> None : 
        self.destination = destination
        self.links = YouTubeDownloader.get_links(url)
        self.available_resolutions = ['720p', '480p',]
        self.max_retries = 1

    def download(self) -> None :
        print(colored('Connecting to YouTube...', color='white', attrs=['bold'], on_color='on_grey'))
        for file_number, l in enumerate(self.links) :
            yt = pytube.YouTube(l,
                on_progress_callback=on_progress,
            )
        
            stream = None
            for res in self.available_resolutions:
                stream = yt.streams.get_by_resolution(res)
                if stream is not None:
                    break

            if stream is None:
                stream = yt.streams.get_lowest_resolution()

            if stream :
                print(colored('Starting the Download process...', color='white', attrs=['bold'], on_color='on_grey'))
                print(colored(f"File Name :{stream.title}", color='cyan',))
            
                file_name = self.build_sanitized_filename(stream.title, file_number)
                stream.download(
                    output_path=self.destination,
                    filename= file_name,
                    max_retries=self.max_retries,
                    )
            print(colored('\nFile Downloaded!\n', color='grey',
                          attrs=['bold',], on_color='on_green'))
            
    
    @staticmethod 
    def build_sanitized_filename(name: str, number: int) -> str :
        sanitized_chars = ['/', '\\', ':', ';', '|', '?', '*', '"', "'", '<', '>', ' ']
        name = ''.join([char for char in name if char not in sanitized_chars])
        return f"{number}_{name}.mp4"
        
        
    @classmethod
    def get_links(cls, link) :
        print(colored('Gathering links...', color='white', attrs=['bold', ], on_color='on_grey'))
        if cls.is_playlist(link) :
            playlist = pytube.Playlist(link)
            links = playlist.video_urls 
        else : 
            links = [link]
            
        return links
    

    @staticmethod
    def is_playlist(link) :
        pattern = re.compile('youtube.com/playlist')
        if pattern.findall(link) : 
            return True
        return False
    
