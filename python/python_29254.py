# Docker: How to run cython_extensions?
RUN source /home/ubuntu/canonicaliser_api/venv/bin/activate &amp;&amp; cd /home/ubuntu/canonicaliser_api/canonicaliser/cython_extensions/ &amp;&amp; python setup.py build_ext --inplace
