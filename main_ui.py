# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1226, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icon/icone.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.header_sys = QFrame(self.centralwidget)
        self.header_sys.setObjectName(u"header_sys")
        self.header_sys.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_sys.sizePolicy().hasHeightForWidth())
        self.header_sys.setSizePolicy(sizePolicy1)
        self.header_sys.setMinimumSize(QSize(30, 20))
        self.header_sys.setMaximumSize(QSize(200, 50))
        self.header_sys.setLayoutDirection(Qt.LeftToRight)
        self.header_sys.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_sys.setFrameShape(QFrame.NoFrame)
        self.header_sys.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.header_sys)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.header_sys)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QSize(200, 16777215))
        self.label_10.setFrameShadow(QFrame.Raised)
        self.label_10.setText(u"")
        self.label_10.setPixmap(QPixmap(u":/icon/icon/lg-naz.gif"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(False)
        self.label_10.setMargin(9)

        self.verticalLayout_9.addWidget(self.label_10)


        self.gridLayout.addWidget(self.header_sys, 0, 0, 1, 1)

        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMaximumSize(QSize(200, 16777215))
        self.frame_menu.setFrameShape(QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_menu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.my_treeWidget = QTreeWidget(self.frame_menu)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 216))
        brush.setStyle(Qt.NoBrush)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/config.png", QSize(), QIcon.Normal, QIcon.Off)
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/setConfig.png", QSize(), QIcon.Normal, QIcon.Off)
        font2 = QFont()
        font2.setPointSize(8)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/relatorios.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/lancamentos.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/setLanc.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtreewidgetitem = QTreeWidgetItem(self.my_treeWidget)
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(0, font);
        __qtreewidgetitem.setForeground(0, brush);
        __qtreewidgetitem.setIcon(0, icon1);
        __qtreewidgetitem1 = QTreeWidgetItem(self.my_treeWidget)
        __qtreewidgetitem1.setFont(0, font1);
        __qtreewidgetitem1.setIcon(0, icon2);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setFont(0, font2);
        __qtreewidgetitem2.setIcon(0, icon3);
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem3.setFont(0, font2);
        __qtreewidgetitem3.setIcon(0, icon3);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem4.setFont(0, font2);
        __qtreewidgetitem4.setIcon(0, icon3);
        __qtreewidgetitem5 = QTreeWidgetItem(self.my_treeWidget)
        __qtreewidgetitem5.setFont(0, font1);
        __qtreewidgetitem5.setIcon(0, icon4);
        QTreeWidgetItem(__qtreewidgetitem5)
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(self.my_treeWidget)
        __qtreewidgetitem7.setFont(0, font1);
        __qtreewidgetitem7.setIcon(0, icon5);
        __qtreewidgetitem8 = QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8.setIcon(0, icon6);
        self.my_treeWidget.setObjectName(u"my_treeWidget")
        self.my_treeWidget.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(10)
        self.my_treeWidget.setFont(font3)
        self.my_treeWidget.setFrameShape(QFrame.NoFrame)
        self.my_treeWidget.setFrameShadow(QFrame.Raised)
        self.my_treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.my_treeWidget.setProperty("showDropIndicator", True)
        self.my_treeWidget.setIconSize(QSize(20, 20))
        self.my_treeWidget.setTextElideMode(Qt.ElideLeft)
        self.my_treeWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.my_treeWidget.setAutoExpandDelay(1)
        self.my_treeWidget.setIndentation(18)
        self.my_treeWidget.setUniformRowHeights(False)
        self.my_treeWidget.setItemsExpandable(True)
        self.my_treeWidget.setAnimated(True)
        self.my_treeWidget.setAllColumnsShowFocus(False)
        self.my_treeWidget.setWordWrap(False)
        self.my_treeWidget.setHeaderHidden(False)
        self.my_treeWidget.setExpandsOnDoubleClick(True)
        self.my_treeWidget.header().setVisible(True)
        self.my_treeWidget.header().setCascadingSectionResizes(False)
        self.my_treeWidget.header().setHighlightSections(False)
        self.my_treeWidget.header().setProperty("showSortIndicator", False)

        self.horizontalLayout.addWidget(self.my_treeWidget)


        self.gridLayout.addWidget(self.frame_menu, 3, 0, 1, 1)

        self.frame_telas = QFrame(self.centralwidget)
        self.frame_telas.setObjectName(u"frame_telas")
        self.frame_telas.setStyleSheet(u"")
        self.frame_telas.setFrameShape(QFrame.NoFrame)
        self.frame_telas.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_telas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_telas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setStyleSheet(u"")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.frame_home = QFrame(self.pg_home)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setGeometry(QRect(9, 55, 1008, 526))
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_home)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 661, 140))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_6)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 180, 70))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_ServiHome = QLabel(self.layoutWidget)
        self.lb_ServiHome.setObjectName(u"lb_ServiHome")
        self.lb_ServiHome.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamily(u"Arial Narrow")
        font4.setBold(True)
        font4.setWeight(75)
        self.lb_ServiHome.setFont(font4)
        self.lb_ServiHome.setLayoutDirection(Qt.LeftToRight)
        self.lb_ServiHome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lb_ServiHome)

        self.Subframe_home = QFrame(self.layoutWidget)
        self.Subframe_home.setObjectName(u"Subframe_home")
        self.Subframe_home.setMaximumSize(QSize(16777215, 80))
        self.Subframe_home.setStyleSheet(u"#Subframe_home {\n"
"	background-color: #fff;\n"
"	border-radius: 15px;\n"
"}")
        self.Subframe_home.setFrameShape(QFrame.StyledPanel)
        self.Subframe_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Subframe_home)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lb_nmServiHome = QLabel(self.Subframe_home)
        self.lb_nmServiHome.setObjectName(u"lb_nmServiHome")
        font5 = QFont()
        font5.setPointSize(20)
        self.lb_nmServiHome.setFont(font5)
        self.lb_nmServiHome.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lb_nmServiHome)


        self.verticalLayout_8.addWidget(self.Subframe_home)

        self.layoutWidget_2 = QWidget(self.frame_6)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(210, 10, 180, 70))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lb_ServiHome_2 = QLabel(self.layoutWidget_2)
        self.lb_ServiHome_2.setObjectName(u"lb_ServiHome_2")
        self.lb_ServiHome_2.setMaximumSize(QSize(16777215, 20))
        self.lb_ServiHome_2.setFont(font4)
        self.lb_ServiHome_2.setLayoutDirection(Qt.LeftToRight)
        self.lb_ServiHome_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lb_ServiHome_2)

        self.Subframe_home_2 = QFrame(self.layoutWidget_2)
        self.Subframe_home_2.setObjectName(u"Subframe_home_2")
        self.Subframe_home_2.setMaximumSize(QSize(16777215, 80))
        self.Subframe_home_2.setStyleSheet(u"#Subframe_home_2 {\n"
"	background-color: #fff;\n"
"	border-radius: 15px;\n"
"}")
        self.Subframe_home_2.setFrameShape(QFrame.StyledPanel)
        self.Subframe_home_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Subframe_home_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lb_nmServiHome_2 = QLabel(self.Subframe_home_2)
        self.lb_nmServiHome_2.setObjectName(u"lb_nmServiHome_2")
        self.lb_nmServiHome_2.setFont(font5)
        self.lb_nmServiHome_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lb_nmServiHome_2)


        self.verticalLayout_10.addWidget(self.Subframe_home_2)

        self.layoutWidget_3 = QWidget(self.frame_6)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(410, 10, 180, 70))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lb_ServiHome_3 = QLabel(self.layoutWidget_3)
        self.lb_ServiHome_3.setObjectName(u"lb_ServiHome_3")
        self.lb_ServiHome_3.setMaximumSize(QSize(16777215, 20))
        self.lb_ServiHome_3.setFont(font4)
        self.lb_ServiHome_3.setLayoutDirection(Qt.LeftToRight)
        self.lb_ServiHome_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lb_ServiHome_3)

        self.Subframe_home_3 = QFrame(self.layoutWidget_3)
        self.Subframe_home_3.setObjectName(u"Subframe_home_3")
        self.Subframe_home_3.setMaximumSize(QSize(16777215, 80))
        self.Subframe_home_3.setStyleSheet(u"#Subframe_home_3 {\n"
"	background-color: #fff;\n"
"	border-radius: 15px;\n"
"}")
        self.Subframe_home_3.setFrameShape(QFrame.StyledPanel)
        self.Subframe_home_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Subframe_home_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lb_nmServiHome_3 = QLabel(self.Subframe_home_3)
        self.lb_nmServiHome_3.setObjectName(u"lb_nmServiHome_3")
        self.lb_nmServiHome_3.setFont(font5)
        self.lb_nmServiHome_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lb_nmServiHome_3)


        self.verticalLayout_11.addWidget(self.Subframe_home_3)

        self.label_12 = QLabel(self.pg_home)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 20, 1026, 31))
        font6 = QFont()
        font6.setFamily(u"Arial Narrow")
        font6.setPointSize(20)
        font6.setItalic(False)
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"color: rgb(103, 103, 103);")
        self.stackedWidget.addWidget(self.pg_home)
        self.pg_cad_Unidade = QWidget()
        self.pg_cad_Unidade.setObjectName(u"pg_cad_Unidade")
        self.pg_cad_Unidade.setStyleSheet(u"")
        self.frame = QFrame(self.pg_cad_Unidade)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 511, 271))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.input_unidade = QLineEdit(self.frame)
        self.input_unidade.setObjectName(u"input_unidade")
        self.input_unidade.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.input_unidade)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, -1, 0, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_3.addWidget(self.label)

        self.input_Razao = QLineEdit(self.frame)
        self.input_Razao.setObjectName(u"input_Razao")

        self.horizontalLayout_3.addWidget(self.input_Razao)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(13, -1, -1, -1)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.input_cnpj = QLineEdit(self.frame)
        self.input_cnpj.setObjectName(u"input_cnpj")
        self.input_cnpj.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_6.addWidget(self.input_cnpj)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.input_cidade = QLineEdit(self.frame)
        self.input_cidade.setObjectName(u"input_cidade")

        self.horizontalLayout_4.addWidget(self.input_cidade)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(23, -1, -1, -1)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.input_uf = QLineEdit(self.frame)
        self.input_uf.setObjectName(u"input_uf")
        self.input_uf.setInputMethodHints(Qt.ImhNone)
        self.input_uf.setMaxLength(2)
        self.input_uf.setFrame(True)

        self.horizontalLayout_5.addWidget(self.input_uf)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.btnCadastroUnidade = QPushButton(self.pg_cad_Unidade)
        self.btnCadastroUnidade.setObjectName(u"btnCadastroUnidade")
        self.btnCadastroUnidade.setGeometry(QRect(170, 300, 221, 23))
        self.frame_7 = QFrame(self.pg_cad_Unidade)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 340, 771, 311))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.tableWidget = QTableWidget(self.frame_7)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.pg_cad_Unidade)
        self.pg_cad_Forn = QWidget()
        self.pg_cad_Forn.setObjectName(u"pg_cad_Forn")
        self.pg_cad_Forn.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.pg_cad_Forn)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.pg_cad_Forn)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(50, 50, 691, 461))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(True)
        self.btnCadastroFrn = QPushButton(self.groupBox_2)
        self.btnCadastroFrn.setObjectName(u"btnCadastroFrn")
        self.btnCadastroFrn.setGeometry(QRect(200, 400, 370, 29))
        self.btnCadastroFrn.setFont(font)
        self.btnCadastroFrn.setCursor(QCursor(Qt.PointingHandCursor))
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 160, 641, 211))
        font7 = QFont()
        font7.setBold(False)
        font7.setWeight(50)
        self.groupBox_3.setFont(font7)
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.layoutWidget1 = QWidget(self.groupBox_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 211, 22))
        self.horizontalLayout_22 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_22.setSpacing(2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_22.addWidget(self.label_19)

        self.input_bairro_fornecedor = QLineEdit(self.layoutWidget1)
        self.input_bairro_fornecedor.setObjectName(u"input_bairro_fornecedor")

        self.horizontalLayout_22.addWidget(self.input_bairro_fornecedor)

        self.layoutWidget2 = QWidget(self.groupBox_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 50, 212, 24))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_23.setSpacing(2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_23.addWidget(self.label_20)

        self.input_logradouro_forncedor = QLineEdit(self.layoutWidget2)
        self.input_logradouro_forncedor.setObjectName(u"input_logradouro_forncedor")

        self.horizontalLayout_23.addWidget(self.input_logradouro_forncedor)

        self.layoutWidget3 = QWidget(self.groupBox_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 80, 211, 22))
        self.horizontalLayout_21 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_21.addWidget(self.label_18)

        self.input_num_fornecedor = QLineEdit(self.layoutWidget3)
        self.input_num_fornecedor.setObjectName(u"input_num_fornecedor")

        self.horizontalLayout_21.addWidget(self.input_num_fornecedor)

        self.layoutWidget4 = QWidget(self.groupBox_3)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 110, 211, 22))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_20.addWidget(self.label_17)

        self.input_cep_fornecedor = QLineEdit(self.layoutWidget4)
        self.input_cep_fornecedor.setObjectName(u"input_cep_fornecedor")

        self.horizontalLayout_20.addWidget(self.input_cep_fornecedor)

        self.layoutWidget5 = QWidget(self.groupBox_3)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 140, 211, 22))
        self.horizontalLayout_24 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_24.setSpacing(2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_24.addWidget(self.label_21)

        self.input_munic_fornecedor = QLineEdit(self.layoutWidget5)
        self.input_munic_fornecedor.setObjectName(u"input_munic_fornecedor")

        self.horizontalLayout_24.addWidget(self.input_munic_fornecedor)

        self.layoutWidget6 = QWidget(self.groupBox_3)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 170, 211, 22))
        self.horizontalLayout_25 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_25.setSpacing(2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_25.addWidget(self.label_22)

        self.input_uf_fornecedor = QLineEdit(self.layoutWidget6)
        self.input_uf_fornecedor.setObjectName(u"input_uf_fornecedor")

        self.horizontalLayout_25.addWidget(self.input_uf_fornecedor)

        self.layoutWidget7 = QWidget(self.groupBox_2)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(20, 20, 411, 26))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(1, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_16.addWidget(self.label_13)

        self.input_cnpj_fornecedor = QLineEdit(self.layoutWidget7)
        self.input_cnpj_fornecedor.setObjectName(u"input_cnpj_fornecedor")
        self.input_cnpj_fornecedor.setMaximumSize(QSize(16777215, 20))
        self.input_cnpj_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.input_cnpj_fornecedor.setMaxLength(14)

        self.horizontalLayout_16.addWidget(self.input_cnpj_fornecedor)

        self.btn_procurar_cnpj = QPushButton(self.layoutWidget7)
        self.btn_procurar_cnpj.setObjectName(u"btn_procurar_cnpj")
        self.btn_procurar_cnpj.setMaximumSize(QSize(16777215, 22))
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/setLupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_procurar_cnpj.setIcon(icon7)

        self.horizontalLayout_16.addWidget(self.btn_procurar_cnpj)

        self.layoutWidget8 = QWidget(self.groupBox_2)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(20, 50, 411, 22))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_17.addWidget(self.label_14)

        self.input_nome_fornecedor = QLineEdit(self.layoutWidget8)
        self.input_nome_fornecedor.setObjectName(u"input_nome_fornecedor")

        self.horizontalLayout_17.addWidget(self.input_nome_fornecedor)

        self.layoutWidget9 = QWidget(self.groupBox_2)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(20, 80, 411, 22))
        self.horizontalLayout_18 = QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_18.addWidget(self.label_15)

        self.input_nmFantasia_forncedor = QLineEdit(self.layoutWidget9)
        self.input_nmFantasia_forncedor.setObjectName(u"input_nmFantasia_forncedor")

        self.horizontalLayout_18.addWidget(self.input_nmFantasia_forncedor)

        self.layoutWidget10 = QWidget(self.groupBox_2)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(20, 110, 411, 22))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_19.addWidget(self.label_16)

        self.input_tipo_atv = QLineEdit(self.layoutWidget10)
        self.input_tipo_atv.setObjectName(u"input_tipo_atv")

        self.horizontalLayout_19.addWidget(self.input_tipo_atv)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 301, 41))
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: rgb(103, 103, 103);")

        self.verticalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.pg_cad_Forn)
        self.pg_cad_Serv_TipServ = QWidget()
        self.pg_cad_Serv_TipServ.setObjectName(u"pg_cad_Serv_TipServ")
        self.verticalLayout_5 = QVBoxLayout(self.pg_cad_Serv_TipServ)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.label_3 = QLabel(self.pg_cad_Serv_TipServ)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color: rgb(103, 103, 103);")

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame_4 = QFrame(self.pg_cad_Serv_TipServ)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(100, 40, 391, 69))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.input_TipoServ = QLineEdit(self.frame_5)
        self.input_TipoServ.setObjectName(u"input_TipoServ")
        self.input_TipoServ.setMinimumSize(QSize(0, 25))
        self.input_TipoServ.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_6.addWidget(self.input_TipoServ)

        self.btnCadTipServ = QPushButton(self.frame_5)
        self.btnCadTipServ.setObjectName(u"btnCadTipServ")
        self.btnCadTipServ.setMinimumSize(QSize(0, 25))
        self.btnCadTipServ.setMaximumSize(QSize(16777215, 30))
        self.btnCadTipServ.setFont(font)

        self.verticalLayout_6.addWidget(self.btnCadTipServ)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 160, 721, 371))
        font8 = QFont()
        font8.setFamily(u"Arial Narrow")
        font8.setPointSize(9)
        self.frame_8.setFont(font8)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.tableServicos = QTableWidget(self.frame_8)
        if (self.tableServicos.columnCount() < 6):
            self.tableServicos.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableServicos.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableServicos.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableServicos.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableServicos.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableServicos.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableServicos.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableServicos.setObjectName(u"tableServicos")
        self.tableServicos.setGeometry(QRect(0, 0, 721, 311))
        self.tableServicos.setFrameShape(QFrame.StyledPanel)
        self.tableServicos.setFrameShadow(QFrame.Plain)
        self.tableServicos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableServicos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableServicos.setGridStyle(Qt.DashLine)
        self.buttonsTable = QFrame(self.frame_8)
        self.buttonsTable.setObjectName(u"buttonsTable")
        self.buttonsTable.setGeometry(QRect(0, 340, 171, 30))
        self.buttonsTable.setMaximumSize(QSize(16777215, 35))
        self.buttonsTable.setFrameShape(QFrame.StyledPanel)
        self.buttonsTable.setFrameShadow(QFrame.Raised)
        self.layoutWidget11 = QWidget(self.buttonsTable)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(0, 0, 143, 25))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.layoutWidget11)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setMaximumSize(QSize(30, 20))
        font9 = QFont()
        font9.setFamily(u"Arial Narrow")
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setWeight(75)
        self.btnBack.setFont(font9)

        self.horizontalLayout_12.addWidget(self.btnBack)

        self.nm_pg = QLabel(self.layoutWidget11)
        self.nm_pg.setObjectName(u"nm_pg")
        self.nm_pg.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_12.addWidget(self.nm_pg)

        self.lb_nm_pgs = QLabel(self.layoutWidget11)
        self.lb_nm_pgs.setObjectName(u"lb_nm_pgs")
        self.lb_nm_pgs.setFont(font8)

        self.horizontalLayout_12.addWidget(self.lb_nm_pgs)

        self.tt_nm_pg = QLabel(self.layoutWidget11)
        self.tt_nm_pg.setObjectName(u"tt_nm_pg")
        self.tt_nm_pg.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_12.addWidget(self.tt_nm_pg)

        self.btnNext = QPushButton(self.layoutWidget11)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setMaximumSize(QSize(30, 20))
        self.btnNext.setFont(font9)

        self.horizontalLayout_12.addWidget(self.btnNext)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 140, 201, 16))
        font10 = QFont()
        font10.setFamily(u"Arial Narrow")
        font10.setPointSize(12)
        self.label_11.setFont(font10)
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 721, 91))
        self.btnCadServico = QPushButton(self.groupBox)
        self.btnCadServico.setObjectName(u"btnCadServico")
        self.btnCadServico.setGeometry(QRect(360, 50, 161, 23))
        self.btnCadServico.setFont(font)
        self.layoutWidget12 = QWidget(self.groupBox)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.layoutWidget12.setGeometry(QRect(190, 20, 281, 27))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget12)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.layoutWidget12)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 25))
        self.lineEdit_6.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_6.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_6.setMaxLength(3)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setEchoMode(QLineEdit.Normal)
        self.lineEdit_6.setCursorPosition(0)

        self.horizontalLayout_10.addWidget(self.lineEdit_6)

        self.toolBtnFornecedor = QToolButton(self.layoutWidget12)
        self.toolBtnFornecedor.setObjectName(u"toolBtnFornecedor")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.toolBtnFornecedor.sizePolicy().hasHeightForWidth())
        self.toolBtnFornecedor.setSizePolicy(sizePolicy4)
        self.toolBtnFornecedor.setMinimumSize(QSize(0, 25))
        self.toolBtnFornecedor.setMaximumSize(QSize(20, 16777215))
        self.toolBtnFornecedor.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.toolBtnFornecedor)

        self.lbFornCad = QLabel(self.layoutWidget12)
        self.lbFornCad.setObjectName(u"lbFornCad")
        font11 = QFont()
        font11.setPointSize(7)
        font11.setBold(True)
        font11.setWeight(75)
        self.lbFornCad.setFont(font11)

        self.horizontalLayout_10.addWidget(self.lbFornCad)

        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 50, 161, 25))
        self.lineEdit_7.setMinimumSize(QSize(0, 25))
        self.layoutWidget13 = QWidget(self.groupBox)
        self.layoutWidget13.setObjectName(u"layoutWidget13")
        self.layoutWidget13.setGeometry(QRect(10, 20, 171, 27))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.layoutWidget13)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 25))
        self.lineEdit_4.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_4.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setEchoMode(QLineEdit.Normal)
        self.lineEdit_4.setCursorPosition(0)

        self.horizontalLayout_8.addWidget(self.lineEdit_4)

        self.toolBtnEmpresa = QToolButton(self.layoutWidget13)
        self.toolBtnEmpresa.setObjectName(u"toolBtnEmpresa")
        self.toolBtnEmpresa.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.toolBtnEmpresa.sizePolicy().hasHeightForWidth())
        self.toolBtnEmpresa.setSizePolicy(sizePolicy4)
        self.toolBtnEmpresa.setMinimumSize(QSize(0, 25))
        self.toolBtnEmpresa.setMaximumSize(QSize(20, 16777215))
        self.toolBtnEmpresa.setIconSize(QSize(20, 20))
        self.toolBtnEmpresa.setPopupMode(QToolButton.DelayedPopup)
        self.toolBtnEmpresa.setAutoRaise(False)
        self.toolBtnEmpresa.setArrowType(Qt.NoArrow)

        self.horizontalLayout_8.addWidget(self.toolBtnEmpresa)

        self.lbEmpCad = QLabel(self.layoutWidget13)
        self.lbEmpCad.setObjectName(u"lbEmpCad")
        self.lbEmpCad.setMaximumSize(QSize(90, 16777215))
        self.lbEmpCad.setFont(font11)

        self.horizontalLayout_8.addWidget(self.lbEmpCad)

        self.layoutWidget14 = QWidget(self.groupBox)
        self.layoutWidget14.setObjectName(u"layoutWidget14")
        self.layoutWidget14.setGeometry(QRect(190, 50, 161, 22))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget14)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget14)
        self.label_8.setObjectName(u"label_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.dateEdit = QDateEdit(self.layoutWidget14)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setWrapping(True)
        self.dateEdit.setFrame(True)
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_11.addWidget(self.dateEdit)

        self.layoutWidget15 = QWidget(self.groupBox)
        self.layoutWidget15.setObjectName(u"layoutWidget15")
        self.layoutWidget15.setGeometry(QRect(480, 20, 231, 27))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget15)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.layoutWidget15)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 25))
        self.lineEdit_5.setMaximumSize(QSize(66, 16777215))

        self.horizontalLayout_9.addWidget(self.lineEdit_5)

        self.toolBtnTpServ = QToolButton(self.layoutWidget15)
        self.toolBtnTpServ.setObjectName(u"toolBtnTpServ")
        sizePolicy4.setHeightForWidth(self.toolBtnTpServ.sizePolicy().hasHeightForWidth())
        self.toolBtnTpServ.setSizePolicy(sizePolicy4)
        self.toolBtnTpServ.setMinimumSize(QSize(0, 25))
        self.toolBtnTpServ.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_9.addWidget(self.toolBtnTpServ)

        self.lbTpSrvCad = QLabel(self.layoutWidget15)
        self.lbTpSrvCad.setObjectName(u"lbTpSrvCad")
        self.lbTpSrvCad.setFont(font11)

        self.horizontalLayout_9.addWidget(self.lbTpSrvCad)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.pg_cad_Serv_TipServ)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame_telas, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtreewidgetitem = self.my_treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Menu", None));

        __sortingEnabled = self.my_treeWidget.isSortingEnabled()
        self.my_treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.my_treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Home", None));
