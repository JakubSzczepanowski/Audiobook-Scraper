import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Set video's queue offset or specify tasks to do")
    parser.add_argument('--offset', metavar='N', type=int,
                        help='set offset value', default=0)
    parser.add_argument('--extract_only', '-e', action='store_true', help="extract videos with config's prefix to audio only (without downloading)")
    parser.add_argument('--download_only', '-d', action='store_true', help="download videos without extracting them to audio")

    return parser.parse_args()