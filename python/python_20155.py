# Call exe from python script
cmd = "colorDescriptor %s --detector harrislaplace --descriptor sift --output %s.txt " % (imagepath, imagepath)
    os.popen(cmd)
