import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

img1 = mpl.image.imread('img/img1.jpg')#left image
img2 = mpl.image.imread('img/img2.jpg')#right image
fig, axs = plt.subplots(1,3)

idx_elem = 0
idx = 0

#for example we read only blue channel
A = img1[:,:,0]
B = img2[:,:,0]

idx_left = 0
idx_right = 0
min_times = 0
minsum =  np.sum(abs(A[:,-1] - B[:,0]))

#slice defect images that is why we use estimation: sum of the differens in pixel values
for j in range(B.shape[1]):
        b = B[:, j]
        k = np.sum(np.abs(A - b.reshape(-1,1)), axis=0)
        i = np.argmin(k)
        if (np.min(k) < minsum):
            idx_left = i
            idx_right = j
            minsum = np.min(k)
            min_times+=1

res_img = np.concatenate((A[:,:idx_left],B[:,idx_right:]), axis=1)

axs[0].imshow(img1)
axs[1].imshow(img2)
axs[2].imshow(res_img)

plt.show()