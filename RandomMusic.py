#-*- coding: utf-8 -*-
from PySide import QtGui
from PySide.QtCore import QSize

class Dialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()
        self.initFunc()
        self.getPlaylist()
    # set shortcut and other function
    def initFunc( self ):
        # set multi selection
        self.playlistBox.setSelectionMode( QtGui.QAbstractItemView.ExtendedSelection )
        # set playlist function
        self.setPlaylistButton.clicked.connect( self.setPath )
        QtGui.QShortcut( QtGui.QKeySequence( "R" ), self, self.setPath )
        # set delete function
        QtGui.QShortcut( QtGui.QKeySequence( "D" ), self, self.deletePlaylistItem )
        QtGui.QShortcut( QtGui.QKeySequence( "Del" ), self, self.deletePlaylistItem )
        # set focus function
        QtGui.QShortcut( QtGui.QKeySequence( "F" ), self, self.setFocus )
        QtGui.QShortcut( QtGui.QKeySequence( "Enter" ), self, self.loseFocus )
    # set UI
    def initUI( self ):
        self.getConfig()
        # components of UI
        self.playlistBox = QtGui.QListWidget()
        self.setPlaylistButton = QtGui.QPushButton( "Set Playlist!" )
        self.boxLabel = QtGui.QLabel("곡 수: ")
        self.numberOfMusicBox = QtGui.QLineEdit( self.config['number'], parent=None )
        # set horizontal position
        hBox = QtGui.QHBoxLayout()
        hBox.addWidget( self.setPlaylistButton )
        hBox.addWidget( self.boxLabel )
        hBox.addWidget( self.numberOfMusicBox )
        # set vertical position
        vBox = QtGui.QVBoxLayout()
        vBox.addWidget( self.playlistBox )
        vBox.addLayout( hBox )
        # setting for main widget
        self.setLayout( vBox )
        self.setWindowTitle( "랜덤 뮤직" )
        self.setGeometry( 100, 100, 400, 300 )
    # get read config file
    def getConfig( self ):
        # read file
        import configparser
        config = configparser.ConfigParser()
        config.read("configs.ini")
        # input file info
        self.config = {}
        options = config.options( 'Playlist' )
        for option in options:
            self.config[option] = config.get( 'Playlist', option )
    # set music file path
    def setPath( self ):
        path = QtGui.QFileDialog.getExistingDirectory()
        if not path == '':
            self.setPlaylist( path )
    # make playlist
    def setPlaylist( self, path ):
        # check whether file is music file
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
        # set the number of music
        fileNumber = len( tempList )
        musicNumber = int( self.numberOfMusicBox.text() )
        
        if fileNumber == 0:
            return self.showErrorMessage()

        if fileNumber <= musicNumber:
            scope = fileNumber
        else:
            scope = musicNumber        
        # get music by random
        import random
        playlist = open( self.config['name'], "w" )
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
    # get read playlist file
    def getPlaylist( self ):
        playlist = open( self.config['name'], "r" )
        text = playlist.readlines()
        playlist.close()
        self.drawPlaylistBox( text )
    # draw list in self.playlistBox
    def drawPlaylistBox( self, playlist ):
        # initialize
        self.playlistBox.clear()
        size = QSize( 150, 16 )
        # add item
        import re
        for item in playlist:
            item = re.sub( "File\d*=\w:([\\\\]\w+)*[\\\\](.*)[.].+", r"\2", item )
            listItem = QtGui.QListWidgetItem( item )
            listItem.setSizeHint( size )
            self.playlistBox.addItem( listItem )
    # show error message if there's no music in path
    def showErrorMessage( self ):
        msgBox = QtGui.QMessageBox()
        msgBox.setText( "해당 폴더에 음악 파일이 없습니다!" )
        msgBox.exec_()
    # delete selected item from screen and playlist file
    def deletePlaylistItem( self ):
        # read playlist
        with open( self.config['name'], "r" ) as playlist:
            listItem = playlist.readlines()
        # change selected items to blanks
        selected = self.playlistBox.selectedItems()
        for item in selected:
            index = self.playlistBox.indexFromItem( item ).row()
            listItem[index] = ""
        # delete selected item
        with open( self.config['name'], "w" ) as playlist:
            for line in listItem:
                if line != "":
                    playlist.write( line )
                else:
                    listItem.remove( line )
        # apply to the screen
        self.drawPlaylistBox( listItem )
    # set focus to input number of music
    def setFocus( self ):
        self.numberOfMusicBox.clear()
        self.numberOfMusicBox.setFocus()
    # lose focus from self.numberOfMusicBox
    def loseFocus( self ):
        if self.numberOfMusicBox.gotFocus():
            self.numberOfMusicBox.loseFocus()
        print( "lose" )

if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = Dialog()
    form.show()
    app.exec_()
