import matplotlib.pyplot as plt 
import numpy as np 
#steps to create a virtual environment
#1. create your VE (py -3 - m venv (insert name here))
#2. activate your VE (.\introvenv\Scripts\activate), your virtual environment is active if it turns green
#3. Install your third party library in your VE (pip install (insert library you would like to install here))
#after step 3, you should be able to see the library for the library that you wanted to insert
x = np.linspace(0,20,100)
plt.plot(x, np.sin(x))
plt.show()
#git takes a snapshot of all the files and code of the projet that you have in time of everything that is currently there
#ignore all files from the virtual environment