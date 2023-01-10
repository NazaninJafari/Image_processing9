from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Colorpicker(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        
        self.ui.RedSlider.valueChanged.connect(self.getValue)
        self.ui.GreenSlider.valueChanged.connect(self.getValue)
        self.ui.BlueSlider.valueChanged.connect(self.getValue)

    def getValue(self):
        self.red = self.ui.RedSlider.value()
        self.green = self.ui.GreenSlider.value()
        self.blue = self.ui.BlueSlider.value()
        
        self.ui.red_value.setText(str(self.red))
        self.ui.green_value.setText(str(self.green))
        self.ui.blue_value.setText(str(self.blue))
        #self.rgb_colorbutton()

        #self.ui.pushButton.setStyleSheet(f'rgb({self.red},{self.green},{self.blue})')
        self.ui.pushButton.setStyleSheet(f'background-color: rgb({self.red}, {self.green}, {self.blue})')
        self.ui.pushButton.setText(f'rgb({self.red}, {self.green}, {self.blue})')


app = QApplication([])
window = Colorpicker()
app.exec_()