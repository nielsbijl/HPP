from matplotlib import pyplot as plt


processes = [1, 2, 4, 8, 16, 32]
time = [343, 278, 158, 109, 100, 100]


fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

# Set titles for the figure and the subplot respectively
fig.suptitle('system: 8 processors and 4 cores', fontsize=14, fontweight='bold')
ax.set_title('Circuit satisfiablility problem')

ax.set_xlabel('processes')
ax.set_ylabel('time (s)')

ax.plot(processes, time)

plt.show()