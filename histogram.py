import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 6
french = [72.3, 75.9, 78.0, 79.5, 80.9, 80.1]
hindi = [74.7, 77.2, 78.6, 80.6, 81.3, 81.7]

fr_err = [2.05, 1.96, 1.9, 1.85, 1.8, 1.83]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.30                      # the width of the bars

## the bars
french_bar = ax.bar(ind, french, width,
                color='red',
                error_kw=dict(elinewidth=2,ecolor='black'),
		yerr=fr_err)

hindi_bar = ax.bar(ind+width, hindi, width,
                    color='blue',
                    error_kw=dict(elinewidth=2,ecolor='black'))

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(70,83)
ax.set_ylabel('Accuracy')
ax.set_xlabel('Vector length (D/K)')
xTickMarks = ['50 - 250', '100 - 500', '200 - 1000', '300 - 1500', '500 - 2500',
              '600 - 3000']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=30, fontsize=12)

## add a legend
ax.legend( (french_bar[0], hindi_bar[0]), ('Dense', 'Binary'), loc=2)

plt.show()
