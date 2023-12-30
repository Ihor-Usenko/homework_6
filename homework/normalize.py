import re
from transliterate import translit

text = 'Повертає всі @& %% ^ _+nнеперекриваючі збіги шаблону в рядку у вигляді списку\
        рядків або кортежів. Рядок сканується зліва направо, і збіги\
        п.овертаються в пор,ядку знайдення. Пор56ожні збіги включаються в результат\
        .'

def normalize(text):
    # Привести текст к нижнему регистру
    #text = text.lower()
    
    # Перевести кириллические символы в латиницу
    text = translit(text, 'ru', reversed=True)
    
    # Удалить знаки пунктуации
    text = re.sub(r'[^\w\s]', '_', text)
    
    #Удалить лишние пробелы
    text = re.sub(r'\s+', ' ', text)#.strip()
    
    return text

print(normalize(text))