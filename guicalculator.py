from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Pencere(QWidget):
    def __init__(self):
        self.islem=""
        super().__init__()
        self.setUI()
    def setUI(self):
        self.setWindowTitle("Hesap Makinası")
        self.yazi1=QLabel("Sayi 1:")
        self.yazi2=QLabel("Sayi 2:")
        self.sonuc=QLabel("")
        self.temizle=QPushButton("Temizle")
        self.sonuc.setAlignment(Qt.AlignCenter)

        self.giris1=QLineEdit()
        self.giris2=QLineEdit()

        self.topla=QPushButton("+")
        self.cikarma=QPushButton("-")
        self.carpma=QPushButton("*")
        self.bolme=QPushButton("/")

        self.topla.setFont(QFont("Arial",15,QFont.Bold))
        self.cikarma.setFont(QFont("Arial",15,QFont.Bold))
        self.carpma.setFont(QFont("Arial",15,QFont.Bold))
        self.bolme.setFont(QFont("Arial",15,QFont.Bold))

        self.button=QPushButton("Hesapla")

        h_box=QHBoxLayout()
        h_box_islemler=QHBoxLayout()
        h_box2=QHBoxLayout()

        h_box_islemler.addWidget(self.topla)
        h_box_islemler.addWidget(self.cikarma)
        h_box_islemler.addWidget(self.carpma)
        h_box_islemler.addWidget(self.bolme)
        h_box.addWidget(self.yazi1)
        h_box.addWidget(self.giris1)

        h_box2.addWidget(self.yazi2)
        h_box2.addWidget(self.giris2)

        v_box=QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.sonuc)
        v_box.addLayout(h_box_islemler)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.button)

        self.topla.clicked.connect(self.tp)
        self.cikarma.clicked.connect(self.ck)
        self.carpma.clicked.connect(self.cp)
        self.bolme.clicked.connect(self.bl)

        self.button.clicked.connect(self.uygulama)
        self.temizle.clicked.connect(self.tz)
        
        self.setLayout(v_box)
        self.show()
    def tz(self):
        self.giris1.clear()
        self.giris2.clear()
    def tp(self):
        self.islem="+"
    def ck(self):
        self.islem="-"
    def cp(self):
        self.islem="*"
    def bl(self):
        self.islem="/"
    def uygulama(self):
        if self.islem == "+":
            try:
                giris1=int(self.giris1.text())
                giris2=int(self.giris2.text())
                sonuc=giris1+giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris2.clear()
        if self.islem == "-":
            try:
                giris1=int(self.giris1.text())
                giris2=int(self.giris2.text())
                sonuc=giris1-giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris2.clear()
        if self.islem == "*":
            try:
                giris1=int(self.giris1.text())
                giris2=int(self.giris2.text())
                sonuc=giris1*giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris2.clear()
        if self.islem == "/":
            try:
                giris1=int(self.giris1.text())
                giris2=int(self.giris2.text())
                sonuc=giris1/giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris2.clear()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())