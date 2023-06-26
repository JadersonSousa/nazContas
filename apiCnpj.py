import requests

def dadosEmpresa(cnpj):
        try:
                        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
                        headers = {"Accept": "application/json"}

                        response = requests.get(url, headers=headers)

                        dados = response.json()
                        lista = [
                                dados['cnpj'], 
                                dados['nome'], 
                                dados['fantasia'], 
                                dados['atividade_principal'][0]['text'], 
                                dados['bairro'], 
                                dados['logradouro'],
                                dados['numero'],
                                dados['cep'],
                                dados['municipio'],
                                dados['uf']
                                ]
                        return lista
        except:
                        erros = response.json()
                        erro = erros['message']
                        return f"{erro}"