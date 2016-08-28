# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/pinisi'
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "\xfd\x14\x17\xa9\xe9\x95\xc1t1\xc7Z{\x01Xz\x04*iY4[?\xfbg"

# Secret key for signing cookies
SECRET_KEY = "g\xfb?[4Yi*\x04zX\x01{Z\xc71t\xc1\x95\xe9\xa9\x17\x14\xfd"

# Mandrill
MANDRILL_API_KEY = ''
MANDRILL_DEFAULT_FROM = ''