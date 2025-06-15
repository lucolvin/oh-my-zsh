#!/usr/bin/env python3
import os
import subprocess
import sys
from security import safe_command

ssh_proxy = os.path.join(os.path.dirname(__file__), "ssh-proxy.py")

argv = [
    os.environ.get("NAME", "ssh"),
    "-o",
    "ProxyCommand={} %h %p".format(ssh_proxy),
    "-o",
    "Compression=yes",
]

safe_command.run(subprocess.call, argv + sys.argv[1:], env=os.environ)
