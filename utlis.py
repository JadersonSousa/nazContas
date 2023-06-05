



def frmtText(text):
    palavras = text.split()
    text_format = ""

    for palavra in palavras:
        if len(palavra) == 2:
            palavra = palavra.lower()
        text_format += palavra + " "

    text_format = text_format.strip()
    return text_format

