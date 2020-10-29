# Fabric scripts

Here are example scripts using Fabric2.


# Setup

Tested on Debian10 Host. You need to install Python3 + PIP
(stock Debian offers only Fabric1 version) using these commands:

```bash
sudo apt-get install python3-pip python3-dev gcc make libffi-dev
sudo pip3 install fabric
```

# Running

To list all known tasks run:

```bash
$ fab -l
Available tasks:

  debian-all-upgrade
  debian-update
  free
```

NOTE: `fab` replaces function's underscores `_` with dashes `-`.

To run `uptime` task directly on this host, use:

```bash
fab uptime
```

More realistic example:
```bash
fab -H my-debian-host debian-update
```

WARNING! Fab will use SSH connection (or `~/.ssh/config`) to resolve
`my-debian-host`. If there is prompt for any password (user's password or ssh
key password) you must use correct argument to `fab` or run `ssh-agent`.



