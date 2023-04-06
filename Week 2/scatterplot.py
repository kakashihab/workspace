from matplotlib import pyplot as plt

widgets = [5, 7, 9, 13, 86, 103]
gromits = [23, 38, 77, 102, 165, 198]
labels = ["Alice", "Bob", "Carol", "Derek", "Ernie", "Fiona"]

plt.scatter(widgets, gromits)

for label, widget, gromit in zip(labels, widgets, gromits):
    plt.annotate(label, xy=(widget, gromit), xytext=(5,-5), textcoords="offset points")
plt.xlabel("Widgets")
plt.ylabel("Gromits")
plt.title("Widgets and Gromits")
plt.show()