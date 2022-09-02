# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrimeiraTela.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QPushButton


class Ui_PrimeiraTela(object):
    bt_cadrastrar_usuario: QPushButton

    def setupUi(self, PrimeiraTela):
        if not PrimeiraTela.objectName():
            PrimeiraTela.setObjectName(u"PrimeiraTela")
        PrimeiraTela.setWindowModality(Qt.WindowModal)
        PrimeiraTela.setEnabled(True)
        PrimeiraTela.resize(644, 507)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PrimeiraTela.sizePolicy().hasHeightForWidth())
        PrimeiraTela.setSizePolicy(sizePolicy)
        PrimeiraTela.setMinimumSize(QSize(0, 507))
        PrimeiraTela.setMaximumSize(QSize(674, 507))
        PrimeiraTela.setSizeIncrement(QSize(10, 0))
        PrimeiraTela.setCursor(QCursor(Qt.ArrowCursor))
        PrimeiraTela.setContextMenuPolicy(Qt.CustomContextMenu)
        PrimeiraTela.setWindowTitle(u"MainWindow")
#if QT_CONFIG(whatsthis)
        PrimeiraTela.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        PrimeiraTela.setAutoFillBackground(False)
        PrimeiraTela.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 0);")
        self.centralwidget = QWidget(PrimeiraTela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(644, 498))
        self.centralwidget.setMaximumSize(QSize(644, 498))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 30, 626, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 571, 37))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.layoutWidget)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_home.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.btn_home.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_home.setLayoutDirection(Qt.RightToLeft)
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.btn_home.setAutoDefault(False)
        self.btn_home.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_import = QPushButton(self.layoutWidget)
        self.btn_import.setObjectName(u"btn_import")
        sizePolicy.setHeightForWidth(self.btn_import.sizePolicy().hasHeightForWidth())
        self.btn_import.setSizePolicy(sizePolicy)
        self.btn_import.setFont(font)
#if QT_CONFIG(tooltip)
        self.btn_import.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_import.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.btn_import.setAutoDefault(False)
        self.btn_import.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_import)

        self.btn_table = QPushButton(self.layoutWidget)
        self.btn_table.setObjectName(u"btn_table")
        sizePolicy.setHeightForWidth(self.btn_table.sizePolicy().hasHeightForWidth())
        self.btn_table.setSizePolicy(sizePolicy)
        self.btn_table.setFont(font)
#if QT_CONFIG(tooltip)
        self.btn_table.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_table.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.btn_table.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.btn_table.setAutoDefault(False)
        self.btn_table.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_table)

        self.btn_sobre = QPushButton(self.layoutWidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_sobre.sizePolicy().hasHeightForWidth())
        self.btn_sobre.setSizePolicy(sizePolicy)
        self.btn_sobre.setSizeIncrement(QSize(500, 500))
        self.btn_sobre.setBaseSize(QSize(500, 500))
        self.btn_sobre.setFont(font)
#if QT_CONFIG(tooltip)
        self.btn_sobre.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_sobre.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.btn_sobre.setAutoDefault(False)
        self.btn_sobre.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.layoutWidget)
        self.btn_contato.setObjectName(u"btn_contato")
        sizePolicy.setHeightForWidth(self.btn_contato.sizePolicy().hasHeightForWidth())
        self.btn_contato.setSizePolicy(sizePolicy)
        self.btn_contato.setMaximumSize(QSize(500, 500))
        self.btn_contato.setSizeIncrement(QSize(4500, 500))
        self.btn_contato.setBaseSize(QSize(500, 500))
        self.btn_contato.setFont(font)
#if QT_CONFIG(tooltip)
        self.btn_contato.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_contato.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.btn_contato.setAutoDefault(False)
        self.btn_contato.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_contato)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setEnabled(True)
        self.Pages.setGeometry(QRect(9, 107, 626, 361))
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.Pages.setMinimumSize(QSize(0, 361))
        self.Pages.setMaximumSize(QSize(16777215, 361))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.Pages.setFont(font1)
        self.Pages.setAcceptDrops(False)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.pg_table.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pg_table.sizePolicy().hasHeightForWidth())
        self.pg_table.setSizePolicy(sizePolicy)
