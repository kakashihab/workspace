from matplotlib import pyplot as plt

countries = ["China", "India", "USA", "Indonesia", "Pakistan",
            "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]
populations = [1401.5, 1359.3, 329.4, 265.0, 208.2, 211.2, 188.5, 168.2, 146.9, 126.6]

plt.bar(range(len(countries)), populations)
plt.xticks(range(len(countries)), countries)
plt.title("Highest population countries")
plt.ylabel("Millions")

plt.show()