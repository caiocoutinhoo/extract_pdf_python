import fitz  # PyMuPDF
import re


def extract_text_from_pdf(pdf_path):
    # Abrir o documento PDF
    document = fitz.open(pdf_path)
    
    # Extração de texto de todas as páginas
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
    
    return text


def organize_resume_text(text):
    # Dicionário para armazenar as seções organizadas
    sections = {
        "Resumo Profissional": "",
        "Habilidades": "",
        "Qualificações": "",
        "Experiência": "",
        "Educação": "",
        "Histórico de Trabalho": ""
    }

    # Definir padrões para cada seção
    patterns = {
        "Resumo Profissional": r"Professional Summary(.*?)(?=\nSkills|\nCore Qualifications|\nExperience|\nEducation|\nWork History|\n$)",
        "Habilidades": r"Skills(.*?)(?=\nCore Qualifications|\nExperience|\nEducation|\nWork History|\n$)",
        "Qualificações": r"Core Qualifications(.*?)(?=\nExperience|\nEducation|\nWork History|\n$)",
        "Experiência": r"Experience(.*?)(?=\nEducation|\nWork History|\n$)",
        "Educação": r"Education(.*?)(?=\nWork History|\n$)",
        "Histórico de Trabalho": r"Work History(.*?)(?=$)"
    }

    # Extrair cada seção usando regex
    for section, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            sections[section] = match.group(1).strip()

    return sections

pdf = extract_text_from_pdf("cv.pdf")

pdf = organize_resume_text(pdf)

for section, content in pdf.items():
        print(f"{section}:\n{content}\n{'-'*40}")