# shows debug info only for people who are listed in DEBUG_IPS
export DEBUG_IPS='['YOUR_VALUE_HERE', 'YOUR_VALUE_HERE', 'YOUR_VALUE_HERE']'

# deactivates the sites for maintenance
# use maintenance instead of debug in production
export MAINTENANCE=False

# DEBUG Info
# if DEBUG is ON, Maintenance mode will be ignored and DEBUG info will be shown
# to everyone! so always use Maintenance mode in production.
export DEBUG=False

# Security Conf
export SECRET_KEY='YOUR_VALUE_HERE'
export ALLOWED_HOSTS='['YOUR_VALUE_HERE', 'YOUR_VALUE_HERE', 'YOUR_VALUE_HERE']'

# DB conf
export DB_NAME='YOUR_VALUE_HERE'
export DB_USER='YOUR_VALUE_HERE'
export DB_PASSWORD='YOUR_VALUE_HERE'
export DB_HOST='localhost'
export DB_PORT=''

# STATIC AND MEDIA URL  
export STATIC_URL=''
export MEDIA_URL=''

# STATIC AND MEDIA ROOT 
export STATIC_ROOT=''
export MEDIA_ROOT=''

