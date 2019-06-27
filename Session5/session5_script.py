import numpy as np 
import pandas as panda
import matplotlib
import matplotlib.pyplot as plt

#--------------------numpy----------------------
# https://www.numpy.org/
# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
#     a powerful N-dimensional array object
#     useful linear algebra, Fourier transform, and random number capabilities
# Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. 
# Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

#numpy arrays
#Unterscheiden sich von Listen durch die Funktionen, die auf sie angewendet werden können
#speichern große Datenmengen effizienter
#Python Liste
mylist=[1,2,3,5,6,8]

#umwandeln der Liste in ein Numpy Array
arr=np.array(mylist)

print(mylist)
print(arr)
print(arr*3)
print(mylist*3)

#nützliche numpy Funktionen

#def arange(start, stop, step, , dtype)
#Return evenly spaced values within a given interval.
np.arange(0,10)
np.arange(0,10,3)

np.zeros(5)
np.zeros((5,6))
np.ones(8)
np.ones((8,3))
np.ones((5,), dtype=int)


#def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#Returns num evenly spaced samples, calculated over the interval [start, stop]
np.linspace(0,10,20)

#def randint(low, high, size, dtype)
#Return "size" random integers from low (inclusive) to high (exclusive).
np.random.randint(0,10,20)

#Setzen des random Seed
np.random.seed(112)
np.random.randint(0,100,20)

#Array Funktionen
arr=np.random.randint(0,100,20)

arr.min()
arr.argmin()
arr.max()
arr.argmax()
arr.mean()

#reshape gives a new shape to an array without changing its data.
arr.reshape(5,4)
newarr = np.arange(0,100).reshape(10,10)

#Zugriff auf Daten innerhalb eines Arrays
#array[zeile,reihe]
#Slicing in Reihen und Zeilen ist möglich 
newarr[1,5]
newarr[:,2]
newarr[2,:]

#Masking 
newarr > 10

myfilter = (newarr > 10) & (newarr < 20)
newarr[myfilter]
newarr[newarr > 10]

#Python Data Analysis Library
#https://pandas.pydata.org/
#pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
#Python has long been great for data munging and preparation, but less so for data analysis and modeling. pandas helps fill this gap, enabling you to carry out your entire data analysis workflow in Python without having to switch to a more domain specific language like R.


#Pandas: einlesen von CSV Dateien und Beispiele für den Umgang mit DataFrames 

df = panda.read_csv('BeispielDaten.csv')

df = panda.df()
df.describe()

df['x']

#Eine Reihe zurückgeben
df.loc('1')
df.iloc[1]
df.loc[1,'x']


#Man kann auch eine Liste mit Spaltennamen übergeben

df[['x','y']]

#Neue Spalten erzeugen 
df['new'] = df['x']+df['y']
#Spalte entfernen
df.drop('new',axis=1,inplace=True)


df['x'].max()

#conditional selection
df['x'] > 0.2
df[df['x']>0.2]['x']


df['color'] == 'red'
df[df['color'] == 'red']

#konvertiert Dataframe in ein zweidimensionales Array
#df.as_matrix() 


#matplotlib
#https://matplotlib.org/
#Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
#%matplotlib inline
#Generieren von Beispielwerten (Arrays) für den Plot
x = np.arange(0,10)
y = x**2


#Einfaches plotten plt.plot(x,y)
plt.plot(x,y,':')
plt.plot(x,y)
plt.title("TEST")
plt.xlabel('X LABEL')
plt.ylabel('Y LABEL')
plt.show()

test = np.arange(0,100).reshape(10,10)

plt.imshow(test)
plt.show()

rando = np.random.randint(0,100,(10,10))
plt.imshow(rando)
plt.colorbar()
plt.show()

#Plotten von DataFrames
df.plot(x='x',y='y',kind='scatter')
plt.show()

