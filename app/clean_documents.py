import re 
from copy import deepcopy
# pyrefly: ignore [missing-import]
from langchain_core.documents import Document

def clean_text(text:str)->str:
  """
  Nettoie le texte extrait des PDF.
  """
  # Supprimer les tabulations
  text = text.replace("\t", " ")
  # Supprimer les retours chariot Windows
  text = text.replace("\r", " ")
  # Supprimer les caractères invisibles
  text = text.replace("\x00", " ")
  text = text.replace("\x01", " ")
  text = text.replace("\x02", " ")
  text = text.replace("\x03", " ")
  text = text.replace("\x04", " ")
  text = text.replace("\x05", " ")
  text = text.replace("\x06", " ")
  text = text.replace("\x07", " ")
  text = text.replace("\x08", " ")
  text = text.replace("\x09", " ")
  text = text.replace("\x0a", " ")
  text = text.replace("\x0b", " ")
  text = text.replace("\x0c", " ")
  text = text.replace("\x0d", " ")
  text = text.replace("\x0e", " ")
  text = text.replace("\x0f", " ")
  text = text.replace("\x10", " ")
  text = text.replace("\x11", " ")
  text = text.replace("\x12", " ")
  text = text.replace("\x13", " ")
  text = text.replace("\x14", " ")
  text = text.replace("\x15", " ")
  text = text.replace("\x16", " ")
  text = text.replace("\x17", " ")
  text = text.replace("\x18", " ")
  text = text.replace("\x19", " ")
  text = text.replace("\x1a", " ")
  text = text.replace("\x1b", " ")
  text = text.replace("\x1c", " ")
  text = text.replace("\x1d", " ")
  text = text.replace("\x1e", " ")
  text = text.replace("\x1f", " ")
  text = text.replace("\x7f", " ")
  # Supprimer les numéros de page
  text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)
  # Supprimer les numéros seuls
  text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)
  # Supprimer les URLs
  text = re.sub(r"https?://\S+", "", text)
  text = re.sub(r"www\.\S+", "", text)
  # Supprimer les e-mails
  text = re.sub(r"\S+@\S+", "", text)
  # Supprimer les caractères spéciaux inutiles
  text = re.sub(r"[©®™]", "", text)
  # Réduire plusieurs espaces
  text = re.sub(r"[ ]{2,}", " ", text)
  # Réduire plusieurs lignes vides
  text = re.sub(r"\n{3,}", "\n\n", text)
  return text.strip()


def clean_documents(documents:list[Document])->list[Document]:
    """
    Nettoie tous les documents de langchain.
    """
    cleaned_documents = []
    for doc in documents:
        cleaned_doc = deepcopy(doc)
        cleaned_doc.page_content = clean_text(cleaned_doc.page_content)
        cleaned_documents.append(cleaned_doc)
    return cleaned_documents
# Baad lnhotoh namlolo l appel fll extract_document.py