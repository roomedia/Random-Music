#0.0.1
##수정
###initUI
메인 다이얼로그에 들어갈 UI 설정.
스크롤 되는 텍스트 상자랑 곡 갯수를 입력할 텍스트 상자,
플레이리스트 설정하는 버튼 위치 설정.

###setPath
플레이리스트 버튼이 눌리면 실행되는 함수.
플레이리스트 다이얼로그를 연다. 선택된 다이얼로그의 경로를 리턴한다.
취소를 누르면 현재 경로를 리턴. 음악으로 간주되는 파일이 없으면 재귀호출.

###setPlaylist
플레이리스트 다이얼로그가 닫히면 실행되는 함수.
전체 음악 파일 목록을 집합으로 만들어 플레이리스트에 저장한다.

###getPlaylist
프로그램 실행 시 실행되는 함수, setPlaylist 실행 이후에 실행되는 함수.
플레이리스트 목록을 텍스트 박스로 불러온다.



#0.0.2
##수정
###setPath
음악으로 간주되는 파일이 없으면 showErrorMessage를 호출.
단축키 R로도 호출 가능.

###getPlaylist
playlist를 불러와 리스트로 만들고 drawPlaylistBox를 호출.

###initUI
self.playlistBox가 다중 선택을 할 수 있도록 설정


##추가
###showErrorMessage
선택한 폴더에 음악 파일이 없을 때 뜨는 메시지 창.

###getConfig
initUI를 실행하면 실행.
configs.ini 파일로부터 플레이리스트의 이름, 곡의 개수를 읽어오는 함수.

###drawPlaylistBox
playlist.pls의 내용 리스트를 인자로 받아 각각의 요소를 QListWidgetItem
으로 만드는 함수. 사이즈를 조정한 후 self.PlaylistBox에 추가해준다.

###deletePlaylistItem
self.PlaylistBox에서 항목을 선택한 후 키보드 Delete/D 키를 누르면
해당 항목을 playlist.pls와 self.PlaylistBox에서 삭제.
이후 drawPlaylistBox 호출

###setFocus
단축키 F를 통해 self.numberOfMusicBox에 Focus를 가져온다.

###loseFocus
self.numberOfMusicBox에 Focus가 있을 경우,
단축키 Enter를 통해 self.numberOfMusicBox에서 Focus를 해제한다.

###initFunc
프로그램에서 쓰이게 될 단축키 함수 설정.
R 키를 누르면 setPath 함수 호출.
F 키를 누르면 setFocus 함수 호출.
Enter 키를 누르면 loseFocus 함수 호출.
Del/D 키를 누르면 deletePlaylistItem 함수 호출.



#Issue
##0.0.2
1. Delete를 두 번 누르면 선택되지 않은 항목도 지워지는 버그 발견
2. loseFocus 미구현