#if QT_CONFIG(tooltip)
        self.pg_table.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pg_table.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.pg_table.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.gridLayout_2 = QGridLayout(self.pg_table)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Estoque_Saida = QTabWidget(self.pg_table)
        self.Estoque_Saida.setObjectName(u"Estoque_Saida")
        self.Estoque_Saida.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Estoque_Saida.sizePolicy().hasHeightForWidth())
        self.Estoque_Saida.setSizePolicy(sizePolicy)
        self.Estoque_Saida.setTabletTracking(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_10.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_4.addWidget(self.label_17)

        self.treeWidget = QTreeWidget(self.tab)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.treeWidget)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_5.addWidget(self.label_16)

        self.treeWidget_3 = QTreeWidget(self.tab)
        self.treeWidget_3.setObjectName(u"treeWidget_3")

        self.verticalLayout_5.addWidget(self.treeWidget_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_10.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.Estoque_Saida.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_18.setFont(font2)
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(False)
        self.label_18.setOpenExternalLinks(False)

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")

        self.horizontalLayout_11.addWidget(self.pushButton_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setFont(font)

        self.gridLayout_3.addWidget(self.txt_filtro, 2, 0, 1, 1)

        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_3.addWidget(self.tableView, 3, 0, 1, 1)

        self.Estoque_Saida.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.Estoque_Saida, 0, 0, 1, 2)

        self.Pages.addWidget(self.pg_table)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.label_13 = QLabel(self.pg_contato)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        self.label_13.setGeometry(QRect(270, 10, 111, 20))
        self.label_13.setFont(font2)
        self.label_13.setScaledContents(False)
        self.label_13.setWordWrap(False)
        self.label_13.setOpenExternalLinks(False)
        self.layoutWidget1 = QWidget(self.pg_contato)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(140, 60, 371, 241))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_8.addWidget(self.label_25)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_8.addWidget(self.label_22)

        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_8.addWidget(self.label_23)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_8.addWidget(self.label_24)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.label_14 = QLabel(self.pg_sobre)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QRect(280, 10, 91, 41))
        self.label_14.setFont(font2)
        self.label_19 = QLabel(self.pg_sobre)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 80, 551, 221))
        self.label_19.setFont(font)
        self.Pages.addWidget(self.pg_sobre)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.pg_home.setEnabled(True)
#if QT_CONFIG(tooltip)
        self.pg_home.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pg_home.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.pg_home.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.gridLayout = QGridLayout(self.pg_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setStyleSheet(u"color: rgb(0, 85, 0);")
        self.label.setPixmap(QPixmap(u"../../../../../Downloads/A2B (2).png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.bt_cadrastrar_usuario = QPushButton(self.pg_home)
        self.bt_cadrastrar_usuario.setObjectName(u"bt_cadrastrar_usuario")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bt_cadrastrar_usuario.sizePolicy().hasHeightForWidth())
        self.bt_cadrastrar_usuario.setSizePolicy(sizePolicy3)
        self.bt_cadrastrar_usuario.setFont(font)
        self.bt_cadrastrar_usuario.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(tooltip)
        self.bt_cadrastrar_usuario.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.bt_cadrastrar_usuario.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.bt_cadrastrar_usuario.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}")
        self.bt_cadrastrar_usuario.setFlat(False)

        self.gridLayout.addWidget(self.bt_cadrastrar_usuario, 1, 0, 1, 1)

        self.Pages.addWidget(self.pg_home)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.label_2 = QLabel(self.pg_import)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 591, 51))
        self.label_12 = QLabel(self.pg_import)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(270, 80, 71, 81))
        self.label_12.setPixmap(QPixmap(u"../../../../../Downloads/1486505265-document-file-export-sending-exit-send_81434 (1).png"))
        self.layoutWidget2 = QWidget(self.pg_import)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(70, 180, 461, 32))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font3 = QFont()
        font3.setPointSize(8)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 85, 0);")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.ptn_open_2 = QPushButton(self.layoutWidget2)
        self.ptn_open_2.setObjectName(u"ptn_open_2")
        self.ptn_open_2.setFont(font)
        self.ptn_open_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 0);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.ptn_open_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.ptn_open_2)

        self.layoutWidget3 = QWidget(self.pg_import)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 330, 571, 25))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.pushButton = QPushButton(self.layoutWidget3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.label_15 = QLabel(self.layoutWidget3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.Pages.addWidget(self.pg_import)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_3 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.pg_cadastro)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_4.setFont(font4)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.pg_cadastro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setBold(False)
        font5.setWeight(50)
        self.txt_nome.setFont(font5)
        self.txt_nome.setStyleSheet(u"\n"
"QPushButton{\n"
"front-size: 16;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_nome)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_6.setFont(font6)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        sizePolicy1.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy1)
        self.txt_usuario.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setPointSize(10)
        self.txt_usuario.setFont(font7)

        self.horizontalLayout_5.addWidget(self.txt_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.txt_senha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.txt_senha_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetFixedSize)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy5)
        self.cb_perfil.setFont(font)
        self.cb_perfil.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.cb_perfil)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMaximumSize(QSize(1000, 16777215))
        self.btn_cadastrar.setSizeIncrement(QSize(30, 30))
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setBold(True)
        font8.setUnderline(False)
        font8.setWeight(75)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.btn_cadastrar.setFont(font8)
        self.btn_cadastrar.setMouseTracking(True)
#if QT_CONFIG(tooltip)
        self.btn_cadastrar.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"front-size: 16;\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:houver{background-color: #fff; color:black}\n"
