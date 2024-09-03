#!/usr/bin/env python3
import os
import subprocess
import sys
import urllib.parse
from security import safe_command

proxy = next(os.environ[_] for _ in ("HTTP_PROXY", "HTTPS_PROXY") if _ in os.environ)
argv = [
    "nc",
    "-X",
    "connect",
    "-x",
    urllib.parse.urlparse(proxy).netloc,  # proxy-host:proxy-port
    sys.argv[1],  # host
    sys.argv[2],  # port
]

safe_command.run(subprocess.call, argv)
