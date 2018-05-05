import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
import shutil
import os


def genGif(images):
    out = []
    print("#######################")
    print("Generating gif")
    for filename in images:
        out.append(imageio.imread(filename))
    imageio.mimsave('numbers.gif', out)
    shutil.rmtree('tmp')
    print("Done!")


print("Compute the XOR between a range of integears ad display a 3D Plot")
print("The graph will show Z = X XOR Y")
fr = int(input("From: "))
to = int(input("To: "))
gif = input("Generate gif?[Y]/n: ")
x = []
images = []
for i in range(fr, to):
    x.append(i)

print(x, gif)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for i in x:
    for i1 in x:
        ax.scatter(i, i1, i ^ i1, c="b", marker='o')

if not gif:
    os.mkdir("tmp/")
    for angle in range(0, 180):
        ax.view_init(25, angle)
        name = "tmp/num"+str(angle)+".png"
        print("Generating ", name)
        images.append(name)
        plt.savefig(name)
    genGif(images)
else:
    plt.show()
