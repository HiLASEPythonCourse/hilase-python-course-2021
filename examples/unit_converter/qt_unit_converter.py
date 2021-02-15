import sys

from astropy import units
from PySide6 import QtCore, QtWidgets

from astropy.units import imperial
imperial.enable()


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Unit converter")

        self._setupWidgets()
        self._setupEvents()
        self._setupMenu()

        self.calculate()

    def _setupWidgets(self):
        central_widget = QtWidgets.QWidget(self)        

        layout = QtWidgets.QVBoxLayout()
        

        self.result = QtWidgets.QLabel("Result: ", central_widget)
        self.button = QtWidgets.QPushButton("Calculate!", central_widget)
        self.value = QtWidgets.QLineEdit(self)
        self.value.setText("1.0")

        self.in_unit = QtWidgets.QLineEdit(self)
        self.in_unit.setText("ft")

        self.out_unit = QtWidgets.QLineEdit(self)
        self.out_unit.setText("m")

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Value", self.value)
        form_layout.addRow("From", self.in_unit)
        form_layout.addRow("To", self.out_unit)
        form_widget = QtWidgets.QWidget(self)
        form_widget.setLayout(form_layout)

        layout.addWidget(form_widget)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    @QtCore.Slot()
    def calculate(self):
        try:
            value = float(self.value.text())
        except:
            self.result.setText(f"Invalid input.")
            return

        try:
            in_unit = units.Unit(self.in_unit.text())
        except:
            self.result.setText(f"Invalid input unit.")
            return

        try:
            out_unit = units.Unit(self.out_unit.text())
        except:
            self.result.setText(f"Invalid output unit.")
            return

        try:
            in_quantity = units.Quantity(value, in_unit)
            out_quantity = in_quantity.to(out_unit)
        except Exception as ex:
            self.result.setText(f"Error: {ex}.")
            return

        self.result.setText(f"Result: {out_quantity}")


    def _setupEvents(self):
        self.button.clicked.connect(self.calculate)

    def _setupMenu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("Exit", self.close)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Window()
    window.show()

    sys.exit(app.exec_())