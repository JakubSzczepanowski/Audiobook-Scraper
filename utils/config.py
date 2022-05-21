from dataclasses import dataclass
import json

@dataclass
class ConfigData:
    chrome_driver_path: str
    ffmpeg_path: str
    video_links: list[str]
    output_filename: str

def load_requirements(path: str) -> ConfigData:
    with open(path, 'r', encoding='utf-8') as f:
        r = f.read()
    config = json.loads(r, object_hook=lambda d: ConfigData(**d))
    return config