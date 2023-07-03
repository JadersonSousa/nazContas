import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from main_ui import *
from modalEmpresa_ui import *
from modalForncedor_ui import *
from modalTpServico_ui import *
from backend import *
from utlis import *
from apiCnpj import *
import sqlite3


class MainWIndow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWIndow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"NazContas - Sistema de controle de Contas - Versão: {mostrarVersao()}")
        self.showMaximized()
        self.my_treeWidget.itemClicked.connect(self.tree_onclick)
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        
        self.child_item = QTreeWidgetItem(['Child'])
        
        #BOTÕES DE CADASTROS
        self.btnCadastroUnidade.clicked.connect(self.cadUnidade)
        self.btnCadTipServ.clicked.connect(self.cadTipoServ)
        self.btn_procurar_cnpj.clicked.connect(self.cardProcuraCNPJ)
        self.btnCadastroFrn.clicked.connect(self.finali_cad_fornecedor)
        self.toolBtnEmpresa.clicked.connect(self.modalEmpresa)
        self.toolBtnFornecedor.clicked.connect(self.modalFornecedor)
        self.toolBtnTpServ.clicked.connect(self.modalTipoServico)
        self.btnCadServico.clicked.connect(self.cadServico)

        #PAGINAÇÃO DA TABELA DE SERVIÇOS
        self.current_page = 0
        self.item_per_page = 10
        self.total_items = 0
        self.total_pages = 0
        
        self.btnNext.clicked.connect(self.proximaPagina)
        self.btnBack.clicked.connect(self.paginaAnterior)

        self.homeInfs()
        self.load_data()

    
        

    def tree_onclick(self, item):
        if item.parent() is not None:
            whats_this = item.whatsThis(0)
            self.pagesMain(name=whats_this)
            self.tabUnidades(page=whats_this)
            
        
        if item.whatsThis(0):
            self.pagesMain(name=item.whatsThis(0))
        
    
    def pagesMain(self, name):
        if 'pg_home' in name:
            self.homeInfs()
        next_page = self.stackedWidget.indexOf(self.stackedWidget.findChild(QWidget, name))
        self.stackedWidget.setCurrentIndex(next_page)

    
    def cadUnidade(self):
        unidade = self.input_unidade.text()
        razaoSocial = self.input_Razao.text()
        cnpj = self.input_cnpj.text()
        cidade = self.input_cidade.text()
        uf = self.input_uf.text()

        if unidade == '' or razaoSocial == '' or cnpj == '' or cidade == '' or uf == '':
            QMessageBox.critical(self, 'ALERTA DE ERRO', 'Preencha o todos os campos requeridos')
        else:
            data = cadastroUnidade(unidade, frmtText(text=str(razaoSocial.title())), cnpj, cidade, uf)

            result = data.keys()
            for chave in result:
                if chave in 'data':
                    msg = data['data']
                    
                    self.input_unidade.clear()
                    self.input_Razao.clear()
                    self.input_cnpj.clear()
                    self.input_cidade.clear()
                    self.input_uf.clear()


                    QMessageBox.information(self, "Sucesso", "Unidade cadastrada com sucesso \n Codigo: {}".format(str(msg)))
                    ##ATUALIZANDO A TABELA
                    self.tabUnidades(page='pg_cad_Unidade')

                else:
                    msgErro = data['error']
                    QMessageBox.critical(self, 'Erro', f'{msgErro}')

    def homeInfs(self):
            nmsHome = vwHomeInf()
            self.lb_nmServiHome.setText(str(nmsHome[0]))
            self.lb_nmServiHome_2.setText(str(nmsHome[1]))
            self.lb_nmServiHome_3.setText(str(nmsHome[2]))

    def tabUnidades(self, page):

        if 'pg_cad_Unidade' in page:
            
            dadosUnidades = mostrarUnidades()
            
            
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.setRowCount(len(dadosUnidades))
            self.tableWidget.setColumnCount(len(dadosUnidades[0]))

            for row, registro in enumerate(dadosUnidades):
                for column, valor in enumerate(registro):
                    item = QTableWidgetItem(str(valor))
                    self.tableWidget.setItem(row, column, item)
                    self.tableWidget.resizeColumnsToContents()
            
    def cardProcuraCNPJ(self):
        cnpj = self.input_cnpj_fornecedor.text()
        try:
            if len(cnpj) < 14:
                QMessageBox.critical(self, 'ALERTA DE ERRO', 'CNPJ informado falta números!!!')
            else:
                if 'CNPJ inválido' in dadosEmpresa(cnpj=cnpj):
                    QMessageBox.warning(self, 'ATENÇÃO', 'O CNPJ informado parece não ser valido, favor verifique.')
                else:
                    dados_empresa = dadosEmpresa(cnpj=cnpj)
                    

                    self.input_nome_fornecedor.setText(str(dados_empresa[1]))
                    self.input_nmFantasia_forncedor.setText(str(dados_empresa[2]))
                    self.input_tipo_atv.setText(str(dados_empresa[3]))

                    self.input_bairro_fornecedor.setText(str(dados_empresa[4]))
                    self.input_logradouro_forncedor.setText(str(dados_empresa[5]))
                    self.input_num_fornecedor.setText(str(dados_empresa[6]))
                    self.input_cep_fornecedor.setText(str(dados_empresa[7]))
                    self.input_munic_fornecedor.setText(str(dados_empresa[8]))
                    self.input_uf_fornecedor.setText(str(dados_empresa[9]))
        except:
            QMessageBox.critical(self, 'ALERTA DE ERRO', 'Houve um erro ao buscar CNPJ')

    def finali_cad_fornecedor(self):
        cnpj = self.input_cnpj_fornecedor.text()
        nome = self.input_nome_fornecedor.text()
        fantasia = self.input_nmFantasia_forncedor.text()
        tipoAtv = self.input_tipo_atv.text()
        bairro = self.input_bairro_fornecedor.text()
        logradouro = self.input_logradouro_forncedor.text()
        num = self.input_num_fornecedor.text()
        cep = self.input_cep_fornecedor.text()
        municipio = self.input_munic_fornecedor.text()
        uf = self.input_uf_fornecedor.text()

        if len(cnpj) == 0 | len(nome) == 0 | len(fantasia) == 0 | len(municipio) == 0 | len(uf) == 0:
            QMessageBox.critical(self, 'ALERTA DE ERRO', 'Preencha todos os campos.')
        else:
            cadFornecedor(cnpj, nome, fantasia, tipoAtv, bairro, logradouro, num, cep, municipio, uf)
            QMessageBox.warning(self, 'ATENÇÃO', 'Fonecedor cadastrado com sucesso')

    def cadTipoServ(self):
        tipoServico = self.input_TipoServ.text()
        
        if tipoServico == '':
            QMessageBox.critical(self, 'Erro', 'Preencha o todos os campos requeridos')
        else:
            data = cadTipoServico(tipoServico=tipoServico)
          

            result = data.keys()
            for chave in result:
                if chave in 'data':
                    msg = data['data']
                    
                    self.input_TipoServ.clear()


                    QMessageBox.information(self, "Sucesso", "Serviço cadastro com sucesso. \n Codigo: {}".format(str(msg)))


                else:
                    msgErro = data['error']
                    QMessageBox.critical(self, 'Erro', '{}'.format(msgErro))


    def cadServico(self):

        emp = self.lineEdit_4.text()
        frn = self.lineEdit_6.text()
        tpSrv = self.lineEdit_5.text()
        crc = self.lineEdit_7.text()
        dtVnc = self.dateEdit.text()

        if emp == '' or frn == '' or tpSrv == '' or crc == '' or dtVnc == '':
                    QMessageBox.critical(self, 'Erro', 'Preencha o todos os campos requeridos')
        else:
            data = cad_Servico(emp, frn, tpSrv, crc, dtVnc)
                

            result = data.keys()
            for chave in result:
                if chave in 'data':
                    msg = data['data']
                            
                    self.lineEdit_4.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_5.clear()
                    self.lineEdit_7.clear()
                    self.dateEdit.clear()

                    QMessageBox.information(self, "Sucesso", "Serviço cadastrado com sucesso. \n Codigo: {}".format(str(msg)))


                else:
                    msgErro = data['error']
                    QMessageBox.critical(self, 'Erro', '{}'.format(msgErro))
        


