# 
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys

rollsoffirst = [random.randrange(1,7) for i in range(int(sys.argv[1]))]
rollsofsecond = [random.randrange(1,7) for i in range(int(sys.argv[1]))]
totalofrolls = []
for i in range(len(rollsoffirst)):
	totalofrolls.append(rollsoffirst[i]+rollsofsecond[i])
values, frequencies = np.unique(totalofrolls, return_counts=True)

title = f'Frequencies of {len(totalofrolls):,} Rolls'
sns.set_style('white')
axes = sns.barplot(x=frequencies, y=values, orient='h', palette='bright')
axes.set_title(title)
axes.set(ylabel='Die Value', xlabel='Frequency')
axes.set_xlim(right=max(frequencies)*1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_y = bar.get_y()+ bar.get_height()
    text_x = bar.get_width()
    text = f'{frequency:,}\n{frequency / len(totalofrolls):.3%}'
    axes.text(text_x, text_y ,text, fontsize=11, ha='left', va='baseline')

plt.show()
