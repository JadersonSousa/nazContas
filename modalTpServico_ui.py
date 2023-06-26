# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modalTpServico.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogTpSrv(object):
    def setupUi(self, DialogTpSrv):
        if not DialogTpSrv.objectName():
            DialogTpSrv.setObjectName(u"DialogTpSrv")
        DialogTpSrv.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(DialogTpSrv)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(DialogTpSrv)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tbModalTpServico = QTableWidget(self.frame)
        if (self.tbModalTpServico.columnCount() < 2):
            self.tbModalTpServico.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbModalTpServico.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbModalTpServico.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbModalTpServico.setObjectName(u"tbModalTpServico")

        self.verticalLayout.addWidget(self.tbModalTpServico)


        self.horizontalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogTpSrv)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogTpSrv)
        self.buttonBox.accepted.connect(DialogTpSrv.accept)
        self.buttonBox.rejected.connect(DialogTpSrv.reject)

        QMetaObject.connectSlotsByName(DialogTpSrv)
    # setupUi

    def retranslateUi(self, DialogTpSrv):
        DialogTpSrv.setWindowTitle(QCoreApplication.translate("DialogTpSrv", u"Dialog", None))
        ___qtablewidgetitem = self.tbModalTpServico.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogTpSrv", u"Cod.", None));
        ___qtablewidgetitem1 = self.tbModalTpServico.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogTpSrv", u"Tipo de Servi\u00e7o", None));
    # retranslateUi

