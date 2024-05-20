from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QLabel,QFileDialog,QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
import sys
import json
from PyQt6.QtWidgets import QMessageBox

class Settings(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")  # Set your window title
        self.setGeometry(100,100,400,100)
        self.setWindowIcon(QIcon('icons/logo.png'))
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        # Create buttons

        # Define the size of the buttons
        button_size = QSize(50, 20)  # Adjust the size as needed
        icon_size = QSize(10, 10)


        self.input_select = QLineEdit()
        self.input_select.setPlaceholderText('Enter Path')
        # Create buttons and set their size
        self.save_button = QPushButton('Save')
        self.save_button.setIcon(QIcon('icons/user.png'))
        self.save_button.setFixedSize(button_size)
        self.save_button.setIconSize(icon_size)
        self.save_button.clicked.connect(lambda: self.save_path_to_json(self.input_select.text()))
        self.save_button.setEnabled(False)

        self.input_select_data = QLineEdit()
        self.input_select_data.setPlaceholderText('Enter Data Path')
        self.save_button_data = QPushButton('Save')
        self.save_button_data.setIcon(QIcon('icons/user.png'))
        self.save_button_data.setFixedSize(button_size)
        self.save_button_data.setIconSize(icon_size)
        self.save_button_data.clicked.connect(lambda: self.save_data_path_to_json(self.input_select_data.text()))
        self.save_button_data.setEnabled(False)


        self.path_label = QLabel("Select recording Path:")
        self.select_button = QPushButton('Select')
        self.select_button.setIcon(QIcon('icons/folder.png'))
        self.select_button.setFixedSize(button_size)
        self.select_button.setIconSize(icon_size)
        self.select_button.setToolTip('Select the path where the recordings will be saved')
        self.select_button.clicked.connect(self.choose_file_path)

        self.path_label_data = QLabel("Select Data Path:")
        self.select_button_data = QPushButton('Select')
        self.select_button_data.setIcon(QIcon('icons/folder.png'))
        self.select_button_data.setFixedSize(button_size)
        self.select_button_data.setIconSize(icon_size)
        self.select_button_data.setToolTip('Select the path where the data will be saved')
        self.select_button_data.clicked.connect(self.set_data_file_path)
        

        layout.addWidget(self.path_label,0,0,1,2)
        layout.addWidget(self.select_button,1,3)
        layout.addWidget(self.input_select,1,0,1,2)
        layout.addWidget(self.save_button,2,0)
        layout.addWidget(self.path_label_data,3,0,1,2)
        layout.addWidget(self.select_button_data,4,3)
        layout.addWidget(self.input_select_data,4,0,1,2)
        layout.addWidget(self.save_button_data,5,0)

        self.setLayout(layout)
        

    def choose_file_path(self):
        try:
            file_path = QFileDialog.getExistingDirectory(self, 'Select Directory')
            self.input_select.setText(file_path)
            self.save_button.setEnabled(True)
        except Exception as e:
            QMessageBox.warning(self, 'Error', f"An error occurred: {e}")
        
    def save_path_to_json(self, file_path):
        data = {'path': file_path}
        with open(r'datas\path.json', 'w') as json_file:
            json.dump(data, json_file)
        QMessageBox.information(self, 'Information', 'Path saved successfully')  # Fix: Indent the line to match the surrounding code
    
    def set_data_file_path(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, 'Select File')
            if file_path:  # Check if a file was selected
                self.input_select_data.setText(file_path)
                self.save_button_data.setEnabled(True)
        except Exception as e:
            QMessageBox.warning(self, 'Error', f"An error occurred: {e}")

    def save_data_path_to_json(self, data_path):
        data = {"data_path": data_path}
        with open(r"datas\settings.json", "w") as file:
            json.dump(data, file)
        QMessageBox.information(self, 'Information', 'Data path saved successfully')

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    
    ex = Settings()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()