# MODAL EMPRESA NO CAD_SERV
    def modalEmpresa(self):
        self.modal = Dialog(self)

        dadosUnidades = mostrarUnidades_CadServ()
        
            
        self.modal.tableWidget.verticalHeader().setVisible(False)
        self.modal.tableWidget.setRowCount(len(dadosUnidades))
        self.modal.tableWidget.setColumnCount(len(dadosUnidades[0]))

        for row, registro in enumerate(dadosUnidades):
            for column, valor in enumerate(registro):
                item = QTableWidgetItem(str(valor))
                self.modal.tableWidget.setItem(row, column, item)
                self.modal.tableWidget.resizeColumnsToContents()
        
        self.modal.tableWidget.cellClicked.connect(self.obter_valor_empresa)

        
        self.modal.setModal(True)
        self.modal.show()
#FIM cadServ

# MODAL FORNECEDOR NO CAD_SERV
    def modalFornecedor(self):
        self.modalForn = DialogForn(self)

        dadosFornecedor = mostrarFornecedores_CadServ()

        self.modalForn.tbModalFornecedor.verticalHeader().setVisible(False)
        self.modalForn.tbModalFornecedor.setRowCount(len(dadosFornecedor))
        self.modalForn.tbModalFornecedor.setColumnCount(len(dadosFornecedor[0]))

        for row, registro in enumerate(dadosFornecedor):
            for column, valor in enumerate(registro):
                item = QTableWidgetItem(str(valor))
                self.modalForn.tbModalFornecedor.setItem(row, column, item)
                self.modalForn.tbModalFornecedor.resizeColumnsToContents()
        
        self.modalForn.tbModalFornecedor.cellClicked.connect(self.obter_valor_fornecedor)

        self.modalForn.setModal(True)
        self.modalForn.show()
