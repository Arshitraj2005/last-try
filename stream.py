import subprocess
import config

process = None

def start_streaming():
    global process
    command = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",
        "-i", config.VIDEO_URL,
        "-f", "lavfi",
        "-i", "anullsrc",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "128k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-f", "flv",
        f"rtmp://a.rtmp.youtube.com/live2/{config.STREAM_KEY}"
    ]
    process = subprocess.Popen(command)

def stop_streaming():
    global process
    if process:
        process.terminate()
        process = None

def check_status():
    return process is not None

