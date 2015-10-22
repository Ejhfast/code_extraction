# Virtualenvs won't work after switching from 64 to 32-bit Python on OSX
pip freeze -E lepoc &gt; requirements.txt
pip install -E newve -r /path/to/pip-requirements.txt
