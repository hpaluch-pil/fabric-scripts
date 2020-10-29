
# "read-only" tasks for Fabric2
from fabric import task

@task
def uptime(c):
    c.run('uptime')



