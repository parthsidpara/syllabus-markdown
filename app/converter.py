import fitz
import re

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    text = text.replace('–', ':')
    text = text.replace('’', "'")
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    return text

# Filter the extracted text
def filter_text(text):
    start_index = text.find("Module:1")
    end_index = text.find("Total Lecture hours")
    
    if start_index != -1:
        text = text[start_index:end_index] if end_index != -1 else text[start_index:]
    elif end_index != -1:
        text = text[:end_index]

    text = re.sub(r'\b\d+\s*hours\b', '', text)
    return text

def create_markdown_from_syllabus(text):
    markdown_content = "# Syllabus\n\n"
    modules = re.findall(r'Module:\s*(\d+)\s*(.*?)(?=Module:\d+|Total Lecture hours)', text, re.DOTALL)
    
    for module_num, module_content in modules:
        module_parts = module_content.strip().split('\n', 1)
        module_title = re.sub(r'\s*\d+\s*hours?', '', module_parts[0].strip())
        module_body = module_parts[1].strip() if len(module_parts) > 1 else ""
        
        markdown_content += f"## Module {module_num}: {module_title}\n\n"
        
        module_body = re.sub(r'^\s*\d+\s*hours?\s*', '', module_body)
        main_points = re.split(r'\s*(?<![\w-])-(?![\w-])\s*', module_body)
        
        for point in main_points:
            point = point.strip()
            if ':' in point:
                main_point, sub_points = point.split(':', 1)
                markdown_content += f"- [ ] {main_point.strip()}:\n"
                
                sub_points = re.split(r',\s*(?![^()]*\))', sub_points)
                for sub_point in sub_points:
                    sub_point = sub_point.strip()
                    if sub_point:
                        markdown_content += f"  - [ ] {sub_point}\n"
            else:
                markdown_content += f"- [ ] {point}\n"
        
        markdown_content += "\n"
    
    return markdown_content

def save_markdown_to_file(content, file_path):
    with open(file_path, "w") as f:
        f.write(content)
