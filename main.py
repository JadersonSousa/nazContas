import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from main_ui import *
from backend import *
from utlis import *
import sqlite3

class MainWIndow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWIndow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"NazContas - Sistema de controle de Contas - Versão: {versaoAtual()}")
        self.showMaximized()
        self.my_treeWidget.itemClicked.connect(self.tree_onclick)
        
        
        self.child_item = QTreeWidgetItem(['Child'])
        
        #BOTÕES DE CADASTROS
        self.btnCadastroUnidade.clicked.connect(self.cadUnidade)
        self.btnCadTipServ.clicked.connect(self.cadTipoServ)
        
        #PAGINAÇÃO DA TABELA DE SERVIÇOS
        self.current_page = 0
        self.item_per_page = 10
        self.total_items = 0
        self.total_pages = 0
        
        self.btnNext.clicked.connect(self.proximaPagina)
        self.btnBack.clicked.connect(self.paginaAnterior)
    
        self.load_data()
    

    def tree_onclick(self, item):
        if item.parent() is not None:
            whats_this = item.whatsThis(0)
            self.pagesMain(name=whats_this)
            self.tabUnidades(page=whats_this)

        
        if item.whatsThis(0):
            self.pagesMain(name=item.whatsThis(0))

    
    def pagesMain(self, name):
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





if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWIndow()
    window.show()
    app.exec_()