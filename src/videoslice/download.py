from typing import List
from videoslice.logger import MyCustomPP, MyLogger, my_hook
from videoslice.program_runner import ProgramRunner
import yt_dlp


def download_runner(ytdlp_args: List[str], log=True) -> int:
    """
    Downloads a video using yt-dlp with the provided arguments.
        :param ytdlp_args: Arguments for yt-dlp as a string.
        :param log: Whether to log the output command.
        :return: Exit code of the yt-dlp command.
    """
    p = ProgramRunner(" ".join(ytdlp_args))
    return p.run(log=log)


def get_ydl_opts(url: str, destination: str) -> dict:
    ydl_opts = {
        "cookiesfrombrowser": ("chrome", None, None, None),
        "extract_flat": "discard_in_playlist",
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b",
        "fragment_retries": 10,
        "ignoreerrors": "only_download",
        "outtmpl": {"default": destination},
        "postprocessors": [
            {"key": "FFmpegConcat", "only_multi_video": True, "when": "playlist"}
        ],
        "retries": 10,
        "logger": MyLogger(),
        "progress_hooks": [my_hook],
    }
    return ydl_opts


def youtube_download_args(url: str, destination: str) -> List[str]:
    """
    Downloads a video using yt-dlp.
        :param url: URL YouTube video.
        :param destination: Path to save video file.
    """
    args = [
        "yt-dlp",
        "-f",
        "'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b'",
        url,
        "-o",
        destination,
        "--cookies-from-browser",
        "chrome",
    ]

    return args
