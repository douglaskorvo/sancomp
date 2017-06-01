import sys
import numpy as np
import calculations
from PyQt4 import QtCore, QtGui, uic
import re
 
qtCreatorFile = "sancompt.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

face = []
core = []
face_moduli = []
face_density = []
face_poisson = []
gxy = 0

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		#self.laminate.toggled.connect(self.f_laminate)
		#self.radioButton.toggled.connect(self.calc_def)
		self.calcular_f.clicked.connect(self.verify)
		self.calcular_g.clicked.connect(self.verify2)
		self.cb_beam.activated.connect(self.setImage)
		
		#filling qcombobox from file nucleo-elasticidade.dat
		global core
		core=[]
		global core_moduli
		core_moduli=[]
		file = open('nucleo-elasticidade.dat')
		linha=file.readline()
		while(linha):
			core.append(str(linha.split("	")[0]))
			core_moduli.append(float(linha.split("	")[1]))
			linha=file.readline()
		self.cb_core.addItems(core)
		#filling qcombobox from file face-elasticidade-poisson.dat
		global face
		#face=[]
		global face_moduli
		face_moduli=[]
		global face_poisson
		face_poisson=[]
		file2=open('face-elasticidade-poisson.dat')
		linha2=file2.readline()
		while(linha2):
			face.append(str(linha2.split("	")[0]))
			face_moduli.append(float(linha2.split("	")[1]))
			face_poisson.append(float(linha2.split()[2]))
			linha2 =file2.readline()
		self.cb_laminate.addItems(face)
		
		#face.append(str(self.name))
		#face_moduli.append(float(self.ex))
		
	def setImage(self): #set pixmap when focus change
		if self.cb_beam.currentText() == "Simple-Simple / Point":
			self.pic_beam.setPixmap(QtGui.QPixmap("image/v1.png"))
		elif self.cb_beam.currentText() == "Simple-Simple / Uniform":
			self.pic_beam.setPixmap(QtGui.QPixmap("image/v2.png"))
		elif self.cb_beam.currentText() == "Free-Fixed / Point":
			self.pic_beam.setPixmap(QtGui.QPixmap("image/v3.png"))
		elif self.cb_beam.currentText() == "Free-Fixed / Uniform":
			self.pic_beam.setPixmap(QtGui.QPixmap("image/v4.png"))
		elif self.cb_beam.currentText() == "Fixed-Fixed / Point":
			self.pic_beam.setPixmap(QtGui.QPixmap("image/v5.png"))
		elif self.cb_beam.currentText() == "Fixed-Fixed / Uniform":
			self.pic_beam.setPixmap(QtGui.QPixmap("image/v6.png"))
		elif self.cb_beam.currentText() == "Choose beam...":
			self.pic_beam.setPixmap(QtGui.QPixmap("image/v0.png"))
			
			
	def verify(self): #verifying input data and calculating lamina or assuming data as laminate data
		#if not self.lamina.isChecked() and not self.laminate.isChecked():
		#	self.textBrowser.setText("Select lamina or laminate")
		#	self.textBrowser.setStyleSheet('color: red')
		#elif self.lamina.isChecked(): #calling functions of calculations module to calculate first tab
		#	self.textBrowser.setStyleSheet('color: black')
		#	calculations.lamina(self)
		#elif self.laminate.isChecked():
		#	self.textBrowser.setStyleSheet('color: black')
		#	calculations.laminate(self)
		try: #reading form data and making the treatment of ValueError
			name = str(self.name.toPlainText())
			ex = self.ex.toPlainText()
			ex=float(ex)
			ey = float(self.ey.toPlainText())
			gxy = float(self.gxy.toPlainText())
			#g12 = float(g12)
			vxy = float(self.vxy.toPlainText())
			#calculations.save_laminate_temp(self)
			if name == "":
				self.textBrowser.setText("Insert a name for the custom laminate")
			else:
				face.append(name)
				face_moduli.append(ex)
				linha_face = ("\n"+name+"\t"+str(ex))
				with open("face-elasticidade-poisson.dat","a") as arq_face:
					arq_face.write(linha_face)
				self.cb_laminate.addItems(face)
				self.tabWidget.setCurrentIndex(1)
			
		except ValueError: 
			self.textBrowser.setStyleSheet('color: red')
			self.textBrowser.setText("Fill all fields or check if data entered is correct")	


		
	def verify2(self):
		try: #reading form data for second tab and making the treatment of ValueError
			laminate_cb = str(self.cb_laminate.currentText())
			core_cb = str(self.cb_core.currentText())
			beam_cb = str(self.cb_beam.currentText())
			load = float(self.load.toPlainText())
			h = float(self.h.toPlainText())
			H = float(self.H.toPlainText())
			b = float(self.b.toPlainText())
			l = float(self.l.toPlainText())
			self.message.setText(" ")

			calculations.beam(self,face,face_moduli,face_poisson,core,core_moduli)
			
		except ValueError:
			self.message.setStyleSheet('color: red')
			self.message.setText("Fill all fields or check if data entered is correct" )
		lami = "Choose laminate..."
		cor = "Choose core..."
		beam = "Choose beam..."
		if self.cb_laminate.currentText() == lami:
			self.message.setText("Select a laminate")
		elif self.cb_core.currentText() == cor:
			self.message.setText("Select a core")
		elif self.cb_beam.currentText() == beam:
			self.message.setText("Select a beam type")
		
		
	
	
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('image/sancomp.ico'))
	window = MyApp()
	window.show()
	sys.exit(app.exec_())