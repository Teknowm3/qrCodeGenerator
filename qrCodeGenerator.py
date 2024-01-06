import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
import qrcode

class QRCodeWindow(QWidget):
    def __init__(self, url):
        super().__init__()

        self.url = url
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QR Code Window")

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")

        pixmap = QPixmap("qrcode.png")
        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)

        self.show()

def main():
    url = "https://www.canva.com/design/FAF4irjbChs/ZxIQq45J5Xf43IZQOxopAB/view?utm_content=DAF4irjbvhs&utm_campaign=designshare&utm_medium=link&utm_source=editor"

    app = QApplication(sys.argv)
    window = QRCodeWindow(url)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
