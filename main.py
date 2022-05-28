from utils.bot import ChromeBot
from utils.config import load_requirements
import utils.save as save
import os
import pathlib
import utils.command_builder as command_builder
import cli

MAIN_PATH = pathlib.Path().resolve()

def main():
    try:
        config = load_requirements(os.path.join(MAIN_PATH, 'requirements.json'))
    except TypeError as e:
        print(e)
        return
    args = cli.get_args()
    bot = ChromeBot(config.chrome_driver_path)
    filename_prefix = config.output_filename
    for index, link in enumerate(config.video_links):
        src = bot.get_video_src(link)
        save.save_file(src, f'{filename_prefix} Rozdział {index+1+args.offset}.mp4')
    mypath = os.path.curdir
    downloaded = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.startswith(config.output_filename)]
    for video in downloaded:
        v = os.path.join(MAIN_PATH, video)
        output_filename = video.split('.')[0]
        command_builder.extract_audio_with_ffmpeg(config.ffmpeg_path, v, output_filename)
    bot.close()
    

if __name__ == '__main__':
    try:
        assert os.path.isfile('requirements.json')
        main()
    except AssertionError:
        print('requirements.json is not exists!')