import os
import json
from definition import *


class info:

    def __init__(self):
        pass

    def getinfo(self):
        data = json.loads(open(information_file).read())
        return data