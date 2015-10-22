# Using Bitmap.LockBits and Marshal.Copy in IronPython not changing image as expected
for y in range(bmData.Height):
    for x in range(bmData.Width):
        rgbValues[(bmData.Stride * y) + (3 * x) +2] = 255
