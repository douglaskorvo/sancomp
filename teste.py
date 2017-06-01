import calculations
import sancomp
import numpy as np
from scipy.interpolate import interp1d

def ler_do_arquivo_e_separar_colunas_em_vetores(self):
	nucleo=[]
	elasticidade=[]
	file = open('nucleo-elasticidade.dat')
	linha=file.readline()
	while(linha):
		nucleo.append(str(linha.split("	")[0]))
		elasticidade.append(float(linha.split("	")[1]))
		linha=file.readline()

#print sancomp.MyApp.face

x=0.7
v=0.3
	
v0 = [0.8333, 0.8333, 0.8333, 0.8333, 0.8333, 0.8333]
v25 = [1, 0.8331, 0.8295, 0.7961, 0.6308, 0]
v50 = [1, 0.8385, 0.8228, 0.7375, 0.4404, 0]

def y(y0,y1,x0,x1,x):
	return y0+((y1-y0)*((x-x0)/(x1-x0)))
	
if (v > 0.25) and (v < 0.5):
	if (x>2):
		f3=1
		print str(f3)
	elif (x<2) and (x>1):
		f1 = y(v25[1],v50[1],0.25, 0.5,v)
		f2 = y(v25[2],v50[2],0.25,0.5,v)
		f3 = y(f1,f2,2,1,x)
		print str(f3)
	elif (x<1) and (x>0.5):
		f1 = y(v25[2],v50[2],0.25,0.5,v)
		f2 = y(v25[3],v50[3],0.25,0.5,v)
		f3 = y(f1,f2,1,0.5,x)
		print str(f3)
	elif (x<0.5) and (x>0.25):
		f1 = y(v25[3],v50[3],0.5,0.25,v)
		f2 = y(v25[4],v50[4],0.5,0.25,v)
		f3 = y(f1,f2,0.5,0.25,x)
		print str(f3)
	elif (x<0.25) and (x>-0.5):
		f1 = y(v25[4],v50[4],0.25,-0.5,v)
		f2 = y(v25[5],v50[5],0.25,-0.5,v)
		f3 = y(f1,f2,0.25,-0.5,x)
		print str(f3)
else:
	if (x>2):
		f3=1
		print str(f3)
	elif (x<2) and (x>1):
		f1 = y(v0[1],v25[1],0.25, 0.5,v)
		f2 = y(v0[2],v25[2],0.25,0.5,v)
		f3 = y(f1,f2,2,1,x)
		print str(f3)
	elif (x<1) and (x>0.5):
		f1 = y(v0[2],v25[2],0.25,0.5,v)
		f2 = y(v0[3],v25[3],0.25,0.5,v)
		f3 = y(f1,f2,1,0.5,x)
		print str(f3)
	elif (x<0.5) and (x>0.25):
		f1 = y(v0[3],v25[3],0.5,0.25,v)
		f2 = y(v0[4],v25[4],0.5,0.25,v)
		f3 = y(f1,f2,0.5,0.25,x)
		print str(f3)
	elif (x<0.25) and (x>-0.5):
		f1 = y(v0[4],v25[4],0.25,-0.5,v)
		f2 = y(v0[5],v25[5],0.25,-0.5,v)
		f3 = y(f1,f2,0.25,-0.5,x)
		print str(f3)

file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))