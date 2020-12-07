import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

img1 = mpl.image.imread('img/image1.jpg')#left image
img2 = mpl.image.imread('img/image2.jpg')#right image
fig, axs = plt.subplots(1,3)

idx_elem = 0
idx = 0


A = img1[:,:,:]
B = img2[:,:,:]

idx_left = 0
idx_right = 0
min_times = 0
minsum =  np.sum(abs(A[:,-1,:] - B[:,0,:]))

#slice defect images that is why we use estimation: sum of the differens in pixel values
for i in reversed(np.arange(img1.shape[1])):
    for j in np.arange(img2.shape[1]):


        x = A[:,i,:]
        y = B[:,j,:]
        k = np.sum(abs(x-y))
        if (k < minsum):
            idx_left = i
            idx_right = j
            minsum = k
            min_times+=1
        elif (min_times > 6):#unnececary but speeds up splice significantly
            break
res_img = np.concatenate((A[:,:idx_left,:],B[:,idx_right:,:]), axis=1) 
#res_img = B[:,:,:]
axs[0].imshow(img1)
axs[1].imshow(img2)
axs[2].imshow(res_img)

plt.show()