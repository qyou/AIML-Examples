'''
@author: summer
'''
import sys
from PySide import QtGui
import ui_MainWidget

class Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.widget = ui_MainWidget.Ui_Form()
        self.widget.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    form = Widget()
    form.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()