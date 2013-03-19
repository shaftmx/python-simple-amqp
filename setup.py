#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: setup.py,v 0.2.3.4 2013-02-27 09:56:56 gaelL Exp $
#
# Copyright (C) 2010-2013  Gaël Lambert (gaelL) <gael@gael-lambert.org>
#
# You can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

if __name__ == '__main__':

    setup(name='simple-amqp',
        version='0.0.0.1',
        description='Simple amqp',
        long_description="""Simple lib to use rabbitmq with a pool of server""",
        author='Gaël Lambert (gaelL)',
        author_email='gael@gael-lambert.org',
        maintainer='Gaël Lambert (gaelL)',
        maintainer_email='gael@gael-lambert.org',
        keywords=['rabbitmq','amqp'],
        url='https://github.com/shaftmx/python-simple-amqp',
        license='GNU Affero General Public License v3',
        packages = ['simpleamqp'],
        package_dir = {'simpleamqp':'src/simpleamqp'},   
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Advanced End Users',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
            'Operating System :: POSIX',
            'Programming Language :: Python',
            'Topic :: System'
        ],
    )
