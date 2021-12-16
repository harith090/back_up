import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
  
class Window(QWidget):
  
    # method called by timer
    def showTime(self):
  
        # getting current time
        current_time = QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
  
        # showing it to the label
        self.label.setText(label_time)
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# showing all the widgets
window.show()
  
# start the app
App.exit(App.exec_())