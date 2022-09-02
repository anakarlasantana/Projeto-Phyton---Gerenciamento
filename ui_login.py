# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(409, 484)
        Login.setWindowTitle(u"Login")
        Login.setLayoutDirection(Qt.LeftToRight)
        Login.setAutoFillBackground(False)
        Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAcceptDrops(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        self.logo.setGeometry(QRect(10, 40, 371, 131))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMaximumSize(QSize(371, 131))
        self.logo.setInputMethodHints(Qt.ImhExclusiveInputMask)
        self.logo.setPixmap(QPixmap(u"../../../../../Downloads/A2B (3).png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignCenter)
        self.icone1 = QLabel(self.frame)
        self.icone1.setObjectName(u"icone1")
        self.icone1.setEnabled(False)
        self.icone1.setGeometry(QRect(160, 180, 71, 81))
        sizePolicy1.setHeightForWidth(self.icone1.sizePolicy().hasHeightForWidth())
        self.icone1.setSizePolicy(sizePolicy1)
        self.icone1.setMaximumSize(QSize(71, 81))
        self.icone1.setAcceptDrops(False)
        self.icone1.setAutoFillBackground(False)
        self.icone1.setPixmap(QPixmap(u"../../../../../Downloads/user.png"))
        self.icone1.setScaledContents(True)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 300, 152, 77))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_user = QLineEdit(self.layoutWidget)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_user.sizePolicy().hasHeightForWidth())
        self.btn_user.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_user.setFont(font)
        self.btn_user.setMouseTracking(False)
        self.btn_user.setFocusPolicy(Qt.StrongFocus)
        self.btn_user.setAcceptDrops(False)
        self.btn_user.setAutoFillBackground(False)
        self.btn_user.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")
        self.btn_user.setFrame(True)
        self.btn_user.setAlignment(Qt.AlignCenter)
        self.btn_user.setPlaceholderText(u"User")
        self.btn_user.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.btn_user.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.btn_user)

        self.btn_passaword = QLineEdit(self.layoutWidget)
        self.btn_passaword.setObjectName(u"btn_passaword")
        self.btn_passaword.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_passaword.sizePolicy().hasHeightForWidth())
        self.btn_passaword.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.btn_passaword.setFont(font1)
        self.btn_passaword.setMouseTracking(False)
        self.btn_passaword.setAcceptDrops(False)
        self.btn_passaword.setToolTipDuration(-1)
        self.btn_passaword.setAutoFillBackground(False)
        self.btn_passaword.setEchoMode(QLineEdit.Password)
        self.btn_passaword.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.btn_passaword)

        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy3)
        self.btn_login.setFont(font)
        self.btn_login.setMouseTracking(False)
        self.btn_login.setAcceptDrops(False)
#if QT_CONFIG(accessibility)
        self.btn_login.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_login.setAutoFillBackground(False)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")
        self.btn_login.setAutoDefault(True)
        self.btn_login.setFlat(True)

        self.verticalLayout.addWidget(self.btn_login)

        self.layoutWidget.raise_()
        self.logo.raise_()
        self.icone1.raise_()

        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Login)

        self.btn_login.setDefault(True)


        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        self.logo.setText("")
#if QT_CONFIG(accessibility)
        self.icone1.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.icone1.setText("")
#if QT_CONFIG(tooltip)
        self.btn_passaword.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_passaword.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.btn_passaword.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.btn_passaword.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Entrar", None))
        pass
    # retranslateUi