#FIM modalFornecedor

# MODAL TIPO SERVICO NO CAD_SERV
    def modalTipoServico(self):
        self.modalTpSrv = DialogTpSrv(self)

        dadosTpServico = mostrarTipoServico_CadServ()

        self.modalTpSrv.tbModalTpServico.verticalHeader().setVisible(False)
        self.modalTpSrv.tbModalTpServico.setRowCount(len(dadosTpServico))
        self.modalTpSrv.tbModalTpServico.setColumnCount(len(dadosTpServico[0]))

        for row, registro in enumerate(dadosTpServico):
            for column, valor in enumerate(registro):
                item = QTableWidgetItem(str(valor))
                self.modalTpSrv.tbModalTpServico.setItem(row, column, item)
                self.modalTpSrv.tbModalTpServico.resizeColumnsToContents()
        
        self.modalTpSrv.tbModalTpServico.cellClicked.connect(self.obter_valor_tpServico)

        self.modalTpSrv.setModal(True)
        self.modalTpSrv.show()
#FIM modalTipoServico

# OBTER VALOR
    def obter_valor_empresa(self, row, colum):
        empresa = self.modal.tableWidget.item(row, 0)
        nomeEmp = self.modal.tableWidget.item(row, 2)
        if empresa is not None:
            valor = empresa.text()
            valor1 = nomeEmp.text()
            self.lineEdit_4.setText(str(valor))
            self.lbEmpCad.setText(str(valor1))

    def obter_valor_fornecedor(self, row, colum):
        forncedor = self.modalForn.tbModalFornecedor.item(row, 0)
        nomeForn = self.modalForn.tbModalFornecedor.item(row, 1)
        if forncedor is not None:
            forn = forncedor.text()
            nmFrn = nomeForn.text()
            self.lineEdit_6.setText(str(forn))
            self.lbFornCad.setText(str(nmFrn))
            
    def obter_valor_tpServico(self, row, colum):
        tipoServico = self.modalTpSrv.tbModalTpServico.item(row, 0)
        nomeTpSrv = self.modalTpSrv.tbModalTpServico.item(row, 1)
        if tipoServico is not None:
            tpSrv = tipoServico.text()
            nmTpSrv = nomeTpSrv.text()
            self.lineEdit_5.setText(str(tpSrv))
            self.lbTpSrvCad.setText(str(nmTpSrv))
#FIM obter_valor




    def load_data(self):
        try:
            with connect:
                cursor = connect.cursor()
                start_index = self.current_page * self.item_per_page
                end_index = start_index + self.item_per_page
                sql = f"SELECT * from vwServicos LIMIT {self.item_per_page} OFFSET {start_index}"

                cursor.execute(sql)
                dadosServicos = cursor.fetchall()


                


                totalServicos = vw_TotalServicos()[0]
                self.total_items = totalServicos
                self.total_pages = (self.total_items + self.item_per_page - 1) // self.item_per_page
                self.tt_nm_pg.setText(str(self.total_pages))
                self.nm_pg.setText(str(self.current_page+1))

                self.tableServicos.verticalHeader().setVisible(False)
                self.tableServicos.clearContents()
                self.tableServicos.setRowCount(len(dadosServicos))
                self.tableServicos.setColumnCount(len(dadosServicos[0]))

                for row, registro in enumerate(dadosServicos):
                    for column, valor in enumerate(registro):
                        item = QTableWidgetItem(str(valor))
                        self.tableServicos.setItem(row, column, item)                
                            
        except sqlite3.Error as erros:
            print("Error ao buscar informações no banco: vw_TotalServicos", erros)

        finally:
            cursor.close()
    
    def paginaAnterior(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.load_data()
    
    def proximaPagina(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.load_data()


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, window):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Modal - Empresa")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.window = window

class DialogForn(QDialog, Ui_DialogForn):
    def __init__(self, window):
        super(DialogForn, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Modal - Fornecedor")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.window = window

class DialogTpSrv(QDialog, Ui_DialogTpSrv):
    def __init__(self, window):
        super(DialogTpSrv, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Modal - Tipo Serviço")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.window = window


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWIndow()
    window.show()
    app.exec_()