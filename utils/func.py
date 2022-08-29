from utils.bot import ChromeBot
from utils import command_builder
from utils.bot import ChromeBot
from utils.config import ConfigData
import utils.save as save
import os

def download_files(config: ConfigData, video_offset: int):
    bot = ChromeBot(config.chrome_driver_path)
    filename_prefix = config.output_filename
    for index, link in enumerate(config.video_links):
        src = bot.get_video_src(link)
        save.save_file(src, f'{filename_prefix} Rozdział {index+1+video_offset}.mp4')
    bot.close()

def extract_videos_to_audios(base_directory: str, config: ConfigData):
    mypath = os.path.curdir
    downloaded = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.startswith(config.output_filename)]
    for video in downloaded:
        v = os.path.join(base_directory, video)
        output_filename = video.split('.')[0]
        command_builder.extract_audio_with_ffmpeg(config.ffmpeg_path, v, output_filename)