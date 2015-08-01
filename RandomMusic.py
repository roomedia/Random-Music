from PySide import QtGui
from PySide.QtCore import QSize

class Dialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()
        self.getPlaylist()

    def initUI( self ):
        self.playlistBox = QtGui.QListWidget()
        self.setPlaylistButton = QtGui.QPushButton( "Set Playlist!" )
        self.boxLabel = QtGui.QLabel("곡 수: ")
        self.numberOfMusicBox = QtGui.QLineEdit( "30", parent=None )
        
        self.setPlaylistButton.clicked.connect( self.setPath )

        hBox = QtGui.QHBoxLayout()
        hBox.addWidget( self.setPlaylistButton )
        hBox.addWidget( self.boxLabel )
        hBox.addWidget( self.numberOfMusicBox )

        vBox = QtGui.QVBoxLayout()
        vBox.addWidget( self.playlistBox )
        vBox.addLayout( hBox )

        self.setLayout( vBox )
        self.setWindowTitle( "랜덤 뮤직" )
        self.setGeometry( 100, 100, 400, 300 )

    def setPath( self ):
        path = QtGui.QFileDialog.getExistingDirectory()
        if not path == '':
            self.setPlaylist( path )

    def setPlaylist( self, path ):
        import os
        fileList = [ item for item in os.listdir( path ) if os.path.isfile( path + "\\" + item ) ]
        tempList = []
        musicFormat = '.3gp.aiff.aac.alac.amr.wav.au.awb.dvf.flac.mmf.mp3.mpc.msv.ogg.opus.tta.vox.wma'
        
        import re
        for item in fileList:
            for i in range(-5, -3):
                if musicFormat.find( item[i:] ) == -1:
                    remove = True
                else:
                    remove = False
            if not remove:
                tempList.append( item )

        fileNumber = len( tempList )
        musicNumber = int( self.numberOfMusicBox.text() )
        
        if fileNumber == 0:
            return getErrorMsg()

        if fileNumber <= musicNumber:
            scope = fileNumber
        else:
            scope = musicNumber        

        import random
        playlist = open( "playlist.pls", "w" )
        for i in range( scope ):
            if i != scope:
                seed = random.randrange( 0, fileNumber - i )
                music = tempList[ seed ]
                playlist.write( "File"+str(i)+"="+path+"\\"+music+"\n" )
                tempList.remove( music )
            else:
                musicList.append( tempList[0] )
        playlist.close()
        self.getPlaylist()

    def getPlaylist( self ):
        print( "I'm getPlaylist!" )
        self.playlistBox.clear()
        playlist = open( "playlist.pls", "r" )
        text = playlist.readlines()
        playlist.close()

        size = QSize( 150, 16 )

        import re
        for item in text:
            item = re.sub( "File\d*=\w:([\\\\]\w+)*[\\\\](.*)[.].+", r"\2", item )
            listItem = QtGui.QListWidgetItem( item )
            listItem.setSizeHint( size )
            self.playlistBox.addItem( listItem )

if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = Dialog()
    form.show()
    app.exec_()