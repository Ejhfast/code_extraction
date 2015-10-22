# How to git commit nothing without an error?
git add -A
git diff --quiet --exit-code --cached || git commit -m 'bla'
