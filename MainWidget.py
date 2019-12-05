#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QKeyEvent, QPixmap
from PySide2.QtCore import Qt, Slot

from Ui_MainWidget import Ui_MainWidget

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        else:
            event.ignore()

    @Slot()
    def update_image(self):
        if os.path.isfile('foo.txt.png'):
            self.ui.label.setPixmap(QPixmap('foo.txt.png'))
