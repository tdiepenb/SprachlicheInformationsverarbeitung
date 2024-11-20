import re
import string


# reads a file and returns it
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f"An error occurred: {e}")


def calculate_TTR(file):
    text = read_file(file)

    # entfernt ({*}) wo * eine zahl ist
    cleantext = re.sub(r'\(\{\d+\}\)', '', text)

    # fügt leerzeichen vor satzzeichen hinzu um diese als eigene Token zu zählen
    cleantext = re.sub(r'([.,!?;:"\'()])', r' \1 ', cleantext)

    # entfernt doppelte leerzeichen sowie leerzeichen am anfang und am ende
    cleantext = re.sub(r'\s+', ' ', cleantext).strip()

    # aufteilung des textes in einzelne tokens basierend auf leerzeichen und anzahl der tokens
    tokens = cleantext.split()
    numtokens = len(tokens)

    # types im token set und anzahl der types
    types = set(tokens)
    numtypes = len(types)


    type_token_ratio = numtypes / numtokens

    return {
        "Filename:": file,
        "Anzahl Tokens": numtokens,
        "Anzahl Types": numtypes,
        "Type Token Ratio": type_token_ratio
    }


filePathTest = "./data/test.txt"
result = calculate_TTR(filePathTest)
print(result)