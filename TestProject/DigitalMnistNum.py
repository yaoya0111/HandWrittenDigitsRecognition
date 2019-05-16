# 定义手写数字面板类
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor


class DigitalMnistNum(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DigitalMnistNum, self).__init__(parent)
        self.pen = QtGui.QPen()
        self.pen.setStyle(QtCore.Qt.SolidLine)
        self.pen.setWidth(12)  # 笔的粗细
        self.pen.setColor(QtCore.Qt.white)  # 白色字体
        # 图片大小为28*28 pixel
        self.bitmapSize = QtCore.QSize(28, 28)
        self.resetBitmap()

    def resetBitmap(self):
        self.pix = QtGui.QBitmap(self.size())
        self.pix.fill(QtCore.Qt.black)  # 设置黑色背景

    # 清除按钮
    def clearBitmap(self):
        self.resetBitmap()
        self.update()
    # 保存图片格式以及图片信息

    def recongBitmap(self):
        pass

    def saveBitmap(self):
        fileName = str("pic.bmp")
        tmp = self.pix.scaled(
            self.bitmapSize, QtCore.Qt.KeepAspectRatio)  # 保存图片
        QtCore.qDebug(str(tmp.size()))
        tmp.save(fileName)

    def setBitmapSize(self, size):
        self.bitmapSize = QtCore.QSize(size[0], size[1])


# 以下三个函数为记录鼠标手写数字事件
    # 定义鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.startPos = event.pos()
            painter = QtGui.QPainter()
            painter.begin(self.pix)
            painter.setPen(self.pen)
            painter.drawPoint(self.startPos)
            painter.end()
        self.update()
    # 鼠标移动事件

    def mouseMoveEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self.pix)
        painter.setPen(self.pen)
        painter.drawLine(self.startPos, event.pos())
        painter.end()
        self.startPos = event.pos()
        self.update()
    # 鼠标画线事件

    def paintEvent(self, event):
        if self.size() != self.pix.size():
            QtCore.qDebug(str(self.size()) + "," +
                          str(self.pix.size()) + "," + str(event.type()))
            self.resetBitmap()
        painter = QtGui.QPainter(self)
        painter.drawPixmap(QtCore.QPoint(0, 0), self.pix)
    # 鼠标释放事件

    def mouseReleaseEvent(self, event):
        self.update()
