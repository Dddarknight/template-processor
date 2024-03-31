from src.renderer import DocumentRenderer
from src.validator import DocumentValidator


class DocumentProcessorFactory:
    @staticmethod
    def get_renderer(template, context):
        return DocumentRenderer(template=template, context=context)

    @staticmethod
    def get_validator(template_path, dataset):
        return DocumentValidator(template_path=template_path, dataset=dataset)
