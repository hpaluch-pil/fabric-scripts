
# Tasks for Debian an derivatives
from fabric import task

# Repository Update - safe
@task
def debian_update(c):
    c.run('sudo apt-get update')

# Does all: update, upgrade, dist-upgrade - potentially dangerous
@task
def debian_all_upgrade(c):
    c.run('sudo apt-get update')
    c.run('sudo apt-get -y upgrade', pty=True)
    c.run('sudo apt-get -y dist-upgrade', pty=True)


