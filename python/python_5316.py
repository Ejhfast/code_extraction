# Read/Write files in Python
def main():
    path = "C:\\temp\\log.txt"
    os.chmod(path, stat.S_IWRITE)
