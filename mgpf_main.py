#!/usr/bin/python
# -*-coding:Utf-8 -*

# Par Cédric Bouiron
# Pour la MGPF Team
# 27 Juillet 2017

# --- import des modules ---
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os, sys, time

# --- import du GUI ---
from mgpf_gui import *


SystemState = False
NeverLaunch = True
Time0 = 0
TimeSpend = 0

# Classe contenant le code actif
class myApp(QMainWindow, Ui_MainWindow):

	# ici self représente la classe
	
	def __init__ (self, parent = None):
		QMainWindow.__init__(self)	# init de QMainWindow
		self.setupUi(parent) 		# obligatoire
	
		self.connect(self.pushButton, SIGNAL("clicked()"), self.pushButtonClicked)
		
		# init timer
		self.timer=QTimer()
		self.connect(self.timer, SIGNAL("timeout()"), self.timer_msec)
		
		self.timer2=QTimer()
		self.connect(self.timer2, SIGNAL("timeout()"), self.timer_seconde)
		
		self.timer3=QTimer()
		self.connect(self.timer3, SIGNAL("timeout()"), self.timer_minute)
		# code actif initial
		
	# End __init__	
		
	# les fonctions appelées
	
	
		
	
	def pushButtonClicked(self):
		global SystemState, NeverLaunch, Time0, TimeSpend
		
		SystemState ^= True
		
		if SystemState == True :
			Time0 = time.time()
			self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "STOP", None, QtGui.QApplication.UnicodeUTF8))
			self.timer.start()
			self.timer2.start()
			self.timer3.start()
		else:
			self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "START", None, QtGui.QApplication.UnicodeUTF8))
			self.timer.stop()
			self.timer2.stop()
			self.timer3.stop()
			
			
		print("button pushed") 
		
	def timer_msec(self):
		global TimeSpend,Time0
		self.timer.stop()
		TimeSpend += time.time() - Time0
		Time = int((TimeSpend - int(TimeSpend)) * 1000)
		print(Time)
		self.lcd_msec.display(Time)
		Time0 = time.time()
		self.timer.start(100)
		
	def timer_seconde(self):
		global TimeSpend
		self.timer2.stop()
		
		Time = int(int(TimeSpend) % 60)
		print(Time)
		self.lcd_seconde.display(Time)
		
		self.timer2.start(100)	
	
	def timer_minute(self):
		global TimeSpend
		self.timer3.stop()
		
		Time = time.time() - Time0
		Time = int(TimeSpend)
		Time = int(Time / 60)
		print(Time)
		self.lcd_minute.display(Time)
		
		self.timer3.start(100)	



		
# Fonction principale exécutant l'application Qt
def main(args):
	a =	QApplication(args)		# crée l'objet application
	f = QMainWindow()			# crée le QMainWindow racine
	c = myApp(f)				# appelle la class contenant le code de l'application
	f.show()					# affiche la fenetre QMainWindow
	r = a.exec_()	 			# lance l'exécution de l'application
	return r
	
# Rend le fichier *.py exécutable
if __name__ == "__main__":
	main(sys.argv) 



#import subprocess, time
#from time import sleep

#play_process = None

#print("Wesh!")
#a = int(input("Appuie sur 1 : "))

#if a==1 :
#   command = '/usr/bin/lxterminal -e /usr/bin/omxplayer -o local /home/pi/mgpf-teaser-2014.mp4'
 #   subprocess.call(command, shell = True)
    



