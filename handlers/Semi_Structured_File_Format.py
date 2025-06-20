from abc import ABC,abstractmethod
from utils.file_utils import get_file_size,get_file_category,get_ext

class BaseStructureFileHandler(ABC): # This is Abstract Base Class
    def __init__(self,file_path,user_id):
        self.file_path = file_path
        self.user_id = user_id
    
    @abstractmethod
    def process(main):
        pass

class SEMI_STRUCTURE_FILE_FORMAT:
    def __init__(self, file_path, user_id):
        self.file_path = file_path
        self.user_id = user_id
        self.get_ext = get_ext(self.file_path)
    
    def SUB_STRING_TYPE(self):

        handle_mapping = {
            ".json" : DOT_JSON,
            ".xml" : DOT_XML,
            ".yaml" : DOT_YAML,
            ".yml" : DOT_YML,
            ".ini" : DOT_INI,
            ".conf" : DOT_CONF,
            ".properties" : DOT_PROPERTIES,
            ".rdf" : DOT_RDF,
            ".edn" : DOT_EDN
        }

        handle_class = handle_mapping.get(self.get_ext)

        if handle_class:
            handler = handle_class(self.file_path,self.user_id)
            return handler.process()
        else:
            return "Invalid Or Unknown Error"

# The Indication is Like DOT_CSV ------REFERS-----> .csv class
class DOT_JSON(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_XML(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_YAML(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_YML(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_INI(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_CONF(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_PROPERTIES(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_RDF(BaseStructureFileHandler):
    def process(main):
        pass

class DOT_EDN(BaseStructureFileHandler):
    def process(main):
        pass