from pyscript import document

import numpy as np
import base64
from io import BytesIO
import matplotlib.pyplot as plt

def abc(event):
    input_text = document.querySelector("#english")
    input_text2 = document.querySelector("#uin")
    input_text.innerHTML=input_text2.value;
    print('Hello,World')


def plot_data():
    x=np.random.randn(100)
    y=np.random.randn(100)
    # plt.plot(x,y)
    return x,y


def set_plot():
    plot_box=document.querySelector("#plot")
    fig, ax = plt.subplots()
    x,y=plot_data()
    ax.scatter(x,y)
    ax.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    # font1 = {'family':'serif','color':'blue','size':20}
    # font2 = {'family':'serif','color':'darkred','size':15}
    ax.set_title("Sports Watch Data")
    ax.set_xlabel("This is X label")
    ax.set_ylabel("This is Y label")
    # plot_box.innerHTML=""
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    plot_box.innerHTML=f"<img src='data:image/png;base64,{data}'/>"