#0.0.1
##����
###initUI
���� ���̾�α׿� �� UI ����.
��ũ�� �Ǵ� �ؽ�Ʈ ���ڶ� �� ������ �Է��� �ؽ�Ʈ ����,
�÷��̸���Ʈ �����ϴ� ��ư ��ġ ����.

###setPath
�÷��̸���Ʈ ��ư�� ������ ����Ǵ� �Լ�.
�÷��̸���Ʈ ���̾�α׸� ����. ���õ� ���̾�α��� ��θ� �����Ѵ�.
��Ҹ� ������ ���� ��θ� ����. �������� ���ֵǴ� ������ ������ ���ȣ��.

###setPlaylist
�÷��̸���Ʈ ���̾�αװ� ������ ����Ǵ� �Լ�.
��ü ���� ���� ����� �������� ����� �÷��̸���Ʈ�� �����Ѵ�.

###getPlaylist
���α׷� ���� �� ����Ǵ� �Լ�, setPlaylist ���� ���Ŀ� ����Ǵ� �Լ�.
�÷��̸���Ʈ ����� �ؽ�Ʈ �ڽ��� �ҷ��´�.



#0.0.2
##����
###setPath
�������� ���ֵǴ� ������ ������ showErrorMessage�� ȣ��.
����Ű R�ε� ȣ�� ����.

###getPlaylist
playlist�� �ҷ��� ����Ʈ�� ����� drawPlaylistBox�� ȣ��.

###initUI
self.playlistBox�� ���� ������ �� �� �ֵ��� ����


##�߰�
###showErrorMessage
������ ������ ���� ������ ���� �� �ߴ� �޽��� â.

###getConfig
initUI�� �����ϸ� ����.
configs.ini ���Ϸκ��� �÷��̸���Ʈ�� �̸�, ���� ������ �о���� �Լ�.

###drawPlaylistBox
playlist.pls�� ���� ����Ʈ�� ���ڷ� �޾� ������ ��Ҹ� QListWidgetItem
���� ����� �Լ�. ����� ������ �� self.PlaylistBox�� �߰����ش�.

###deletePlaylistItem
self.PlaylistBox���� �׸��� ������ �� Ű���� Delete/D Ű�� ������
�ش� �׸��� playlist.pls�� self.PlaylistBox���� ����.
���� drawPlaylistBox ȣ��

###setFocus
����Ű F�� ���� self.numberOfMusicBox�� Focus�� �����´�.

###loseFocus
self.numberOfMusicBox�� Focus�� ���� ���,
����Ű Enter�� ���� self.numberOfMusicBox���� Focus�� �����Ѵ�.

###initFunc
���α׷����� ���̰� �� ����Ű �Լ� ����.
R Ű�� ������ setPath �Լ� ȣ��.
F Ű�� ������ setFocus �Լ� ȣ��.
Enter Ű�� ������ loseFocus �Լ� ȣ��.
Del/D Ű�� ������ deletePlaylistItem �Լ� ȣ��.



#Issue
##0.0.2
1. Delete�� �� �� ������ ���õ��� ���� �׸� �������� ���� �߰�
2. loseFocus �̱���