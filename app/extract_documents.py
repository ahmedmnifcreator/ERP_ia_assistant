import sys
import json
from clean_documents import clean_documents
from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from tqdm import tqdm

def safe_print(text: str):
    """Print text safely on Windows consoles with limited encoding (e.g. cp1252)."""
    enc = sys.stdout.encoding or "utf-8"
    print(text.encode(enc, errors="replace").decode(enc))


PROCESSED_DATA_PATH = Path("data/processed")
RAW_DATA_PATH = Path("data/raw")

def save_documents(documents: list[Document], output_path: Path = PROCESSED_DATA_PATH / "documents.json"):
    """
    Sauvegarde les documents nettoyés dans un fichier JSON.
    Chaque document est sauvegardé avec son contenu et ses métadonnées.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data = [
        {"page_content": doc.page_content, "metadata": doc.metadata}
        for doc in documents
    ]
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n[SAVE] {len(documents)} documents sauvegardes dans : {output_path}")


def extract_documents(data_path: Path = RAW_DATA_PATH) -> list[Document]:
    """
    Parcourt tous les PDF présents dans data/raw/,
    extrait leur contenu et retourne une liste de Documents LangChain.
    """
    documents =[]
    pdf_files= list(data_path.rglob("*.pdf"))
    if not pdf_files:
        print("Aucun fichier PDF trouve.")
        return documents
    print(f"[PDF] Nombre de PDF trouves : {len(pdf_files)}")
    for pdf_path in tqdm(pdf_files, desc="Extraction des PDF"):
     try:
      reader = PdfReader(str(pdf_path))
      # categorie = premier dossier apres data/raw/
      category = pdf_path.relative_to(data_path).parts[0]
      for page_num, page in enumerate(reader.pages):
       text = page.extract_text() or ""
       doc = Document(
        page_content=text,
        metadata={
         "category": category,
         "filename": pdf_path.name,
         "filepath": str(pdf_path),
         "page": page_num,
        }
       )
       documents.append(doc)
     except Exception as e:
      print(f"\n[ERREUR] Echec de l'extraction de {pdf_path}:")
      print(e)
    return documents

def print_statistics(documents:list[Document]):
  """
  Affiche des statistiques sur les documents extraits
  """
  print("\n=== STATISTIQUES ===")
  print(f"Nombre total de pages : {len(documents)}")
  categories = {}
  for doc in documents:
    category = doc.metadata ["category"]
    categories[category] = categories.get(category, 0) + 1
  print("\nPages par catégorie :\n")  
  for category, count in categories.items():
        print(f"{category:<20} {count}")

def preview_documents(documents: list[Document], n: int = 3):
    """
    Affiche un aperçu des premiers documents.
    """

    print("\nAPERÇU DES DOCUMENTS\n")

    for i, doc in enumerate(documents[:n]):

        print(f"Document {i+1}")
        print("Métadonnées :")
        print(doc.metadata)

        print("\nTexte :\n")

        safe_print(doc.page_content[:600])

        print("\n")

if __name__ == "__main__":
    documents = extract_documents(RAW_DATA_PATH)
    documents = clean_documents(documents)
    save_documents(documents)
    print_statistics(documents)
    preview_documents(documents)
    print(f"\n[OK] Extraction terminee ({len(documents)} pages).")

