import sys
from pathlib import Path


def sort_folder(path):
    pass

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