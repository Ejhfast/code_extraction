# Python lambda with complex number
part = lambda theta,phi, x=x, y=y, z=z, k=k: (N.cos(theta)**(0.5))*N.sin(theta)*N.exp(-1j*k*(x*N.sin(theta)*N.cos(phi) + y*N.sin(theta)*N.sin(phi) - z*N.cos(theta)))
