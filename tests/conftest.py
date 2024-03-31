import json
import os
import sys

import pytest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def not_enough_dataset():
    with open('tests/fixtures/example_inv.json') as f:
        return json.load(f)


@pytest.fixture
def correct_dataset():
    with open('tests/fixtures/example.json') as f:
        return json.load(f)


@pytest.fixture
def over_dataset():
    with open('tests/fixtures/example_over.json') as f:
        return json.load(f)
