import logging

import pytest

from src.builder import DocumentBuilder


def test_not_enough_dataset(not_enough_dataset):
    builder = DocumentBuilder(not_enough_dataset)
    with pytest.raises(AttributeError) as error:
        builder.build_docx()
    assert error is not None


def test_over_dataset(over_dataset, caplog):
    builder = DocumentBuilder(over_dataset)
    builder.save = lambda doc: None
    with caplog.at_level(logging.INFO):
        builder.build_docx()
    assert "Additional data in the dataset {'additional'}" in caplog.text


def test_valid_dataset(correct_dataset, caplog):
    builder = DocumentBuilder(correct_dataset)
    builder.save = lambda doc: None
    with caplog.at_level(logging.ERROR):
        builder.build_docx()
    assert not caplog.records
