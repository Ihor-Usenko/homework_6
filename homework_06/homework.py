import sys
from pathlib import Path
import re
from transliterate import translit


CATEGORIES = {"Audio": [".mp3", ".aiff"],
              "Documents": [".docx", ".txt", ".pdf"]}

def normalize(text):
    # Привести текст к нижнему регистру
    text = text.lower()
    
    # Перевести кириллические символы в латиницу
    text = translit(text, 'ru', reversed=True)
    
    # Удалить знаки пунктуации
    text = re.sub(r'[^\w\s]', '', text)
    
    # Удалить лишние пробелы
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def move_file(path: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        #print(f"Make {target_dir}")
        target_dir.mkdir()
    #print(f"Exist {target_dir}")
    path.replace(target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}"))
    print(path)


def get_categories(path: Path) -> str:
    ext = path.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"



def sort_folder(path: Path) -> None:
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