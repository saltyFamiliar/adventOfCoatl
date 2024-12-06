import numpy as np

d = np.loadtxt("input.txt")

d.sort(axis=0)
print("silver: ", np.sum(np.absolute(np.diff(d, axis=1))))

# hmap = dict(np.array(np.unique_counts(d[:, 1])).T)
# f = np.vectorize(lambda x: x * hmap[x] if x in hmap else 0)
# print("gold: ", np.sum(f(d[:, 0])))

unique_values, counts = np.unique(d[:, 1], return_counts=True)

# Create an array of zeros to hold the counts for the first column values
counts_array = np.zeros(d[:, 0].shape, dtype=int)

# Populate the counts array
for value, count in zip(unique_values, counts):
    counts_array[d[:, 0] == value] = count

# Multiply the values in the first column by their corresponding counts and sum the result
result = np.sum(d[:, 0] * counts_array)

print("gold: ", result)
