from pytube import YouTube
from pytube.cli import on_progress


def get_resolution(yt: YouTube) -> list:
    """
    Given a Youtube url, gets the available resolutions as a list.

    :param str yt:
        A valid Youtube object.
    """
    res = []
    for stream in yt.streams:
        res.append(stream.resolution)

    res = list(map(lambda x:x.strip("p"), set(filter(None, res))))
    res.sort(key=int)
    
    return res



def download_video(url: str, outpath: str = "./assets") -> None:
    """Download a youtube video with lowest resolution.

    :param str url:
        A valid Youtube url.
    :param str outpath:
        Target directory for download
    """
    yt = YouTube(url, on_progress_callback=on_progress)
    
    # Video as a streams.Stream object
    video = yt.streams.filter(file_extension="mp4", resolution=(get_resolution(yt)[0] + "p")).first().download(outpath)