import sys
from pathlib import Path
import re
from transliterate import translit


CATEGORIES = {"Documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
              "Picture": [".jpeg", ".png", ".jpg", ".svg", ".gif"],
              "Musiks": [".mp3", ".aiff", ".avi", ".ogg", ".wav", ".arm"],
              "Video": [".avi", ".mp4", ".mov", ".mkv"],
              "Archives":[".zip", ".gz", ".tar"]}
              

def normalize(text):
 
    
    text = translit(text, 'ru', reversed=True)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def move_file(path: Path, root_dir: Path, categorie: str):
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        target_dir.mkdir()
    path.replace(target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}"))
    print(path)


def get_categories(path: Path) -> str:
    ext = path.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"



def sort_folder(path: Path):
    for item in path.glob("**/*"):
        if item.is_file():
            cat = get_categories(item)
            move_file(item, path, cat)
    

def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
    
    if not path.exists():
        return f"Folder with path {path} dos'n exists."
    
    sort_folder(path)
    
    return "All Ok"
    
if __name__ == "__main__":
    print(main())