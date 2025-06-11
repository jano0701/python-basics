# word_counter.py

def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            print(f"Die Datei '{filename}' enthält {len(words)} Wörter.")
    except FileNotFoundError:
        print(f"Die Datei '{filename}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf
if __name__ == "__main__":
    dateiname = "seminararbeit.txt"  # Ersetze mit deinem Dateinamen
    count_words_in_file(dateiname)
