#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import hashlib
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QThread, Signal

from MainWidget import MainWidget

class MyThread(QThread):
    signal_done = Signal()

    def __init__(self):
        super(MyThread, self).__init__()

        self.h = hashlib.sha256()

    def run(self):
        while True:
    #         with open('foo.txt', 'w') as dot_file:
    #             dot_file.write('''
    # graph graphname {
    #     a;
    #     b;
    #     c;
    #     d;
    #     a -- b;
    #     b -- c;
    #     b -- d;
    # }
    # ''')
    #             dot_file.flush()
    #             dot_file.close()

            result = subprocess.run('graphviz-2.38\\bin\\dot.exe -Tpng -O foo.txt'.split())

            if result.returncode == 0:
                self.signal_done.emit()

app = QApplication(sys.argv)

main_widget = MainWidget()
worker = MyThread()

worker.signal_done.connect(main_widget.update_image)

main_widget.show()
worker.start()

sys.exit(app.exec_())
