# PyQT5 import
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import sys
import os
from os import path
import urllib.request
import shutil
import pafy
import certifi
# import hurry
import humanize
import youtube_dl
import ssl

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent: object = None) -> object:
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_UI()
        self.handle_buttons()

    def handle_UI(self):
        self.setWindowTitle("YtbDownloader")
        self.setFixedSize(601, 250)

    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.download)
        self.pushButton.clicked.connect(self.handle_browse)
        self.pushButton_7.clicked.connect(self.get_ytb_video)
        self.pushButton_3.clicked.connect(self.download_ytb_video)
        self.pushButton_5.clicked.connect(self.handle_browse2)

    def handle_browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files (*.*)")
        path = str(save_place)
        loc = path.split("'")[1]
        self.lineEdit_2.setText(loc)

    def handle_browse2(self):
        save_location = QFileDialog.getExistingDirectory(self, "Select folder")
        #save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files (*.*)")
        path = str(save_location)
        #loc = path.split("'")[1]
        self.lineEdit_4.setText(path)

    def handle_progress(self, copied, totalsize):

        if copied > 0:
            percent = copied * 100 / totalsize
            self.progressBar.setvalue(percent)
            QApplication.processEvents()

    def download(self):
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:
            test = urllib.request.urlopen(url,cafile=r"C:\Users\gupta248\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\certifi\cacert.pem")
            filename = open(save_location, 'wb')
            shutil.copyfileobj(test, filename)
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "Download error", "The download failed")
            return

        QMessageBox.Information(self, "Download Complete", "The download finished")
        self.progressBar.setvalue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

    def copyfileobj(fsrc, fdst, callback, total, length=16 * 1024):
        copied = 0
        while True:
            buf = fsrc.read(length)
            if not buf:
                break
            fdst.write(buf)
            copied += len(buf)
            callback(copied, total=total)

    def get_ytb_video(self):
        video_link = self.lineEdit_3.text()
        w = pafy.new(video_link, ydl_opts="-v --no-check-certificate")
        print(w.title)
        stream = w.videostreams
        for s in stream :
            size = humanize.naturalsize(s.get_filesize())
            data = '{}  {}  {}  {}'.format(s.mediatype, s.resolution, s.extension, size)
            self.comboBox.addItem(data)

    def download_ytb_video(self):
        video_link = self.lineEdit_3.text()
        w = pafy.new(video_link, ydl_opts="-v --no-check-certificate")
        stream = w.videostreams
        save_location = self.lineEdit_4.text()

        quality = self.comboBox.currentIndex()
        down =stream[quality].download(filepath=save_location)
        QMessageBox.information(self, "Download Complete", "The download finished")
        # self.progressBar.setvalue(0)
        # self.lineEdit.setText('')
        # self.lineEdit_2.setText('')


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()  # infinite loop


if __name__ == '__main__':
    main()
