# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modalContas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogConta(object):
    def setupUi(self, DialogConta):
        if not DialogConta.objectName():
            DialogConta.setObjectName(u"DialogConta")
        DialogConta.resize(385, 293)
        DialogConta.setStyleSheet(u"#DialogConta{\n"
"	\n"
"	background-color: rgb(200, 192, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(DialogConta)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(DialogConta)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tbConta = QTableWidget(self.frame)
        if (self.tbConta.columnCount() < 2):
            self.tbConta.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbConta.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbConta.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbConta.setObjectName(u"tbConta")
        self.tbConta.setGeometry(QRect(1, 1, 252, 222))
        self.tbConta.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tbConta.setAcceptDrops(False)
        self.tbConta.setAutoFillBackground(False)
        self.tbConta.setFrameShape(QFrame.StyledPanel)
        self.tbConta.setFrameShadow(QFrame.Plain)
        self.tbConta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbConta.setDragDropOverwriteMode(True)
        self.tbConta.setAlternatingRowColors(True)
        self.tbConta.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tbConta.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbConta.horizontalHeader().setCascadingSectionResizes(False)
        self.tbConta.horizontalHeader().setHighlightSections(True)
        self.tbConta.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbConta.horizontalHeader().setStretchLastSection(True)
        self.tbConta.verticalHeader().setCascadingSectionResizes(False)
        self.tbConta.verticalHeader().setHighlightSections(True)
        self.tbConta.verticalHeader().setStretchLastSection(False)
        self.btnNext = QPushButton(self.frame)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(108, 224, 30, 20))
        self.btnNext.setMaximumSize(QSize(30, 20))
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnNext.setFont(font)
        self.btnNext.setCursor(QCursor(Qt.PointingHandCursor))
        self.tt_nm_pg = QLabel(self.frame)
        self.tt_nm_pg.setObjectName(u"tt_nm_pg")
        self.tt_nm_pg.setGeometry(QRect(97, 224, 16, 16))
        self.tt_nm_pg.setMaximumSize(QSize(20, 16777215))
        self.nm_pg = QLabel(self.frame)
        self.nm_pg.setObjectName(u"nm_pg")
        self.nm_pg.setGeometry(QRect(38, 224, 16, 16))
        self.nm_pg.setMaximumSize(QSize(20, 16777215))
        self.lb_nm_pgs = QLabel(self.frame)
        self.lb_nm_pgs.setObjectName(u"lb_nm_pgs")
        self.lb_nm_pgs.setGeometry(QRect(49, 224, 42, 16))
        font1 = QFont()
        font1.setFamily(u"Arial Narrow")
        font1.setPointSize(9)
        self.lb_nm_pgs.setFont(font1)
        self.btnBack = QPushButton(self.frame)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(2, 224, 30, 20))
        self.btnBack.setMaximumSize(QSize(30, 20))
        self.btnBack.setFont(font)
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogConta)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogConta)
        self.buttonBox.accepted.connect(DialogConta.accept)
        self.buttonBox.rejected.connect(DialogConta.reject)

        QMetaObject.connectSlotsByName(DialogConta)
    # setupUi

    def retranslateUi(self, DialogConta):
        DialogConta.setWindowTitle(QCoreApplication.translate("DialogConta", u"Dialog", None))
        ___qtablewidgetitem = self.tbConta.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogConta", u"Cod.", None));
        ___qtablewidgetitem1 = self.tbConta.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogConta", u"Circuito/Conta", None));
        self.btnNext.setText(QCoreApplication.translate("DialogConta", u">", None))
        self.tt_nm_pg.setText("")
        self.nm_pg.setText("")
        self.lb_nm_pgs.setText(QCoreApplication.translate("DialogConta", u"P\u00e1gina de", None))
        self.btnBack.setText(QCoreApplication.translate("DialogConta", u"<", None))
    # retranslateUi

