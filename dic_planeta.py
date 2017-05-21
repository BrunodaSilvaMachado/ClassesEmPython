#_*_ coding: utf-8 _*_
#!/usr/bin/env python

import matplotlib.pyplot as plt

def grafics(_tlist,_dlist,_imagName,_title,_legend,_xLabel,_yLabel):
	print 'processando...'
	plt.figure(figsize=(5,4),dpi=96)
	
	ax = plt.gca()
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.autoscale()
	
	plt.rc('text',usetex = True)
	plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
	plt.xlabel(_xLabel)
	plt.ylabel(_yLabel)

	plt.title(_title,fontsize = 14)
	plt.grid()
	plt.yscale('log')
	plt.xscale('log')
	plt.plot(_tlist,_dlist,'k-',linewidth = 2,label = _legend)
	plt.legend(loc = 'upper left')
	plt.savefig(_imagName+'.png',dpi=96)
	plt.show()


#dicionarios

planetas_t = {"Mercúrio":0.387,"Vênus":0.723,"Terra":1,"Marte":1.523,"Júpiter":5.202,"Saturno":9.539,"Urano":19.18,"Plutão":39.44}

planetas_r = {"Mercúrio":0.241,"Vênus":0.615,"Terra":1,"Marte":1.88,"Júpiter":11.86,"Saturno":29.5,"Urano":84,"Plutão":248}
#end 

kepler_period = [t**2 for t in planetas_t.values()]
kepler_ratio = [r**3 for r in planetas_r.values()]

grafics(kepler_period,kepler_ratio,'image1',r"Kepler's laws",r"Periodo",r'\textit{tempo}(s)',r'\textit{posi\c{c}\~{a}o} (m)')

