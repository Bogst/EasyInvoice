import random

from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from pathing import resource_path


class SplashScreen(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.title = "Splash Screen"
        if random.randint(0, 100) == 10:
            self.splash_image_path = "./resources/img/Maya.jpg"
        else:
            self.splash_image_path = "./resources/img/SplashScreen.jpg"
        self.start_btn = QPushButton("Factura Noua")
        self.initUI()
        self.main_window = main_window

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(QSize(400, 600))
        background_image = QImage(resource_path(self.splash_image_path)).scaled(QSize(400, 600))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_image))
        self.setPalette(palette)

        hbox = QVBoxLayout()
        hbox.addStretch()

        self.start_btn.clicked.connect(self.on_click)
        self.start_btn.setMinimumSize(50, 50)
        hbox.addWidget(self.start_btn)

        self.setLayout(hbox)

    @pyqtSlot()
    def on_click(self):
        self.main_window.show()
        self.hide()

