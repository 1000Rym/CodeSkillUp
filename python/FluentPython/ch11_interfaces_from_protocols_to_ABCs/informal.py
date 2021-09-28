#Informal Interface
class InformalParserInterface:
    def load_data_source(self, path: str, file: str) -> str:
        """Load in file for extracting text."""
        pass

    def extract_text(self, full_file_name : str) -> dict:
        """Extract text from  the currently loaded file."""
        pass

# concrete implementation1
class PdfParser(InformalParserInterface):
    """Extract Text From PDF"""
    def load_data_source(self, path: str, file_name:str )-> str:
        """Overrides InformalParserInterface.load_data_source"""
        pass

    def extract_text(self, full_path:str)->dict:
        """Overrieds InformalParserInterface.extract_text"""
        pass

# concrete implementation2
class EmlParser(InformalParserInterface):
    """Extract Text From emal"""
    def load_data_source(self, path: str, file_name:str )-> str:
        """Overrides InformalParserInterface.load_data_source"""
        pass

    def extract_text(self, full_path:str)->dict:
        """Overrieds InformalParserInterface.extract_text"""
        pass

if __name__ == "__main__":
    print(f"Is subclass: {issubclass(PdfParser, InformalParserInterface)}")
    print(f"check mro:{EmlParser.__mro__}")



    