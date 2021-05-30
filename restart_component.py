import bge
from collections import OrderedDict

class RestartComponent(bge.types.KX_PythonComponent):
    
    args = OrderedDict([])

    def start(self, args):
        pass

    def update(self):
        keyboard = bge.logic.keyboard.inputs
        if keyboard[bge.events.RKEY].active:
            for scene in bge.logic.getSceneList():
                scene.restart()
            self.object.scene.end()