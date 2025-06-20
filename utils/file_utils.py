import os
import time
import os
from PIL import Image
import cv2
from PyPDF2 import PdfReader
from PIL.ExifTags import TAGS
def get_file_size(file_path):
    try:
        file_size = os.path.getsize(file_path)
        if file_size < 1024:
            return f'{file_size} Bytes'
        elif file_size < 1024 * 1024:
            return f'{file_size / 1024:.2f} KB'
        elif file_size < 1024 * 1024 * 1024:
            return f'{file_size / (1024 * 1024):.2f} MB'
        else:
            return f'{file_size / (1024 * 1024 * 1024):.2f} GB'
    except FileNotFoundError as file_not_found:
        return "Invalid"

def get_file_category(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    structured_file_formats = {".csv", ".tsv", ".xls", ".xlsx", ".db", ".sql", ".parquet", ".avro", ".orc", ".mdb", ".sas7bdat", ".sav"}
    unstructured_file_formats = {".txt", ".pdf", ".doc", ".docx", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".mp3", ".wav", ".mp4", ".avi", ".mov", ".flv", ".mkv", ".html", ".htm", ".log", ".eml", ".zip", ".rar"}
    semi_structured_formats = {".json", ".xml", ".yaml", ".yml", ".ini", ".conf", ".properties", ".rdf", ".edn"}

    if file_extension in structured_file_formats:
        return "Structured File Format"
    elif file_extension in unstructured_file_formats:
        return "Unstructured File Format"
    elif file_extension in semi_structured_formats:
        return "Semi-Structured File Format"
    else:
        return "Invalid File Format"
    
def file_exists(file_path):
    return os.path.isfile(file_path)

def get_ext(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    return file_extension

def file_name(file_path):
    path = os.path.basename(file_path)
    return path

# Date Created / Modified / Accessed

def dob(file_path):
    ti_c = os.path.getctime(file_path)
    c_ti = time.ctime(ti_c)
    return c_ti

def file_permission(file_path):
    return "Unknown"

def file_author(file_path):
    return "Unknown"

def dimension_file(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            img = Image.open(file_path)
            wid, hgt = img.size
            return f"{wid}x{hgt}"

        elif ext in ['.mp4', '.avi', '.mkv', '.mov']:
            video = cv2.VideoCapture(file_path)
            if not video.isOpened():
                return "Unable to open video file"
            width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            video.release()
            return f"{width}x{height}"

        else:
            return "Invalid file type"

    except Exception as e:
        return f"Error occurred: {e}"
    
def get_duration(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext in ['.mp4', '.avi', '.mkv', '.mov']:
            video = cv2.VideoCapture(file_path)
            if not video.isOpened():
                return "Unable to open video file"

            fps = video.get(cv2.CAP_PROP_FPS)
            frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
            duration = frame_count / fps if fps else 0

            video.release()

            # Return as formatted mm:ss string
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            return f"{minutes}m {seconds}s"

        else:
            return "Not a video file"

    except Exception as e:
        return f"Error: {e}"
    
def get_page_count(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext == '.pdf':
            reader = PdfReader(file_path)
            page_count = len(reader.pages)
            return page_count

        else:
            return "Not a PDF file"

    except Exception as e:
        return f"Error: {e}"
    
def get_tags_labels(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext in ['.jpg', '.jpeg', '.png', '.tiff']:
            image = Image.open(file_path)
            exif_data = image.getexif()

            if not exif_data:
                return "No metadata found"

            tags = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                tags[tag] = value

            return tags

        else:
            return "Not an image file"

    except Exception as e:
        return f"Error: {e}"