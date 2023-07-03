import sqlite3



db = 'dbContas.db'

try:
    connect = sqlite3.connect(db)
    if connect:
        print('Sucesso ao conectar ao db')
    
except sqlite3.Error as erros:
    print('Erro ao conectar ao db', erros)


def versionSys(version, hshVersion):
    try:

        with connect:
            cursor = connect.cursor()
            
            cursor.execute(f"SELECT 1 FROM tbSys WHERE version= ?", [version])
            existe = cursor.fetchone()
            
            if not existe:
                sql = "INSERT INTO tbSys (version, hashVersion) VALUES(?,?)"
                cursor.execute(sql, (version, hshVersion))
                connect.commit()

    except sqlite3.Error as erro:
        print(f'Erro aqui na versionSys: {erro}')
    finally:
        cursor.close()

def versaoAtual():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT version FROM tbSys ORDER BY id DESC LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            
            return result[0]
                    
    except sqlite3.Error as erros:
        print("Error ao buscar informações no banco", erros)

    finally:
        cursor.close()




def unidadesNegocios():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT unidade FROM tbUnidade"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            list_unds = [item for tupla in result for item in tupla]

            return list_unds
                    
    except sqlite3.Error as erros:
        print("Error ao buscar informações no banco", erros)

    finally:
        cursor.close()




# CADASTRO DE EMPRESA
def cadastroUnidade(unidade, razaoSocial, cnpj, cidade, uf):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "INSERT INTO tbUnidade (unidade, razaoSocial, cnpj, cidade, uf) VALUES(?,?,?,?,?)"
            
            cursor.execute(sql, (unidade, razaoSocial, cnpj, cidade, uf))
            codUnidade = cursor.lastrowid
            result = {'data': codUnidade}

            connect.commit()
            
            return result
    except sqlite3.Error as erros:
        
        mensagem = str(erros)

        if 'UNIQUE constraint failed' in mensagem:
            mensagem = "Erro de duplicidade ja existe unidade cadastrada com esssas credenciais"
        elif "NOT NULL constraint falied" in mensagem:
            mensagem = "Os valores não podem ser vazios"
        err = {'error': mensagem}
        return err
    
    finally:
        cursor.close()
# FIM cadastroUnidade

# MOSTRANDO DADOS DAS UNIDADES
def mostrarUnidades():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM tbUnidade"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
                    
    except sqlite3.Error as erros:
        print("Error ao buscar informações no banco: mostrarUnidades", erros)

    finally:
        cursor.close()
# FIM mostrarUnidades

# CADASTRANDO OS TIPOS DE SERVIÇOS
def cadTipoServico(tipoServico):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "INSERT INTO tbTipoServ (servicoTipo) VALUES (?)"
            cursor.execute(sql, [tipoServico])
            
            codServico = cursor.lastrowid
            result = {'data': codServico}

            connect.commit()
            
            return result
    except sqlite3.Error as erros:
        
        mensagem = str(erros)

        if 'UNIQUE constraint failed' in mensagem:
            mensagem = "Erro de duplicidade esse serviço ja esta cadastrado!!!"
        elif "NOT NULL constraint falied" in mensagem:
            mensagem = "Os valores não podem ser vazios"
        err = {'error': mensagem}
        return err
    finally:
        cursor.close()    
# FIM cadTipoServico


# MOSTRAR DADOS DOS SERVIÇOS
def vwServicos(limit, offset):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * from vwServicos LIMIT {} OFFSET {}".format(limit, offset)

            cursor.execute(sql)
            result = cursor.fetchall()

            return result
                    
    except sqlite3.Error as erros:
        print("Error ao buscar informações no banco: vwServicos", erros)

    finally:
        cursor.close()

def vw_TotalServicos():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT COUNT(*) from vwServicos"

            cursor.execute(sql)
            result = cursor.fetchone()

            return result
                    
    except sqlite3.Error as erros:
        print("Error ao buscar informações no banco: vwServicos", erros)

    finally:
        cursor.close()
# FIM vwServicos

