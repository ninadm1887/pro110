import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading time"], show_hist=False, colors = ['#5200cc'])
fig.show()
print("population mean:- ",statistics.mean(data))
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading time"], show_hist=False, colors = ['#5200cc'])
    fig.add_trace(go.Scatter(x=[mean,mean], y = [0,1], mode = 'lines', name = 'mean'))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Sampling mean for the data is :- ", statistics.mean(mean_list))

setup()