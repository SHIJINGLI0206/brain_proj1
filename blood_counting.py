import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import patches

# read the csv file using read_csv function of pandas
train = pd.read_csv('blood_cell.csv')
print(train.head())

# reading single image using imread function of matplotlib
image = plt.imread('BCCD/JPEGImages/1.jpg')
plt.imshow(image)
plt.show()

# Number of unique training images
train['image_names'].nunique()
