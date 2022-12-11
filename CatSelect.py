import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRubberBand
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRect, QSize


class ROISelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Region of Interest Selector')
        self.resize(400, 300)

        # Load the cat picture and add it to a QLabel widget
        self.cat_label = QLabel(self)
        pixmap = QPixmap('cat.jpg')
        self.cat_label.setPixmap(pixmap)
        self.cat_label.resize(pixmap.size())

        # Create a QRubberBand object and set its color to red
        self.roi_rubberband = QRubberBand(QRubberBand.Rectangle, self)
        self.roi_color = Qt.red

    def mousePressEvent(self, event):
        # Set the starting position for the rubber band when the user clicks the mouse
        self.roi_start_pos = event.pos()
        self.roi_rubberband.setGeometry(QRect(self.roi_start_pos, QSize()))
        self.roi_rubberband.show()

    def mouseMoveEvent(self, event):
        # Update the size of the rubber band as the user moves the mouse
        self.roi_rubberband.setGeometry(
            QRect(self.roi_start_pos, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        # Set the final size of the rubber band when the user releases the mouse button
        self.roi_rubberband.setGeometry(
            QRect(self.roi_start_pos, event.pos()).normalized())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    roi_selector = ROISelector()
    roi_selector.show()
    sys.exit(app.exec_())
