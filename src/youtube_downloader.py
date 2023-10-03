import pytube
from pytube.cli import on_progress

import re
from termcolor import colored


class YouTubeDownloader:
    def __init__(self, destination, url) :
        self.destination = destination
        self.links = YouTubeDownloader.get_links(url)
         
        
    @classmethods
    def get_links(cls, link) :
        print(colored('Gathering links...', color='white', attrs=['bold', 'blink'], on_color='on_grey'))
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
    
