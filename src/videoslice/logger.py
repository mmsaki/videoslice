import yt_dlp


class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith("[debug] "):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


# ℹ️ See help(yt_dlp.postprocessor.PostProcessor)
yt_dlp.postprocessor.PostProcessor


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def run(self, information):
        self.to_screen("Doing stuff")
        return [], information


# ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)
yt_dlp.YoutubeDL


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now post-processing ...")
