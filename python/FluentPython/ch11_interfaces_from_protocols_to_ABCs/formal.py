import abc

class FormalParserInterface(metaclass = abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path:str):
        """Extract text from the data set"""
        raise NotImplementedError



class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str: 
        """Overrides UpdatedInformalParserInterface """
        pass

    def extract_text(self, full_path:str)->dict:
        """Overrides UPdatedInformalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str: 
        """Overrides UpdatedInformalParserInterface """
        pass

    def extract_text_from_emal(self, full_path:str)->dict:
        """Email Only Parser"""
        pass

if __name__ == '__main__':
    print(issubclass(PdfParserNew, FormalParserInterface))
    print(issubclass(EmlParserNew, FormalParserInterface))
    print(PdfParserNew.__mro__)
    pdf_parser = PdfParserNew()
    eml_Parser = EmlParserNew()
