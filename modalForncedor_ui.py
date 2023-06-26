# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modalForncedor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogForn(object):
    def setupUi(self, DialogForn):
        if not DialogForn.objectName():
            DialogForn.setObjectName(u"DialogForn")
        DialogForn.resize(433, 300)
        self.horizontalLayout_2 = QHBoxLayout(DialogForn)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(DialogForn)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbModalFornecedor = QTableWidget(self.frame)
        if (self.tbModalFornecedor.columnCount() < 3):
            self.tbModalFornecedor.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbModalFornecedor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbModalFornecedor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbModalFornecedor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tbModalFornecedor.setObjectName(u"tbModalFornecedor")

        self.horizontalLayout.addWidget(self.tbModalFornecedor)


        self.horizontalLayout_2.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogForn)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(DialogForn)
        self.buttonBox.accepted.connect(DialogForn.accept)
        self.buttonBox.rejected.connect(DialogForn.reject)

        QMetaObject.connectSlotsByName(DialogForn)
    # setupUi

    def retranslateUi(self, DialogForn):
        DialogForn.setWindowTitle(QCoreApplication.translate("DialogForn", u"Dialog", None))
        ___qtablewidgetitem = self.tbModalFornecedor.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogForn", u"Cod.", None));
        ___qtablewidgetitem1 = self.tbModalFornecedor.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogForn", u"Nome", None));
        ___qtablewidgetitem2 = self.tbModalFornecedor.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogForn", u"Servi\u00e7o", None));
    # retranslateUi

