import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()

x_values = range(1,1001)
y_values = [x*x for x in x_values]

ax.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues ,s=10)

ax.set_title("Squares", fontsize=24)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y=x^2", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.show()

# plt.savefig("squares_plot.jpg", bbox_inches='tight')