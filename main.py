from utils.config import load_requirements
import os
import pathlib
import cli
from utils.func import download_files, extract_videos_to_audios

MAIN_PATH = pathlib.Path().resolve()

def main():
    try:
        config = load_requirements(os.path.join(MAIN_PATH, 'requirements.json'))
    except TypeError as e:
        print(e)
        return
    args = cli.get_args()
    tasks = [lambda: download_files(config, args.offset), lambda: extract_videos_to_audios(MAIN_PATH, config)]

    if args.download_only:
        tasks.pop(1)

    if args.extract_only:
        tasks.pop(0)
    
    for task in tasks:
        task()

if __name__ == '__main__':
    try:
        assert os.path.isfile('requirements.json')
        main()
    except AssertionError:
        print('requirements.json is not exists!')