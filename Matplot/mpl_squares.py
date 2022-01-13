import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_x = [1, 2, 3, 4, 5]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_x, squares, linewidth = 3)

ax.set_title("Squares", fontsize = 24)
ax.set_xlabel("x", fontsize = 14)
ax.set_ylabel("y=x^2", fontsize = 14)

ax.tick_params(axis='both', labelsize = 14)

plt.show()