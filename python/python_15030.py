# Creating a folder and set as working directory for saving stdout files and images
import sys
filename = open(os.path.join('folder','filename.txt'),'w')
sys.stdout = filename
