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
fab -l
```

To run `uptime` tasks on this host, use:

```bash
fab uptime
```


TODO: ...
