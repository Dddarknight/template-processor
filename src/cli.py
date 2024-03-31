import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Builds docx-file from templates.')
    parser.add_argument('context')
    return parser.parse_args()
