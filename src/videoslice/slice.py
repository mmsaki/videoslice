from typing import List, Union

from videoslice.program_runner import ProgramRunner


def slice_video(ffmpeg_args: Union[List[str], str], log=True) -> int:
    """Slices a video using ffmpeg."""
    p = ProgramRunner(ffmpeg_args)
    return p.run(log=log)


def slice_video_args(start, end, source, destination) -> List[str]:
    """
    Cuts a video from start to end time.
        :param start: Start time in HH:MM:SS format.
        :param end: End time in HH:MM:SS format.
        :param source: Path to the source video file.
        :param destination: Path to save the cut video file.
    """
    args = [
        "ffmpeg",
        "-ss",
        start,
        "-to",
        end,
        "-i",
        source,
        "-vcodec",
        "libx264",
        "-acodec",
        "aac",
        "-c",
        "copy",
        "-y",
        destination,
    ]

    return args


def twitter_format_args(input_video: str, output_video) -> str:
    """
    Returns the ffmpeg arguments for converting a video to Twitter format.
    """
    args = [
        "ffmpeg",
        "-i",
        input_video,
        "-filter:v",
        "\"scale='min(1280,iw)':min'(720,ih)':force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2\"",
        "-pix_fmt",
        "yuv420p",
        output_video,
    ]
    return " ".join(args)
