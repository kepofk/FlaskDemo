#!/bin/bash

ENV_NAME=venv

#https://github.com/ContinuumIO/anaconda-issues/issues/6917

python -m venv ${ENV_NAME} --without-pip
source ${ENV_NAME}/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python


#pip
pip install flask #Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.5 click-7.0 flask-1.1.1 itsdangerous-1.1.0
pip install unicorn #gunicorn-19.9.0
