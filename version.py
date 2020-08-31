from __future__ import division, print_function
import os
import shutil
import numpy as np
import zipfile
import glob
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
from tensorflow.keras.models import load_model
from flask import Flask, send_file, url_for, request, render_template
from werkzeug.utils import secure_filename
import flask
import werkzeug
print()
print("flask {}".format(flask.__version__))
print('Pandas {}'.format(werkzeug.__version__))

