class ParserMeta(type):
    """A parser metaclass taht will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    
    def __subclasscheck__(cls, subclass):
        """The class method should be listed in attributes, and callable."""
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    pass

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str: 
        """Overrides UpdatedInformalParserInterface """
        pass

    def extract_text(self, full_path:str)->dict:
        """Overrides UPdatedInformalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str: 
        """Overrides UpdatedInformalParserInterface """
        pass

    def extract_text_from_emal(self, full_path:str)->dict:
        """Email Only Parser"""
        pass

if __name__ == '__main__':
    print(issubclass(PdfParserNew, UpdatedInformalParserInterface))
    print(issubclass(EmlParserNew, UpdatedInformalParserInterface))
    print(PdfParserNew.__mro__)





    