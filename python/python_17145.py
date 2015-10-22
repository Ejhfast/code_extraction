# Error with PyOpenGL and glutSolidCylinder
quadratic = gluNewQuadric()
gluCylinder(quadratic, BASE, TOP, HEIGHT, SLICES, STACKS)      # to draw the lateral parts of the cylinder;
gluDisk(quadratic, INNER_RADIUS, OUTER_RADIUS, SLICES, LOOPS)  # call this two times in the appropriate environment to draw the top and bottom part of the cylinder with INNER_RADIUS=0.
