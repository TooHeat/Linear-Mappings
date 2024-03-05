import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact, FloatSlider

def A(x,y):
  return a*x + b*y, c*x + d*y

def plot_vectors(x=1, y=1):
  Ax, Ay = A(x,y)
  # set up axes so it looks good
  fig, ax = plt.subplots(figsize = (10,10))
  ax.set_ybound(min(y, Ay, -5)-1, max(y, Ay, 5)+1)
  ax.set_xbound(min(x, Ax, -5)-1, max(x, Ax, 5)+1)
  ax.set_aspect(1)
  ax.spines['left'].set_position('zero')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')

  # plot and label arrows
  label_string = "${}\\binom{{x}}{{y}}=\\binom{{{}}}{{{}}}$"
  ax.annotate("", (0,0), xytext = (x, y), arrowprops=dict(arrowstyle="<-"))
  ax.annotate(label_string.format("", x,y), (x, y), xytext = (x, y), fontsize="x-large")
  ax.annotate("", (0,0), xytext = (Ax, Ay), arrowprops=dict(arrowstyle="<-"))
  ax.annotate(label_string.format("A", Ax, Ay), (Ax,Ay), xytext = (Ax, Ay), fontsize="x-large")

a= 0
b= -1
c= 1
d= 0

interact(plot_vectors, x=(-6,6,1), y=((-6,6,1)))
