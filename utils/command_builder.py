import subprocess

def extract_audio_with_ffmpeg(ffmpeg_path: str, video_path: str, output_name: str):
    command = f'"{ffmpeg_path}" -i "{video_path}" -vn -c:a copy "{output_name}.m4a"'
    subprocess.run(command, shell=True)