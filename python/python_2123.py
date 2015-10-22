# Running a python script on all the files in a directory
for f in *.csv; do
  python playlist.py "$f" "${f%.csv}list.txt"
done
