# -*- coding: utf-8 -*-
# cli.py

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import sys

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def main():
    if len(sys.argv) == 2 and sys.argv[1].lower() == 'init':
        from .app import app
        app.init()


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
    main()
