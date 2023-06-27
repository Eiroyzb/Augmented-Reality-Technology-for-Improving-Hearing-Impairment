import subprocess
import time

RTSP_URL = "rtsp://127.0.0.1/live.sdp"  # 替换为实际的 RTSP URL
OUTPUT_FOLDER = "./audio/"  # 替换为保存音频文件的目录路径
RECORD_DURATION = 10  # 录取音频的持续时间（秒）
SAVE_INTERVAL = 10  # 保存音频的时间间隔（秒）
counter = 0  # 保存文件的计数器

def save_audio(file_path):
    global counter
    output_path = f"{OUTPUT_FOLDER}{counter}.wav"
    subprocess.call(["ffmpeg", '-y',"-i", file_path, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1", output_path])
    print(f"保存音频文件: {output_path}")
    counter += 1

def record_audio():
    while True:
        file_path = f"{OUTPUT_FOLDER}temp.wav"
        subprocess.call(["ffmpeg",'-y' ,"-i", RTSP_URL, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1", "-t", str(RECORD_DURATION), file_path])
        save_audio(file_path)
        time.sleep(SAVE_INTERVAL - RECORD_DURATION)

# 启动录音和保存音频的过程
record_audio()
