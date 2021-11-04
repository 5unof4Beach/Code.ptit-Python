from matplotlib import pyplot as plt

# plt.style.use("fivethirtyeight")

slices = [200,400]
labels = ["expense","income"]

plt.pie(slices, labels = labels)
plt.title("Thong ke")
plt.show()