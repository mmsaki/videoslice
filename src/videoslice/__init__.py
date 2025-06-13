import argparse

import yt_dlp

from videoslice.download import get_ydl_opts, youtube_download_args, download_runner
from videoslice.logger import MyCustomPP
from videoslice.slice import slice_video_args, slice_video, twitter_format_args


def main() -> None:
    print("[Video Slice] 🎬 Hello! 👋🏾")
    parser = argparse.ArgumentParser(description="Video slicing utility")
    parser.add_argument(
        "--start",
        "-s",
        type=str,
        required=True,
        help="Start time in HH:MM:SS format",
    )
    parser.add_argument(
        "--end", "-e", type=str, required=True, help="End time in HH:MM:SS format"
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        required=True,
        help="Path to save the downloaded video file",
    )
    parser.add_argument(
        "--output", "-o", type=str, required=True, help="Path to save the sliced video"
    )
    parser.add_argument(
        "--url", "-u", type=str, required=False, help="URL of the video to download"
    )
    parser.add_argument(
        "--log",
        "-l",
        action="store_true",
        help="Enable logging of yt-dlp command and output",
    )
    parser.add_argument(
        "--twitter",
        "-t",
        action="store_true",
        help="Enable Twitter video format conversion.",
    )
    args = parser.parse_args()

    start = args.start
    end = args.end
    input_video = args.input
    output = args.output
    url = args.url
    log = args.log
    ytdlp_args = youtube_download_args(url, input_video)
    ffmpeg_args = slice_video_args(start, end, input_video, output)

    if url is not None:
        # download video
        status = download_runner(ytdlp_args, log=log)

        # slice video
        if status is None:
            print("[Video Slice] ❌ Failed to download video.")
        elif status != 0:
            print("[Video Slice] ❤️‍🩹 recived non-zero exit code from yt-dlp.")

    slice_status = slice_video(ffmpeg_args, log=log)
    if slice_status != 0:
        print("[Video Slice] ✂️ Failed to slice video.")
    else:
        print("[Video Slice] ✅ Video sliced successfully!")

    twitter = args.twitter
    if twitter:
        print("[Video Slice] 🐦 Converting video to Twitter format...")
        # Here you would add the logic to convert the video to Twitter format
        ffmpeg_args_twitter = twitter_format_args(output, "twitter_" + output)
        slice_video(ffmpeg_args_twitter, log=log)

    # ydl_opts = get_ydl_opts(url, input_video)
    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     # ℹ️ "when" can take any value in yt_dlp.utils.POSTPROCESS_WHEN
    #     ydl.add_post_processor(MyCustomPP(), when="pre_process")
    #     ydl.download(url)


if __name__ == "__main__":
    # example
    # videoslice -s 00:04:22 -e 00:05:40 -i cursor.mp4 -o cursor.mp4 -u https://youtu.be/sLaxGAL_Pl0 --log
    main()
