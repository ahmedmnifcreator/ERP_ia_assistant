from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from tqdm import tqdm
RAW_DATA_PATH = Path("data/raw")

def extract_documents(data_path: RAW_DATA_PATH)-> list[Document]:
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

        print(doc.page_content[:600])

        print("\n")

if __name__ == "__main__":
    documents = extract_documents(RAW_DATA_PATH)
    print_statistics(documents)
    preview_documents(documents)
    print(f"\n[OK] Extraction terminee ({len(documents)} pages).")