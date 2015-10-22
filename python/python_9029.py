# Using glGetFloatv to retrieve the modelview matrix in pyglet
a = (GLfloat * 16)()
  mvm = glGetFloatv(GL_MODELVIEW_MATRIX, a)
  print list(a)
