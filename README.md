# BOOMER

Pour pouvoir exécuter le fichier mgpf_main.py sur Windows :

Tuto : http://www.mon-club-elec.fr/mes_downloads/tutos_pyqt/pyqt_abc_installation_windows.pdf

1/ Installer python 3.4:
https://www.python.org/downloads/windows/
Chercher : Python 3.4.4 - 2015-12-21\Download Windows x86 MSI installer

2/ Installer PyQt4
https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/
Chercher : PyQt4-4.11.4-gpl-Py3.4-Qt4.8.7-x32.exe

Pour pouvoir exécuter le fichier mgpf_main.py sur Linux :

Tuto : http://www.mon-club-elec.fr/mes_downloads/tutos_pyqt/pyqt_abc_installation_gnu_linux.pdf

1/ Installer PyQt4:
sudo apt-get install python-qt4 pyqt4-dev-tools

2/ Installer Qt4 Designer:
sudo apt-get install qt4-designer



Le fichier mgpf_gui.ui contient l'interface graphique il peut s'ouvrir et s'éditer grâce à:
C:\Python\Python34\Lib\site-packages\PyQt4\designer.exe

Une fois le fichier modifié comme souhaité il faut le convertir ce fichier 'mgpf_gui.ui' obtenu en 'mgpf_gui.py' 

http://www.mon-club-elec.fr/pmwiki_mon_club_elec/pmwiki.php?n=MAIN.PYQTabcPrincipeProgPyQt

Cela se fait sur Windows : pyuic4 mgpf_gui.ui > mgpf_gui.py

Cela se fait sur Linux : pyuic4 -o mgpf_gui.py -x mgpf_gui.ui
