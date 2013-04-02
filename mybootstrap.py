
#virtualenv --distribute --no-site-packages /tmp/env
#. /tmp/env/bin/activate
#/tmp/env/bin/python setup.py install -n
#deactivate

import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess
def after_install(options, home_dir):
    etc = join(home_dir, 'etc')
    if not os.path.exists(etc):
        os.makedirs(etc)
    # Get depends
    subprocess.call([join(home_dir, 'bin', 'pip'),
                    'install', 'pika'])
    subprocess.call([join(home_dir, 'bin', 'pip'),
                    'install', 'unittest2'])
    activate = "%s/bin/activate" % home_dir
    # Install
    mycmd = "python setup.py install -v"
    pipe = subprocess.Popen(". %s; %s" % (activate, mycmd),
                            stdout=subprocess.PIPE, shell=True)
    print pipe.communicate()[0]
    # Launch unittest
    mycmd = "python run_tests"
    pipe = subprocess.Popen(". %s; %s" % (activate, mycmd),
                            stdout=subprocess.PIPE, shell=True)
    print pipe.communicate()[0]
    print 'debug2'
def adjust_options(options, args):
    args.append('MYENV')
    options.use_distribute = True
    options.no_site_packages = True
"""))
f = open('python-simple-amqp-env-bootstrap.py', 'w').write(output)
