import sys
from time import sleep

from astropy import units
from PySide6 import QtCore, QtWidgets

from astropy.units import imperial
imperial.enable()


class Calculation(QtCore.QObject):
    finished = QtCore.Signal(str)
    progress = QtCore.Signal(int)

    def __init__(self, value, in_unit, out_unit) -> None:
        super().__init__()
        self.value = value
        self.in_unit = in_unit
        self.out_unit = out_unit

    def run(self):
        """Long-running task."""
        for i in range(5):
            sleep(1)
            self.progress.emit(i + 1)

        try:
            in_quantity = units.Quantity(self.value, self.in_unit)
            out_quantity = in_quantity.to(self.out_unit)
        except Exception as ex:
            self.finished.emit(f"Error: {ex}.")
            return

        self.finished.emit(f"Result: {out_quantity}")


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Unit converter")

        self._setupWidgets()
        self._setupEvents()
        self._setupMenu()

    def _setupWidgets(self):
        central_widget = QtWidgets.QWidget(self)        

        layout = QtWidgets.QVBoxLayout()  

        self.result = QtWidgets.QLabel("Result: ", central_widget)
        self.button = QtWidgets.QPushButton("Calculate!", central_widget)
        self.value = QtWidgets.QLineEdit(self)
        self.value.setText("1.0")
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setMaximum(5)

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
        layout.addWidget(self.progress)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    @QtCore.Slot()
    def show_result(self, text):
        self.result.setText(text)

    @QtCore.Slot()
    def start_calculation(self):
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

        self.button.setEnabled(False)
        self.thread = QtCore.QThread()
        self.worker = Calculation(value, in_unit, out_unit)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.progress.setValue)
        self.worker.finished.connect(self.result.setText)
        self.worker.finished.connect(lambda _: self.progress.setValue(0))
        self.worker.finished.connect(lambda _: self.button.setEnabled(True))
        self.thread.start()

    def _setupEvents(self):
        self.button.clicked.connect(self.start_calculation)

    def _setupMenu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("Exit", self.close)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Window()
    window.show()

    sys.exit(app.exec_())