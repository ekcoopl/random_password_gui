# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'random_password.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Random_password(object):
    def setupUi(self, Random_password):
        if not Random_password.objectName():
            Random_password.setObjectName(u"Random_password")
        Random_password.resize(550, 283)
        Random_password.setMinimumSize(QSize(425, 215))
        Random_password.setSizeIncrement(QSize(0, 0))
        self.window = QWidget(Random_password)
        self.window.setObjectName(u"window")
        self.window.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.window)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lenghtEdit = QLineEdit(self.window)
        self.lenghtEdit.setObjectName(u"lenghtEdit")

        self.horizontalLayout.addWidget(self.lenghtEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.window)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.window)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.button_copy = QPushButton(self.window)
        self.button_copy.setObjectName(u"button_copy")

        self.horizontalLayout_2.addWidget(self.button_copy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_letters = QPushButton(self.window)
        self.button_letters.setObjectName(u"button_letters")
        self.button_letters.setCheckable(True)
        self.button_letters.setChecked(True)

        self.horizontalLayout_3.addWidget(self.button_letters)

        self.button_numbers = QPushButton(self.window)
        self.button_numbers.setObjectName(u"button_numbers")
        self.button_numbers.setCheckable(True)
        self.button_numbers.setChecked(True)

        self.horizontalLayout_3.addWidget(self.button_numbers)

        self.button_signs = QPushButton(self.window)
        self.button_signs.setObjectName(u"button_signs")
        self.button_signs.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.button_signs)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        Random_password.setCentralWidget(self.window)

        self.retranslateUi(Random_password)

        QMetaObject.connectSlotsByName(Random_password)
    # setupUi

    def retranslateUi(self, Random_password):
        Random_password.setWindowTitle(QCoreApplication.translate("Random_password", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0445 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.label.setText(QCoreApplication.translate("Random_password", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432 \u043f\u0430\u0440\u043e\u043b\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("Random_password", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.button_copy.setText(QCoreApplication.translate("Random_password", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.button_letters.setText(QCoreApplication.translate("Random_password", u"Abc", None))
        self.button_numbers.setText(QCoreApplication.translate("Random_password", u"123", None))
        self.button_signs.setText(QCoreApplication.translate("Random_password", u"!@#", None))
    # retranslateUi

