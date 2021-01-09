# import
# PyQt4 import
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# from PyQt4.uic import loadUiType


# PyQt5 import
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

# import os
from os import path
import sys

import pafy
import humanize
import os
from win10toast import ToastNotifier
import subprocess

# import UI File
FROM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))

# initiate UI File


class Mainapp(QMainWindow, FROM_CLASS):
    def __init__(self, parent=None):
        super(Mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setWindowTitle('PyDownloader')
        self.setFixedSize(655, 356)

    def Handel_Buttons(self):  # Bouton de téléchargement
        self.pushButton_2.clicked.connect(self.Handel_Browse)
        self.pushButton_3.clicked.connect(self.Download)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.PlaylistDownload)
        self.pushButton_6.clicked.connect(self.Handel_BrowsePl)

    def Handel_Browse(self):  # Bouton de parcourir
        save_place = QFileDialog.getExistingDirectory(self, "Enregistrer dans")
        # text = str(save_place)
        # name = (text[2:].split(',')[0].replace("'", ''))
        self.lineEdit_2.setText(save_place)

    def Handel_BrowsePl(self):  # Bouton de parcourir
        save_place = QFileDialog.getExistingDirectory(self, "Enregistrer dans")
        # text = str(save_place)
        # name = (text[2:].split(',')[0].replace("'", ''))

        self.lineEdit_6.setText(save_place)

    def search(self):
        link = self.lineEdit.text()
        v = pafy.new(link)
        st = v.streams
        for s in st:
            size = humanize.naturalsize(s.get_filesize())
            data = '{} {} {} {}'.format(
                s.mediatype, s.extension, s.quality, size)
            self.comboBox.addItem(data)
            t_video = '{}'.format(s.title)
            self.lineEdit_3.setText(t_video)

    def Download(self):  # Fonction de téléchargement
        link = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        v = pafy.new(link)
        st = v.streams
        quality = self.comboBox.currentIndex()
        download_video = st[quality].download(filepath=save_location)
        QMessageBox.information(
            self, "Download Completed", "The Download finished")

    def PlaylistDownload(self):
        plurl = self.lineEdit_5.text()
        save_location = self.lineEdit_6.text()
        pl = pafy.get_playlist(plurl)
        vpl = pl['items']
        os.chdir(save_location)
        self.lineEdit_4.setText(str(len(pl['items'])))
        QApplication.processEvents()
        if os.path.exists(str(pl['title'])):
            os.chdir(str(pl['title']))
        else:
            os.mkdir(str(pl['title']))
            os.chdir(str(pl['title']))

        for v in vpl:
            p = v['pafy']
            best = p.getbest(preftype='mp4')
            best.download()
            location = self.lineEdit_6.text()

        QMessageBox.information(
            self, "Download Completed", "The Download finished")

        # # Notification windows
        toaster = ToastNotifier()
        toaster.show_toast("Download Completed", "The Download finished")

        subprocess.Popen('explorer / select, "location/')

        #os.system('explorer location/pl["title"]')


def main():
    app = QApplication(sys.argv)
    window = Mainapp()
    window.show()
    app.exec_()  # infinite loop


if __name__ == "__main__":
    main()
