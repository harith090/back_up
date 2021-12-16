from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime,Qt
import pickle

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlag(Qt.FramelessWindowHint)
        timer = QTimer(Form)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(640, 480))
        Form.setStyleSheet("background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.175, fx:0.5, fy:0.5, stop:0 rgba(129, 186, 255, 255), stop:1 rgba(0, 7, 50, 255))")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temperature = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("IrisUPC")
        font.setPointSize(96)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("background-color: rgb(0,0,0,40);color:white;border-radius: 25px;")
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName("temperature")
        self.horizontalLayout.addWidget(self.temperature)
        self.AirVelocity = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("IrisUPC")
        font.setPointSize(96)
        self.AirVelocity.setFont(font)
        self.AirVelocity.setStyleSheet("background-color: rgb(0,0,0,40);color:white;border-radius: 25px;")
        self.AirVelocity.setAlignment(QtCore.Qt.AlignCenter)
        self.AirVelocity.setObjectName("AirVelocity")
        self.horizontalLayout.addWidget(self.AirVelocity)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ShowTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("IrisUPC")
        font.setPointSize(48)
        self.ShowTime.setFont(font)
        self.ShowTime.setStyleSheet("background:transparent;color:white")
        self.ShowTime.setAlignment(QtCore.Qt.AlignCenter)
        self.ShowTime.setObjectName("ShowTime")
        self.verticalLayout_3.addWidget(self.ShowTime)
        self.ShowDate = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("IrisUPC")
        font.setPointSize(48)
        self.ShowDate.setFont(font)
        self.ShowDate.setStyleSheet("background:transparent;color:white")
        self.ShowDate.setAlignment(QtCore.Qt.AlignCenter)
        self.ShowDate.setObjectName("ShowDate")
        self.verticalLayout_3.addWidget(self.ShowDate)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        file = open('data.ob','rb')
        data = pickle.load(file)

        current_time = QDateTime.currentDateTime()
        label_date = current_time.toString('d - M - yyyy')
        label_time = current_time.toString('hh : mm : ss')

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.temperature.setText(_translate("Form", "<html><head/><body><p>" + str(data["Temperature"]) + " °C</p></body></html>"))
        self.AirVelocity.setText(_translate("Form", str(data["AirVelocity"]) + " m/s"))
        self.ShowTime.setText(_translate("Form", label_time))
        self.ShowDate.setText(_translate("Form", label_date))

    def showTime(self):
        file = open('data.ob','rb')
        data = pickle.load(file)

        current_time = QDateTime.currentDateTime()
        label_date = current_time.toString('d - M - yyyy')
        label_time = current_time.toString('hh : mm : ss')
        self.ShowDate.setText(label_date)
        self.ShowTime.setText(label_time)

        self.temperature.setText(str(data["Temperature"]) + " °C")
        self.AirVelocity.setText(str(data["AirVelocity"]) + " m/s")
        
        #print(label_date, label_time)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
