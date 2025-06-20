from abc import ABC, abstractmethod
from utils.file_utils import get_file_size,get_file_category,get_ext,file_name,dob,file_permission,file_author,dimension_file,get_duration,get_page_count,get_tags_labels

class BaseStructureFileHandler(ABC):
    def __init__(self,file_path,user_id):
        self.file_path = file_path
        self.user_id = user_id
    @abstractmethod
    def process(self):
        pass

class STRUCTURED_FILE_FORMAT:
    def __init__(self,file_path, user_id):
        self.file_path = file_path
        self.user_id = user_id
        self.get_ext = get_ext(self.file_path)

    def SUB_STRUCTURE_TYPE(self):
        # Mapping Extension to Handle Class
        handle_mapping = {
            ".csv" : DOT_CSV,
            ".tsv" : DOT_TSV,
            ".xls" : DOT_XLS,
            ".xlsx" : DOT_XLSX,
            ".db" : DOT_DB,
            ".sql" : DOT_SQL,
            ".parquet" : DOT_PARQUET,
            ".avro" : DOT_AVRO,
            ".orc" : DOT_ORC,
            ".mdb" : DOT_MDB,
            ".sas7bdat" : DOT_SAS7BDAT,
            ".sav" : DOT_SAV
        }
        
        handler_class = handle_mapping.get(self.get_ext)

        if handler_class:
            handler = handler_class(self.file_path,self.user_id)
            return handler
        else:
            return "Invalid or Unknown Error"
        
# The Indication is Like DOT_CSV ------REFERS-----> .csv class
class DOT_CSV(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
    def special_prop(self):
        return{

            # Data Structure Properties
            "Presence of Header Row" : {},
            "Number of Rows" : {},
            "Number of Columns" : {},
            "Column Names" : {},
            "Column Order" : {},
            "Delimiter (Comma, semicolon, tab etc.)" : {},
            "Encoding (UTF-8. ASCII, etc)" : {},
            "Multiple Header Rows" : {},
            "Consistent Row Length (Same Number of Column Per Row)" : {},

            # Column-wise Propertiess
            "Data Type Per Column" : {},
            "Unique Values in Each Column" : {},
            "Number and Percentage of Null / Missing Values" : {},
            "Duplicate Row Presence" : {},
            "Duplicate Value in Unique Identified Column" : {},
            "Common Categories in Categorical Columns" : {},
            "Date Format Consistency in Date / Time Columns" : {},
            "Presence of Special Characters or Outliners" : {},
            "Non-standardized Categorical Values (e.g: 'Male','male','M')" : {},

            # Statistical Properties (Numerical Summary)
            "Minimum Value" : {},
            "Maxmium Value" : {},
            "Mean (Average)" : {},
            "Median" : {},
            "Mode" : {},
            "Standard Deviation" : {},
            "Variance" : {},
            "Skewness" : {},
            "Kurtosis" : {},
            "Distribution" : {},
            "Outliers (IQR or z-score)" : {},

            # Relationship Properties (Inter-Column Relationships)
            "Correlation Between Numeric Columns" : {},
            "Covariance Between Numeric Columns" : {},
            "Dependency/Association Between Categorical Variable (Chi-square, Cramer's V)" : {},
            "Multicollinearity (Variance Inflation Factor VIF)" : {},

            # Data Quality & Integrity Checks
            "Missing Value Patterns (MCAR, MAR, MNAR)" : {},
            "Invalid Values (e.g., negative ages, future dates)" : {},
            "Unexpected Data Types" : {},
            "Business Logic Checks (e.g., Salary Should Not be Gegative)" : {},
            "Special Character and Encoding Issues" : {},
            "Null or Empty Text Fields" : {},
            "Data Consistency (e.g., start date before end date)" : {},

            # Metadata & Source Information
            "Source of the Data (trusted/untrusted)" : {},
            "Date of Data Collection" : {},
            "Frequency of Data Collection(daily,Monthly,etc)" : {},
            "Data Version or Timestamp" : {},
            "Documention Avalibility" : {},
            "Data Ownership and Privacy Constraints (GDRP, PII)" : {},

            # Time-Series Data Properties
            "Timestamp Granularity (Seconds, Minutes, Day)" : {},
            "Gaps or Misssing Period in Time" : {},
            "Time Zone Consistency" : {},
            "Seasonality or Trend Presence" : {},

            # Text / NLP Data Properties
            "Average Text Length" : {},
            "Stopwords Presence" : {},
            "Special Characters, emojis, URL in Text" : {},
            "Language Detection" : {},
            "Words Frequency Distribution" : {},

            # Security & Privacy Checks
            "Presence of Personally Identifiable Information (PII)" : {},
            "Sensitive Data Columns (e.g., salary, Mediacl Records)" : {},
            "Anonymization or Masking Status" : {},

            # Automation & ETL Readliness (for ingestion pipelines)
            "File Format Consistency" : {},
            "File Compression Check" : {},
            "Delimiter or Escape Character Issues" : {},
            "Encoding Error Detection" : {},
            "Data Ingestion Readlinees (Schema Validation, etc)" : {}
        }
class DOT_TSV(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_XLS(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_XLSX(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_DB(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_SQL(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }

class DOT_PARQUET(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_AVRO(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_ORC(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_MDB(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_SAS7BDAT(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    
class DOT_SAV(BaseStructureFileHandler):
    def process(self):
        return "Process"
    
    def basic_props(self):
        return {
            "File Name" : file_name(self.file_path),
            "File Size" : get_file_size(self.file_path),
            "Date Created / Modified / Accessed" : dob(self.file_path),
            "File Type" : get_ext(self.file_path), # File Format
            "Permission" : file_permission(self.file_path),
            "Author" : file_author(self.file_path),
            "Dimensions" : dimension_file(self.file_path),
            "Duration" : get_duration(self.file_path),
            "Pages" : get_page_count(self.file_path),
            "Tags / Lables" : get_tags_labels(self.file_path)
        }
    