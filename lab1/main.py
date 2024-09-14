import cv2
import matplotlib.pyplot as plt

sq = cv2.imread('colors.jpeg')

fig, axs = plt.subplots(nrows=3, ncols=4)

# Исходное изображение RGB
rgb = cv2.cvtColor(sq, cv2.COLOR_BGR2RGB)
axs[0,0].set_title('Оригинал')
axs[0,0].imshow(rgb)
for i, n in enumerate(['R', 'G', 'B']):
    axs[0,i+1].axis('off')
    axs[0,i+1].set_title(n)
    axs[0,i+1].imshow(rgb[:,:,i], cmap='Greys_r')

# Вариант 3. RGB → XYZ → RGB;  
xyz = cv2.cvtColor(sq, cv2.COLOR_BGR2XYZ)
axs[1,0].set_title('XYZ')
axs[1,0].imshow(xyz)
for i, n in enumerate(['X', 'Y', 'Z']):
    axs[1,i+1].axis('off')
    axs[1,i+1].set_title(n)
    axs[1,i+1].imshow(xyz[:,:,i], cmap='Greys_r')

# RGB → YCbCr → RGB;
ycrcb = cv2.cvtColor(sq, cv2.COLOR_BGR2YCR_CB)
axs[2,0].set_title('YCbCr')
axs[2,0].imshow(ycrcb)
for i, n in enumerate(['Y', 'Cr', 'Cb']):
    axs[2,i+1].axis('off')
    axs[2,i+1].set_title(n)
    axs[2,i+1].imshow(ycrcb[:,:,i], cmap='Greys_r')
plt.show()
