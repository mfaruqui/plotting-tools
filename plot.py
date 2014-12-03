import matplotlib.pyplot as plt
import matplotlib

font = {'family' : 'normal', 'weight' : 'normal', 'size'   : 15}
matplotlib.rc('font', **font)

vec_len = [50, 100, 200, 300, 500, 1000]
orig = [56, 62.4, 67.2, 68.8, 70.5, 71.5]
retro = [60.7, 66.1, 70.1, 71.6, 72.9, 73.6]
plt.plot(vec_len, retro, marker='o', linestyle='--', color='r', label='SG + Retrofitting')
plt.plot(vec_len, orig, marker = 'x', label='SG')
plt.xlabel('Vector length')
plt.ylabel("Spearman's correlation")
#plt.title('xyz')
plt.legend(loc=4)
plt.show()
