

virtualenv --distribute --no-site-packages /tmp/env
. /tmp/env/bin/activate
/tmp/env/bin/python setup.py install -n
deactivate