"")
        self.btn_cadastrar.setInputMethodHints(Qt.ImhNone)
        self.btn_cadastrar.setAutoDefault(False)
        self.btn_cadastrar.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_cadastrar)

        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.Pages.addWidget(self.pg_cadastro)
        PrimeiraTela.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrimeiraTela)

        self.btn_home.setDefault(True)
        self.btn_import.setDefault(True)
        self.btn_table.setDefault(True)
        self.btn_sobre.setDefault(True)
        self.btn_contato.setDefault(True)
        self.Pages.setCurrentIndex(3)
        self.Estoque_Saida.setCurrentIndex(0)
        self.bt_cadrastrar_usuario.setDefault(True)
        self.ptn_open_2.setDefault(True)
        self.pushButton.setDefault(True)
        self.btn_cadastrar.setDefault(True)


        QMetaObject.connectSlotsByName(PrimeiraTela)
    # setupUi

    def retranslateUi(self, PrimeiraTela):
        self.btn_home.setText(QCoreApplication.translate("PrimeiraTela", u"HOME ", None))
        self.btn_import.setText(QCoreApplication.translate("PrimeiraTela", u"IMPORTAR", None))
        self.btn_table.setText(QCoreApplication.translate("PrimeiraTela", u"TABLE", None))
        self.btn_sobre.setText(QCoreApplication.translate("PrimeiraTela", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("PrimeiraTela", u"CONTATO", None))
        self.pushButton_5.setText(QCoreApplication.translate("PrimeiraTela", u"Importar ", None))
        self.pushButton_4.setText(QCoreApplication.translate("PrimeiraTela", u"Gerar Sa\u00edda", None))
        self.pushButton_3.setText(QCoreApplication.translate("PrimeiraTela", u"Entorno", None))
        self.label_17.setText(QCoreApplication.translate("PrimeiraTela", u"Estoque", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("PrimeiraTela", u"Sa\u00edda", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("PrimeiraTela", u"Requisi\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("PrimeiraTela", u"Usu\u00e1rio ", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("PrimeiraTela", u"Esp\u00e9cie", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("PrimeiraTela", u"Quantidade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("PrimeiraTela", u"Nota Fiscal", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("PrimeiraTela", u"Munic\u00edpio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("PrimeiraTela", u"UF", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("PrimeiraTela", u"ID", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("PrimeiraTela", u"Produto", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("PrimeiraTela", u"Cliente", None));
        self.label_16.setText(QCoreApplication.translate("PrimeiraTela", u"Sa\u00edda", None))
        ___qtreewidgetitem1 = self.treeWidget_3.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("PrimeiraTela", u"Usu\u00e1rio", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("PrimeiraTela", u"Data ", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("PrimeiraTela", u"ID", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("PrimeiraTela", u"Nota Fiscal", None));
        self.Estoque_Saida.setTabText(self.Estoque_Saida.indexOf(self.tab), QCoreApplication.translate("PrimeiraTela", u"Base", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("PrimeiraTela", u"<html><head/><body><p align=\"center\">Estoque </p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("PrimeiraTela", u"Gerar Excel", None))
        self.pushButton_2.setText(QCoreApplication.translate("PrimeiraTela", u"Gerar Gr\u00e1fico", None))
        self.txt_filtro.setText(QCoreApplication.translate("PrimeiraTela", u"Filtro", None))
        self.Estoque_Saida.setTabText(self.Estoque_Saida.indexOf(self.tab_2), QCoreApplication.translate("PrimeiraTela", u"Estoque", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("PrimeiraTela", u"Contatos", None))
        self.label_25.setText(QCoreApplication.translate("PrimeiraTela", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Desenvolvedora: Ana Karla Santana</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("PrimeiraTela", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Email:santanadeanakarla@gmail.com</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("PrimeiraTela", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Linkdin: in\\anakarlasantana</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("PrimeiraTela", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">GitHub: https://github.com/anakarlasantana</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("PrimeiraTela", u"SOBRE", None))
        self.label_19.setText(QCoreApplication.translate("PrimeiraTela", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">O A2B Estoque e Log\u00edstica foi criado com o intuito de facilitar o</span></p><p align=\"center\"><span style=\" font-size:11pt;\"> gerenciamento de estoque em armaz\u00e9m e no transporte log\u00edstico.</span></p></body></html>", None))
        self.label.setText("")
        self.bt_cadrastrar_usuario.setText(QCoreApplication.translate("PrimeiraTela", u"Cadastrar Usu\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("PrimeiraTela", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#005500;\">IMPORTAR XML</span></p></body></html>", None))
        self.label_12.setText("")
        self.ptn_open_2.setText(QCoreApplication.translate("PrimeiraTela", u"Abrir XML", None))
        self.label_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("PrimeiraTela", u"IMPORTAR", None))
        self.label_15.setText("")
        self.label_4.setText(QCoreApplication.translate("PrimeiraTela", u"CADRASTRO DE USU\u00c1RIO", None))
        self.label_5.setText(QCoreApplication.translate("PrimeiraTela", u"Nome:", None))
        self.label_6.setText(QCoreApplication.translate("PrimeiraTela", u"Usu\u00e1rio:", None))
        self.label_7.setText(QCoreApplication.translate("PrimeiraTela", u"Senha:", None))
        self.label_8.setText(QCoreApplication.translate("PrimeiraTela", u"Senha:", None))
        self.label_9.setText(QCoreApplication.translate("PrimeiraTela", u"Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("PrimeiraTela", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("PrimeiraTela", u"Administrador", None))

        self.label_10.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("PrimeiraTela", u"Cadastrar", None))
        self.label_11.setText("")
        pass
    # retranslateUi

