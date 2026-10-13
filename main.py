import sys
from password_generator import password_generator, letters, numbers, signs

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_Random_password
from PySide6.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_Random_password()
        self.ui.setupUi(self)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QLabel {
                color: #cdd6f4;
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #313244;
                color: #cdd6f4;
                border: 2px solid #45475a;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #89b4fa;
            }
            QPushButton {
                background-color: #89b4fa;
                color: #1e1e2e;
                border: none;
                border-radius: 8px;
                padding: 10px 16px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #b4d0ff;
            }
            QPushButton:pressed {
                background-color: #6c9ae8;
            }
            QPushButton:checked {
                 background-color: #a6e3a1;
                 color: #1e1e2e;
                 border: 2px solid #ffffff;
}
        """)

        self.ui.lenghtEdit.setText("16")
        self.ui.pushButton.clicked.connect(self.generate)
        self.ui.button_copy.clicked.connect(self.get_copy)

    def generate(self):
        try:
            lenght = int(self.ui.lenghtEdit.text())
        except ValueError:
            self.ui.lenghtEdit.setText("Введите число!")
            return

        if lenght <= 0:
            self.ui.lenghtEdit.setText("Длина должна быть больше 0")
            return
        elif lenght > 64:
            self.ui.lenghtEdit.setText("Не превышай 64 знака")
            return

        groups = []
        if self.ui.button_letters.isChecked():
            groups.append(letters)
        if self.ui.button_numbers.isChecked():
            groups.append(numbers)
        if self.ui.button_signs.isChecked():
            groups.append(signs)

        if not groups:
            self.ui.lineEdit.setText("Выберите хотя бы один тип символов!")
            return

        password = password_generator(lenght, *groups)
        self.ui.lineEdit.setText(password)

    def get_copy(self):
        password = self.ui.lineEdit.text()
        if not password:
            return
        QApplication.clipboard().setText(password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    window = App()
    window.show()

    sys.exit(app.exec())
