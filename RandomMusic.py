from PySide import QtGui
class Dialog(QtGui.QWidget):
    def __init__(self):
        """Constructor"""
        # super(Dialog, self).__init__()
        QtGui.QWidget.__init__(self)

        #create components
        musicListDocument = QtGui.QTextEdit
        b = QtGui.QTextDocument
        c = QtGui.QTextBlock
        d = QtGui.QTextCursor
        musicPlayBtn = QtGui.QPushButton("Play Random Music")

        #connect components to the functions
        musicPlayBtn.clicked.connect(self.openMp3)

        layout = QtGui.QVBoxLayout()
        #layout.addWidget(musicListFrame)
        layout.addWidget(musicPlayBtn)
        self.setLayout(layout)
        self.setGeometry(100,100, 400, 300)
        self.setWindowTitle("랜덤 뮤직")
        self.dir = ""
        self.length = 0

    def openDirDialog(self):
        """Opens the Directory Dialog"""
        self.dir = QtGui.QFileDialog.getExistingDirectory()
        self.updateMusicList()

    def openMp3(self):
        """Saves music lists and opens music player"""
        self.openDirDialog()

    def updateMusicList(self):
        import os
        print(self.dir)
        self.fileList = os.listdir(self.dir)
        self.fileList = [item for item in self.fileList\
                          if item[-4:] == '.mp3' or item[-4:] == '.wav']
        self.musicList = []
        self.length = len(self.fileList)
        self.selectMusic()

    def selectMusic(self):
        import random
        if self.length == 0:
            self.openError()
        else:
            for i in range(30):
                r = random.randrange(0,self.length)
                self.musicList.insert(-1, self.fileList[r])
                self.fileList.pop(r)
                self.length-=1
                if self.length == 0:
                    break;
        self.makeMusicList()

    #if musicList == 0 -> print Error Message and go back front function
    def openError(self):
        error = QtGui.QErrorMessage()
        error.showMessage("해당 폴더에 음악 파일이 없습니다!")
        error.exec_()
        self.openMp3()

    def makeMusicList(self):
        f = open("Random Music.pls", mode="w")
        for index in range(len(self.musicList)):
            f.writelines("File"+str(index)+"="+self.dir+"\\"+self.musicList[index]+"\n")
        f.close()

if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = Dialog()
    form.show()
    app.exec_()