#if QT_CONFIG(whatsthis)
        ___qtreewidgetitem1.setWhatsThis(0, QCoreApplication.translate("MainWindow", u"pg_home", None));
#endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem2 = self.my_treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Sistema", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Cadastro de Unidades", None));
#if QT_CONFIG(whatsthis)
        ___qtreewidgetitem3.setWhatsThis(0, QCoreApplication.translate("MainWindow", u"pg_cad_Unidade", None));
#endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Cadastro de Servi\u00e7os", None));
#if QT_CONFIG(whatsthis)
        ___qtreewidgetitem4.setWhatsThis(0, QCoreApplication.translate("MainWindow", u"pg_cad_Serv_TipServ", None));
#endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem5 = ___qtreewidgetitem2.child(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Cadastro de Fornecedor", None));
#if QT_CONFIG(whatsthis)
        ___qtreewidgetitem5.setWhatsThis(0, QCoreApplication.translate("MainWindow", u"pg_cad_Forn", None));
#endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem6 = self.my_treeWidget.topLevelItem(2)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Relat\u00f3rios", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Rela\u00e7\u00e3o de Unidades", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem6.child(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Rela\u00e7\u00e3o de Circuitos", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Por Unidade", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem8.child(1)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"Geral", None));
        ___qtreewidgetitem11 = self.my_treeWidget.topLevelItem(3)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Lan\u00e7amentos", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Quita\u00e7\u00e3o", None));
        self.my_treeWidget.setSortingEnabled(__sortingEnabled)

        self.lb_ServiHome.setText(QCoreApplication.translate("MainWindow", u"TOTAL DE SERVI\u00c7OS", None))
        self.lb_nmServiHome.setText("")
        self.lb_ServiHome_2.setText(QCoreApplication.translate("MainWindow", u"UNIDADES CADASTRADAS", None))
        self.lb_nmServiHome_2.setText("")
        self.lb_ServiHome_3.setText(QCoreApplication.translate("MainWindow", u"TOTAL FORNECEDOR", None))
        self.lb_nmServiHome_3.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Unidade: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CNPJ: ", None))
        self.input_cnpj.setInputMask(QCoreApplication.translate("MainWindow", u"00.000.000/0000-00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cidade: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"UF: ", None))
        self.input_uf.setInputMask("")
        self.btnCadastroUnidade.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Rela\u00e7\u00e3o de unidades cadastradas", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cod", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Unidade", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Razao", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es de Cadastro", None))
        self.btnCadastroFrn.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Bairro:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CEP:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Municipio:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"UF:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Procurar CNPJ:", None))
        self.btn_procurar_cnpj.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nome Fantasia:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Tipo de Atividade:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Fornecedor", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  Cadastro Tipo de Servi\u00e7o / Servi\u00e7o", None))
        self.input_TipoServ.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo Servi\u00e7o", None))
        self.btnCadTipServ.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tipo Servi\u00e7o", None))
        ___qtablewidgetitem6 = self.tableServicos.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cod. Servi\u00e7o", None));
        ___qtablewidgetitem7 = self.tableServicos.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Unidade", None));
        ___qtablewidgetitem8 = self.tableServicos.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Fornecedor", None));
        ___qtablewidgetitem9 = self.tableServicos.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7o", None));
        ___qtablewidgetitem10 = self.tableServicos.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Circuito", None));
        ___qtablewidgetitem11 = self.tableServicos.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Data Vencimento", None));
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.nm_pg.setText("")
        self.lb_nm_pgs.setText(QCoreApplication.translate("MainWindow", u"P\u00e1gina de", None))
        self.tt_nm_pg.setText("")
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7os Cadastros", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro Servi\u00e7os", None))
        self.btnCadServico.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fornecedor", None))
        self.toolBtnFornecedor.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbFornCad.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Circuito", None))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.toolBtnEmpresa.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbEmpCad.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dia Venc.:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo servi\u00e7o", None))
        self.toolBtnTpServ.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbTpSrvCad.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Servi\u00e7o", None))
    # retranslateUi

