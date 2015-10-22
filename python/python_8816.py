# Scientific image display python
from skimage import io, data
io.use_plugin('qt')
io.imshow(data.camera(), fancy=True)
