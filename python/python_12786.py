# Using Fabric to deploy current git branch to heroku
from fabric.api import local
my_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
