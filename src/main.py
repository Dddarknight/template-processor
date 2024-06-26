import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.builder import DocumentBuilder
from src.cli import parse
from src.logger import setup_logging


def get_dataset():
    args = parse()
    with open(args.context) as f:
        return json.load(f)


def main():
    setup_logging()
    dataset = get_dataset()
    builder = DocumentBuilder(dataset)
    builder.build_docx()


if __name__ == '__main__':
    main()
