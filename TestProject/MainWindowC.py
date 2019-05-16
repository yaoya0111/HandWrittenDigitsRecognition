from PyQt5 import QtCore, QtWidgets
from Ui_MainWindow import Ui_MainWindow
import tensorflow as tf
from PIL import Image, ImageFilter
from numpy import array


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def clearBtn(self):
        QtCore.qDebug(str("clearBtn"))
        self.ui.widget.clearBitmap()

    def saveBtn(self):
        QtCore.qDebug(str("saveBtn"))
        self.ui.widget.saveBitmap()

    # 预测过程
    def recongBtn(self):
        QtCore.qDebug(str("recongBtn"))
        self.ui.widget.recongBitmap()
        # 打开自己的图片地址
        file_name = R"C:\Users\yaoya\AppData\Local\conda\conda\envs\tensorflow\tensorflow-mnist-tutorial\TestProject\pic.bmp"
        img = Image.open(file_name).convert('L')
        cvtValue = list(img.getdata())
        # 初始化图片的值，1表示纯白色，0表示纯黑色
        #resCvtValue = [(255 - x) * 1.0 / 255.0 for x in cvtValue]
        resCvtValue = [x / 255.0 for x in cvtValue]
        newShape = array(resCvtValue).reshape(28, 28, 1)

        count = 0
        for pixel in resCvtValue:
            print(pixel, end="  ")
            count += 1
            if count == 28:
                print("\n")
                count = 0

        # 加载保存的参数
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            new_saver = tf.train.import_meta_graph(
                R'C:\Users\yaoya\AppData\Local\conda\conda\envs\tensorflow\tensorflow-mnist-tutorial\TestProject\mdlib\md2\init-1000.meta')
            new_saver.restore(sess, tf.train.latest_checkpoint(
                R'C:\Users\yaoya\AppData\Local\conda\conda\envs\tensorflow\tensorflow-mnist-tutorial\TestProject\mdlib\md2'))
            print("model restore done\n")
            graph = tf.get_default_graph()

            # input_X = graph.get_tensor_by_name("input_feed:0")

            '''
            # model 1
            W = graph.get_tensor_by_name("W:0")
            b = graph.get_tensor_by_name("b:0")
            XX = tf.reshape(newShape, [-1, 784])
            Y = tf.nn.softmax(tf.matmul(tf.cast(XX, tf.float32), W) + b)

            feed_dict = {XX: [resCvtValue]}
            '''

            # model 2
            #X = tf.placeholder(tf.float32, [None, 28, 28, 1])
            L = 200
            M = 100
            N = 60
            O = 30
            XX = tf.reshape(newShape, [-1, 784])
            W1 = graph.get_tensor_by_name("W1:0")
            B1 = graph.get_tensor_by_name("B1:0")

            W2 = graph.get_tensor_by_name("W2:0")
            B2 = graph.get_tensor_by_name("B2:0")

            W3 = graph.get_tensor_by_name("W3:0")
            B3 = graph.get_tensor_by_name("B3:0")

            W4 = graph.get_tensor_by_name("W4:0")
            B4 = graph.get_tensor_by_name("B4:0")

            W5 = graph.get_tensor_by_name("W5:0")
            B5 = graph.get_tensor_by_name("B5:0")

            Y1 = tf.nn.sigmoid(tf.matmul(tf.cast(XX, tf.float32), W1) + B1)
            Y2 = tf.nn.sigmoid(tf.matmul(Y1, W2) + B2)
            Y3 = tf.nn.sigmoid(tf.matmul(Y2, W3) + B3)
            Y4 = tf.nn.sigmoid(tf.matmul(Y3, W4) + B4)
            Ylogits = tf.matmul(Y4, W5) + B5
            Y = tf.nn.softmax(Ylogits)
            feed_dict = {XX: [resCvtValue]}

            '''
            # model 3
            X = tf.placeholder(tf.float32, [None, 28, 28, 1])
            K = 4  # first convolutional layer output depth
            L = 8  # second convolutional layer output depth
            M = 12  # third convolutional layer
            N = 200  # fully connected layer

            W1 = graph.get_tensor_by_name("W1:0")
            B1 = graph.get_tensor_by_name("B1:0")
            stride = 1  # output is 28x28
            Y1 = tf.nn.relu(tf.nn.conv2d(
                X, W1, strides=[1, stride, stride, 1], padding='SAME') + B1)

            W2 = graph.get_tensor_by_name("W2:0")
            B2 = graph.get_tensor_by_name("B2:0")
            stride = 2  # output is 14x14
            Y2 = tf.nn.relu(tf.nn.conv2d(Y1, W2, strides=[
                            1, stride, stride, 1], padding='SAME') + B2)

            W3 = graph.get_tensor_by_name("W3:0")
            B3 = graph.get_tensor_by_name("B3:0")

            stride = 2  # output is 7x7
            Y3 = tf.nn.relu(tf.nn.conv2d(Y2, W3, strides=[
                            1, stride, stride, 1], padding='SAME') + B3)

            # reshape the output from the third convolution for the fully connected layer
            YY = tf.reshape(Y3, shape=[-1, 7 * 7 * M])

            W4 = graph.get_tensor_by_name("W4:0")
            B4 = graph.get_tensor_by_name("B4:0")
            Y4 = tf.nn.relu(tf.matmul(YY, W4) + B4)

            W5 = graph.get_tensor_by_name("W5:0")
            B5 = graph.get_tensor_by_name("B5:0")

            Ylogits = tf.matmul(Y4, W5) + B5
            Y = tf.nn.softmax(Ylogits)

            feed_dict = {X: [newShape]}
            
            '''
            #sess.run(tf.global_variables_initializer())
            prediction = sess.run(Y, feed_dict)
            print(prediction)
            res = sess.run(tf.argmax(prediction, 1))
        self.ui.result.setText(str(res))

    def setLabelText(self, text):
        self.ui.result.setText(text)

    def setBitmapSize(self, size):
        self.ui.widget.setBitmapSize(size)
