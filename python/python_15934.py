# package creation file doesnot take value from .bashrc file
import OS
  os.environ['product']='product1'
  subprocess.call("make clean", shell=True)
