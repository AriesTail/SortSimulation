import random

from matplotlib import animation
from matplotlib import pyplot as plt

from Main.Data import Data
from Sort.Sorts import SortMethonds

Data.data_count = 100


def draw_chart(stype, original_data):
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Data(d) for d in original_data]
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)
    
    sortMethonds = SortMethonds(original_data)
    frames = sortMethonds.mergeSort()
    title = ""

    def animate(fi):
        bars = []
        if(len(frames) > fi):
            axs.cla()
            axs.set_title("1")
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Data.data_count)),  # X
                            [d for d in frames[fi]],  # data
                            1,  # width
                            ).get_children()
        return bars

    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=1)
    return plt, anim


od = list(range(1, Data.data_count + 1))
random.shuffle(od)
plt, _ = draw_chart(0, od)
plt.show()
