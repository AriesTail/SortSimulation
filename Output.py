import random

from matplotlib import animation
from matplotlib import pyplot as plt

from Sort.Sorts import SortMethonds

plt.rcParams['animation.ffmpeg_path'] = 'C:/Eclipse Workspace/ffmpeg-20191120-d73f062-win64-static/bin/ffmpeg.exe'
Data_count = 100


def draw_chart(original_data):
    sortMethonds = SortMethonds(original_data)
    frames = sortMethonds.bubbleSort()
#     frames = [sortMethonds.bubbleSort(), sortMethonds.insertSort(), sortMethonds.selectSort(), sortMethonds.mergeSort(), sortMethonds.quickSort2()]
    
    fig = plt.figure(1)
    axs = fig.add_subplot()
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)
    
    def animate(frame):
        bars = []
        if(len(frames) > frame):
            axs.cla()
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Data_count)), [d for d in frames[frame]], 1,).get_children()
        return bars

    anim = animation.FuncAnimation(fig, func=animate, frames=len(frames), interval=50, repeat=False)
    return plt, anim


dataset = list(range(1, Data_count + 1))
random.shuffle(dataset)
plt, _ = draw_chart(dataset)
plt.show()

# default_fn = "1"
# fps = 25
# _, anim = draw_chart(dataset)
# anim.save('1.mp4', writer=animation.FFMpegWriter(fps=fps, extra_args=['-vcodec', 'libx264']))
