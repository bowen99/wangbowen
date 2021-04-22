from PyQt5.Qt import *
import sys


class windows(QWidget):
    def __init__(self):
        super(windows, self).__init__()
        self.setWindowTitle('')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.lb()

    def lb(self):
        with open("ob.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        obj = QPushButton(self)
        obj.setObjectName("lab1")
        obj.setProperty("lv1", "normal")
        obj.setText("ee")
        # obj.setStyleSheet("font-size: 18px;color:red")


'''
    def lb(self):
        obj = QObject()
        obj.setObjectName("notice")
        obj.setProperty("notice_lever1", "yy")
        obj.setProperty("notice_lever2", "er")
        s = obj.property("notice_lever1")
        if s == "yyy":
            print("true")
        else:
            print("false")
        print(obj.dynamicPropertyNames())
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = windows()
    ui.show()
    sys.exit(app.exec_())
