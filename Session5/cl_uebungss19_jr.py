#!/usr/bin/python3
import matplotlib.pyplot as plt
from numpy.random import rand
import pandas

# Funktion CreateData
def createData(data_points, filename):
	if data_points < 5:
		data_points = data_points * 5
	# als Erinnerung: rand(zeilen, spalten)
	x = rand(data_points, 2)
	df = pandas.DataFrame(data=x, columns=['x', 'y'])
	# print(df)
	df.to_csv(filename)
	print("Erzeugte Daten wurden in " + filename + " gespeichert.")


# Funktion CreatePlot
def createPlot(filename):
	df = pandas.read_csv(filename)	
	# plot = plt.scatter(x=df['x'], y=df['y'])
	plot = df.plot(x=df.iloc[:,1], y=df.iloc[:,2], kind='scatter') 
	# plot = df.plot(x=df['x'], y=df['y'], kind='scatter'))	
	# Ausgabe führt zu einem Fehler:	
	print(plot)
	


createData(15, "scatterPlot.csv")
createPlot("scatterPlot.csv")

