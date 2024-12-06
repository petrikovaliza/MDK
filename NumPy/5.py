import numpy as np
from PIL import Image

image = np.array(Image.open("pelmeshek.jpg"))

image_R = image.copy()
image_R[:, :, (1, 2)] = 0
image_B = image.copy()
image_B[:, :, (0, 1)] = 0

image_1 = Image.fromarray(image_R)
image_2 = Image.fromarray(image_B)

result = Image.new("RGB", (image.shape[1]*2, image.shape[0]))
result.paste(image_1, (0,0))
result.paste(image_2, (image.shape[1],0))

result.save("result.png", format="PNG")
