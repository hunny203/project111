import csv
import imp
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
        
    mean=statistics.mean(dataset)
    return mean


mean_list=[]
for i in range(0,100):
    set_of_means=random_set_of_mean(30)
    mean_list.append(set_of_means)

mean=statistics.mean(mean_list)
print("mean is: ",mean)


median_marks=statistics.median(data)
print("median of marks is: {}".format(median_marks))

mode_marks=statistics.mode(data)
print("mode of marks is: {}".format(mode_marks))

std_dev_math=statistics.stdev(data)
print("standard deviation for marks is: {}".format(std_dev_math))

first_std_dev_ht_start,first_std_dev_ht_end=mean-std_dev_math,mean+std_dev_math
list_of_data_within_first_std_dev_ht=[result for result in data if result>first_std_dev_ht_start and result<first_std_dev_ht_end]
print("{}% of data lies within first standard deviation marks".format(len(list_of_data_within_first_std_dev_ht)*100.0/len(data)))

second_std_deviation_ht_start, second_std_deviation_ht_end = mean-(2*std_dev_math), mean+(2*std_dev_math)
list_of_data_within_2_std_deviation_ht = [result for result in data if result > second_std_deviation_ht_start and result < second_std_deviation_ht_end] 
print("{}% of data lies within 2 standard deviations marks".format(len(list_of_data_within_2_std_deviation_ht)*100.0/len(data)))


third_std_deviation_ht_start, third_std_deviation_ht_end = mean-(3*std_dev_math), mean+(3*std_dev_math)
list_of_data_within_3_std_deviation_ht = [result for result in data if result > third_std_deviation_ht_start and result < third_std_deviation_ht_end]
print("{}% of data lies within 3 standard deviations marks".format(len(list_of_data_within_3_std_deviation_ht)*100.0/len(data)))

# def show_fig(mean_list):
   # df=mean_list
 #   mean=statistics.mean(df)
  #  fig=ff.create_distplot([df],["Math_score"],show_hist=False)
   # fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    #fig.show()

#show_fig(mean_list)


df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
mean_sample1=statistics.mean(data)
print("mean1 is: ",mean_sample1)
fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.show()

z_score=(mean-mean_sample1)/std_dev_math
print("Sample 1 z-score is: ",z_score)

