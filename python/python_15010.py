# resize image with PythonMagick
i = PythonMagick.Image(img)
i.sample('!&lt;width&gt;x&lt;height&gt;')
