import os
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

###########################
#### BLUEPRINT CONFIGS ####
###########################

# Import these at the top if you want
# We've imported them here for easy reference
from Project.core.views import core
