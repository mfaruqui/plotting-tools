import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 7
french = [220, 60, 69, 19, 54, 10, 384]
hindi = [180, 43, 88, 28, 54, 3, 253]
russian = [137, 25, 55, 4, 16, 2, 393]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.20                      # the width of the bars

## the bars
french_bar = ax.bar(ind, french, width,
                color='green',
                error_kw=dict(elinewidth=2,ecolor='green'))

hindi_bar = ax.bar(ind+width, hindi, width,
                    color='red',
                    error_kw=dict(elinewidth=2,ecolor='red'))

russian_bar = ax.bar(ind+width+width, russian, width,
                    color='yellow',
                    error_kw=dict(elinewidth=2,ecolor='yellow'))

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,400)
ax.set_ylabel('Number of Relations')
ax.set_xlabel('Binned BLEU Score')
xTickMarks = ['[0-0.1)', '[0.1-0.2)', '[0.2-0.4)', '[0.4-0.6)', '[0.6-0.8)', '[0.8-1)', '[1]']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=30, fontsize=12)

## add a legend
ax.legend( (french_bar[0], hindi_bar[0], russian_bar[0]), ('French', 'Hindi', 'Russian'), loc=2)

plt.show()
