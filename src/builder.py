import json
import logging
import os

from docx import Document

from src.factory import DocumentProcessorFactory


class DocumentBuilder:
    def __init__(
        self,
        dataset: dict,
        factory: DocumentProcessorFactory = DocumentProcessorFactory,
    ):
        self.ordering = self.get_ordering()
        self.order_numbers = sorted(self.ordering.keys())
        self.dataset = dataset
        self.result_name = "generated_doc.docx"
        self.factory = factory
        self.templates_path = 'src/templates'

    def get_ordering(self):
        with open('src/ordering.json') as f:
            ordering_data = json.load(f)
        return {value: key for key, value in ordering_data.items()}

    def build_docx(self):
        combined_document = Document()
        combined_variables = set()
        for number in self.order_numbers:
            template = os.path.join(self.templates_path, self.ordering[number])
            validator = self.factory.get_validator(template_path=template, dataset=self.dataset)
            variables = validator.process()
            combined_variables.update(variables)
            renderer = self.factory.get_renderer(template=template, context=self.dataset)
            with renderer.render() as temp_doc:
                for element in temp_doc.element.body:
                    combined_document.element.body.append(element)

        self.save(combined_document)
        difference = set(self.dataset.keys()) - combined_variables
        if difference:
            logging.info(f'Additional data in the dataset {str(difference)}')

    def save(self, document):
        document.save(self.result_name)
