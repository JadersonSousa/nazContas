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



def infoUnidade(unidade):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM tbUnidade WHERE unidade='{}'".format(unidade)
            cursor.execute(sql)
            result = cursor.fetchall()

            list_inf_und = [item for tupla in result for item in tupla]

            
            return list_inf_und
                    
    except sqlite3.Error as err:
        print("Error ao buscar informações no banco", err)

    finally:
        cursor.close()


def servicoEmpresa(unidade):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT circuito FROM tbServico WHERE codEmpresa='{}'".format(unidade)
            cursor.execute(sql)
            result = cursor.fetchall()

            list_inf_serv = [item for tupla in result for item in tupla]

            return list_inf_serv
                    
    except sqlite3.Error as err:
        print("Error ao buscar informações no banco", err)

    finally:
        cursor.close()


def servicoId(id):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM tbServico WHERE codEmpresa='{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()

            list_inf_servId = [item for tupla in result for item in tupla]
            
            
            return list_inf_servId
                    
    except sqlite3.Error as err:
        print("Error ao buscar informações no banco", err)
    
    finally:
        cursor.close()



def tipoServico(codServico):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM tbTipoServ WHERE idTpServ='{}'".format(codServico)
            cursor.execute(sql)
            result = cursor.fetchall()

            list_inf_tpServ = [item for tupla in result for item in tupla]
            

            return list_inf_tpServ
                    
    except sqlite3.Error as err:
        print("Error ao buscar informações no banco", err)

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