'''
To install it on anaconda
pip install -i https://pypi.anaconda.org/pypi/simple pyttsx
'''

import pyttsx
engine = pyttsx.init()
engine.say('What the hell are you doin')
engine.runAndWait()
