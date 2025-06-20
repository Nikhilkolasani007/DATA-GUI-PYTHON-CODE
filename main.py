import os #Python Module
from utils.file_utils import get_file_size,get_file_category,file_exists
from handlers.Structured_FIle_Format import STRUCTURED_FILE_FORMAT
from handlers.Un_Structured_FIle_Format import UN_STRUCTURE_FILE_FORMAT
from handlers.Semi_Structured_File_Format import SEMI_STRUCTURE_FILE_FORMAT
# from handlers.Structured_FIle_Format import 

class StructureType:
    def __init__(self, file_path, user_id):
        self.file_path = file_path
        self.user_id = user_id
        self.file_category = get_file_category(self.file_path)
        self.file_size = get_file_size(self.file_path)
        self.file_exist = file_exists(self.file_path)
    
    def STRUCTURE_TYPE(self):
        if self.file_path:
            if self.file_category == "Structured File Format":
                structured_handle = STRUCTURED_FILE_FORMAT(self.file_path, self.user_id)
                handler = structured_handle.SUB_STRUCTURE_TYPE()
                print(handler.basic_props())
            elif self.file_category == "Unstructured File Format":
                unstructured_handle = UN_STRUCTURE_FILE_FORMAT(self.file_path, self.user_id)
                handler = structured_handle.SUB_STRUCTURE_TYPE()
                print(handler.process())
            elif self.file_category == "Semi-Structured File Format":
                semistructure_handle = SEMI_STRUCTURE_FILE_FORMAT(self.file_path,self.user_id)
                handler = structured_handle.SUB_STRUCTURE_TYPE()
                print(handler.process())
        else:
            return "Unknown Error With this File"

# Example usage
fd = StructureType(r"CSV\customers-100.csv", '00000')
fd.STRUCTURE_TYPE()

