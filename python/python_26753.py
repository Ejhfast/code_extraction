# Calculating just a specific property in regionprops python
labels,num=label(image, return_num=True)
for i in range(num):
    area[i]=size(np.where(labels==i)[1])
