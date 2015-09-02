activate_this = '/usr/local/src/pinisi/env/bin/activate'
execfile(activate_this, dict(__file__=activate_this))
import sys

sys.path.insert(0, '/usr/local/src/pinisi')

from app import app as application