def vwHomeInf():
    try:
        with connect:
            cursor = connect.cursor()
            sql = f"""SELECT (SELECT count(*) FROM tbServico) as 'contagem_servicos',
                             (SELECT count(*) FROM tbUnidade) as 'contagem_unidades',
                             (SELECT count(*) FROM tbFornecedor) as 'contagem_fornecedors'"""

            cursor.execute(sql)
            result = cursor.fetchall()
            
            return [item for tupla in result for item in tupla]

    except sqlite3.Error as erro:
        print(f"Houve um erro aqui na vwHomeInf => {erro}")
    
    finally:
        cursor.close()

# CADASTRO DE FORNECEDORES
def cadFornecedor(cnpj, nome, fantasia, tipoAtv, bairro, logradouro, num, cep, municipio, uf):
    try:
        with connect:
            cursor = connect.cursor()
            sql = """INSERT INTO tbFornecedores 
                                        (cnpjFonecedor,
                                        nomeFornecedor,
                                        nomeFantasia,
                                        atividadePrincipal,
                                        bairro,
                                        logradouro,
                                        numero,
                                        cep,
                                        municipio,
                                        uf ) VALUES(?,?,?,?,?,?,?,?,?,?)"""
            
            cursor.execute(sql, (cnpj, nome, fantasia, tipoAtv, bairro, logradouro, num, cep, municipio, uf))
            codUnidade = cursor.lastrowid
            result = {'data': codUnidade}

            connect.commit()
            
            return result
    except sqlite3.Error as erros:
        
        mensagem = str(erros)

        if 'UNIQUE constraint failed' in mensagem:
            mensagem = "Erro de duplicidade ja existe unidade cadastrada com esssas credenciais"
        elif "NOT NULL constraint falied" in mensagem:
            mensagem = "Os valores não podem ser vazios"
        err = {'error': mensagem}
        return err
    
    finally:
        cursor.close()
# FIM cadFornecedor

# CADASTRO DE SERVICO
def cad_Servico(emp, frn, tpSrv, crc, dtVenc):
    try:
        with connect:
            cursor = connect.cursor()
            sql = """INSERT INTO tbServico 
                                        ( codEmpresa, codForn, tipoServico, circuito, diaVencimento ) VALUES(?,?,?,?,?)"""
            
            cursor.execute(sql, (emp, frn, tpSrv, crc, dtVenc))
            codServ = cursor.lastrowid
            result = {'data': codServ}

            connect.commit()
            
            return result
    except sqlite3.Error as erros:
        
        mensagem = str(erros)

        if 'UNIQUE constraint failed' in mensagem:
            mensagem = "Erro de duplicidade ja existe serviço cadastrado com esssas credenciais"
        elif "NOT NULL constraint falied" in mensagem:
            mensagem = "Os valores não podem ser vazios"
        err = {'error': mensagem}
        return err
    
    finally:
        cursor.close()
# FIM cadServico  



# MOSTRANDO DADOS UNIDADE PARA TAB_CAD
def mostrarUnidades_CadServ():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT idEmpresa, cnpj, unidade, cidade, uf FROM tbUnidade"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
                    
    except sqlite3.Error as erros:
        print("Error ao buscar informações no banco: mostrarUnidades", erros)

    finally:
        cursor.close()
# FIM mostrarUnidades_CadServ

# MOSTRANDO DADOS FORNCEDOR PARA TAB_CAD
def mostrarFornecedores_CadServ():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM tbFornecedor"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
                    
    except sqlite3.Error as erros:
        print("Error ao buscar informações no banco: mostrarUnidades", erros)

    finally:
        cursor.close()
# FIM mostrarFornecedores_CadServ

# MOSTRANDO DADOS TIPO SERVICO PARA TAB_CAD
def mostrarTipoServico_CadServ():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM tbTipoServ"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
                    
    except sqlite3.Error as err:
        print("Error ao buscar informações no banco", err)

    finally:
        cursor.close()
# FIM mostrarTipoServico_CadServ