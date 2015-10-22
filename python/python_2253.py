# Pyglet OpenGL drawing anti-aliasing
config = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(config=config, resizable=True)
