import os
import tempfile
from contextlib import contextmanager

from docx import Document
from docxtpl import DocxTemplate

from src.base import AbstractRenderer


class TemporaryDocument:
    def __enter__(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
        return self.temp_file.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.temp_file.close()
        os.remove(self.temp_file.name)


class DocumentRenderer(AbstractRenderer):
    def __init__(self, *, template, context):
        self.template = template
        self.context = context

    @contextmanager
    def render(self):
        doc = DocxTemplate(self.template)
        doc.render(self.context)
        with TemporaryDocument() as temp_path:
            doc.save(temp_path)
            yield Document(temp_path)
