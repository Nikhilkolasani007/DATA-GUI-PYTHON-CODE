from abc import ABC,abstractmethod
from utils.file_utils import get_file_size,get_file_category,get_ext

class BaseStructureFileHandler(ABC): #This is Called as Abstract Base Class
    def __init__(self,file_path,user_id):
        self.file_path = file_path
        self.user_id = user_id
    
    @abstractmethod
    def process(main):
        pass

class UN_STRUCTURE_FILE_FORMAT:
    def __init__(self, file_path, user_id):
        self.file_path = file_path
        self.user_id = user_id
        self.get_ext = get_ext(self.file_path)

    def SUB_STRING_TYPE(self):

        handle_mapping = {
            ".txt" : DOT_TXT,
            ".pdf" : DOT_PDF,
            ".doc" : DOT_DOC,
            ".docx" : DOT_DOCX,
            ".jpg" : DOT_JPG,
            ".jpeg" : DOT_JPEG,
            ".png" : DOT_PNG,
            ".gif" : DOT_GIF,
            ".bmp" : DOT_BMP,
            ".tiff" : DOT_TIFF,
            ".mp3" : DOT_MP3,
            ".wav" : DOT_WAV,
            ".mp4" : DOT_MP4,
            ".avi" : DOT_AVI,
            ".mov" : DOT_MOV,
            ".flv" : DOT_FLV,
            ".mkv" : DOT_MKV,
            ".html" : DOT_HTML,
            ".htm" : DOT_HTM,
            ".log" : DOT_LOG,
            ".eml" : DOT_EML,
            ".zip" : DOT_ZIP,
            ".rar" : DOT_RAR
        } 

        handle_class = handle_mapping.get(self.get_ext)

        if handle_class:
            handler = handle_class(self.file_path,self.user_id)
            return handler.process()
        else:
            return "Invalid or Unknown Error"
# The Indication is Like DOT_CSV ------REFERS-----> .csv class
class DOT_TXT(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_PDF(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_DOC(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_DOCX(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_JPG(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_JPEG(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_PNG(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_GIF(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_BMP(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_TIFF(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_MP3(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_WAV(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_MP4(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_AVI(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_MOV(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_FLV(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_MKV(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_HTML(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_HTM(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_LOG(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_EML(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_ZIP(BaseStructureFileHandler):
    def process(self):
        pass

class DOT_RAR(BaseStructureFileHandler):
    def process(self):
        pass