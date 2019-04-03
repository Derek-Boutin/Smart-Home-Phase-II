import numpy as np 
import matplotlib.pyplot as plt

i = 0
j = 1
x_coords = []
y_coords = []
file = open("Light Data.txt", "r")
#for x in file:
    #print(x)

lines = file.readlines()
l = (lines[0])
p = int(l)
#print(p)
#x_coords.append(p)
#print(lines[2])

#print(file.readline())
#file.readline()
#file.readline()
#file.readline()
#print(file.readline())

    
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file_length = file_len("Light Data.txt")

while i<file_length and j<file_length:
    x_line = (lines[i])
    x_line_float = float(x_line)
    x_line_int = int(x_line_float)
    x_coords.append(x_line_int)
    y_line = (lines[j])
    y_line_int = int(y_line)
    y_coords.append(y_line_int)
    
    #int_lines = int(lines)
    #x_coords.append(int_lines)
    #y_coords.append(lines[2])
    i = i + 2
    j = j + 2
    
    
  
#print(file_length)
print(x_coords)
print(y_coords)

import numpy as np 
import matplotlib.pyplot as plt

def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 

    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 

    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x - n*m_y*m_x) 
    SS_xx = np.sum(x*x - n*m_x*m_x) 

    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 

    return(b_0, b_1)

def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 

    # predicted response vector 
    y_pred = b[0] + b[1]*x 

    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
      # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 

    # function to show plot 
    plt.show()

def main(): 
    # observations 
    
    # estimating coefficients
    #x.astype(int)
    x = np.array(x_coords)
    y = np.array(y_coords)

    b = estimate_coef(x,y) 
    print("Estimated Coefficients:\nm = {}  \ \ny-int= {}".format(b[1], b[0])) 

    # plotting regression line 
    plot_regression_line(x, y, b)

main()

    
    