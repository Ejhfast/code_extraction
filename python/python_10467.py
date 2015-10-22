# Save frame from webcam to disk with opencv python bindings
if k == 0x63 or k == 0x43:
    print 'capturing!'
    cv.SaveImage("test.jpg",frame)
