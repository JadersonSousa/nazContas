import subprocess



def frmtText(text):
    palavras = text.split()
    text_format = ""

    for palavra in palavras:
        if len(palavra) == 2:
            palavra = palavra.lower()
        text_format += palavra + " "

    text_format = text_format.strip()
    return text_format


def get_version():
    try:
        output = subprocess.check_output(['git', 'describe', '--tag'])

        result = output.decode('utf-8').strip()
        version = result.rsplit('-', 1)[0]
        return version
    
    except subprocess.CalledProcessError:
        return 'Versão descodificada'