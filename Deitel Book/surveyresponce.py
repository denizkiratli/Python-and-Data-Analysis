#surveyresponce.py deitel ch5 ex 5.28-5.29
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat
import seaborn as sns

#5.28-statistical calculations
rate = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,2,5]
values, frequencies = np.unique(rate, return_counts=True)

print('Rate   Frequency')
for i in range(len(values)):
    print(f'{values[i]:>2} {frequencies[i]:>9}')
print()

print(f'Min rate: {min(rate)}')
print(f'Max rate: {max(rate)}')
print(f'Range: {min(rate)} - {max(rate)}')
print(f'Mean: {stat.mean(rate):.2f}')
print(f'Median: {stat.median(sorted(rate))}')
print(f'Mode: {stat.mode(sorted(rate))}')
print(f'Variance: {stat.pvariance(rate):.2f}')
print(f'Standart Deviation: {stat.pstdev(rate):.2f}')
print()

#5.29-graph
title='Rate Frequencies'
sns.set_style('whitegrid')
axes=sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Rates', ylabel='Frequency')
