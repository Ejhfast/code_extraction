# getting label's date using python and p4v
label = os.popen("sc labels -e the_label_name")
label = label.read()
