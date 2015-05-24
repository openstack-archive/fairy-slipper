# -*- mode: python -*-
from os import path
from pecan.deploy import deploy
pathname = path.join(path.abspath(path.dirname(__file__)), 'config.py')
application = deploy(pathname)
