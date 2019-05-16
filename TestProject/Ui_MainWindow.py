from PyQt5 import QtCore, QtGui, QtWidgets
# DigitalMnistNum为数字画板的子类
from DigitalMnistNum import DigitalMnistNum


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 200)  # 主窗口大小
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = DigitalMnistNum(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 140, 140))  # 画布用140*140
        self.widget.setObjectName("widget")
        # 修改右侧布局
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 20, 105, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.clearBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clearBtn.setObjectName("clearBtn")
        self.verticalLayout.addWidget(self.clearBtn)

        self.saveBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveBtn.setObjectName("saveBtn")
        self.verticalLayout.addWidget(self.saveBtn)

        self.recongBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.recongBtn.setObjectName("recongBtn")
        self.verticalLayout.addWidget(self.recongBtn)
        self.result = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(70)
        # 结果显示区域
        self.result.setFont(font)
        self.result.setObjectName("res")
        self.verticalLayout.addWidget(self.result)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.clearBtn.clicked.connect(MainWindow.clearBtn)
        self.saveBtn.clicked.connect(MainWindow.saveBtn)
        self.recongBtn.clicked.connect(MainWindow.recongBtn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearBtn.setText(_translate("MainWindow", "clear"))
        self.saveBtn.setText(_translate("MainWindow", "save"))
        self.recongBtn.setText(_translate("MainWindow", "recog"))
        self.result.setText(_translate("MainWindow", "res"))
