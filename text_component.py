import bge
import enum
import time
from utils.timer import Timer
from collections import OrderedDict

if not hasattr(bge, "__component__"):
    global scene
    scene = bge.logic.getCurrentScene()

class TextComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([])

    def start(self, args):
        self.timer = Timer()

    def update(self):
        self.object.text = self.timer.__str__()