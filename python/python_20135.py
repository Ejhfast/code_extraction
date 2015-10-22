# write to file with tee command in python
fileName = "file_Iter" + str(It) + "_V_" +str(V)+".txt"
file_out=io.open(fileName, 'w')
os.system("echo - START RUN $(LANG=en_US date +%b_%d_%Y_%k_%M)- | tee -a " + fileName)
