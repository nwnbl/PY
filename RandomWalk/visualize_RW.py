from Random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
    RW_scatters = RandomWalk(5000)
    RW_scatters.fill_walk()

    plt.style.use('seaborn')

    fig, ax = plt.subplots(figsize = (16, 9), dpi = 128)

    point_numbers = range(RW_scatters.num_points)

    ax.scatter(RW_scatters.x_values, RW_scatters.y_values, c=point_numbers, cmap=plt.cm.winter, edgecolors='none', s=10)

    ax.set_title("Random Walk", size=24)
    ax.set_xlabel("X", size=14)
    ax.set_ylabel("Y", size=14)

    ax.tick_params(axis='both', size=14)

    # ax.axis([-500, 500, -500, 500])

    plt.show()
    keep_running = input("Another round? (y/n): ")
    if keep_running == 'n':
        break
