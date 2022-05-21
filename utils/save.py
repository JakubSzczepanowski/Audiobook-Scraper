import requests
import utils.progressBar as progressBar

def get_content_length(url: str) -> int:
    r = requests.head(url)
    return int(r.headers['Content-Length'])

def save_file(url: str, filename: str):
    print('Downloading ', filename, '...')
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        fullsize = int(r.headers['Content-Length'])
        size = 1024*1024
        writed = 0
        progress = progressBar.ConsoleProgressBar(fullsize)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=size):
                f.write(chunk)
                writed += size
                progress.printProgressBar(writed)
            print()