import bge
from collections import OrderedDict
from mathutils import Vector

class DialogComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.is_up = False
        self.is_key_m = False
        self.is_key_z = False
        scene_dialog = bge.logic.getSceneList()["scene_dialog"]
        self.plane_dialog = scene_dialog.objects["plane_dialog"]

    def update(self):
        keyboard = bge.logic.keyboard
        
        if keyboard.inputs[bge.events.MKEY].active and not self.is_key_m:
            self.is_key_z = False
            self.is_key_m = True
            self.is_up = True
            self.plane_dialog.localPosition += Vector((0.0, 4.0, 0.0)) 
        
        if keyboard.inputs[bge.events.ZKEY].active and not self.is_key_z:
            self.is_key_z = True
            self.is_key_m = False
            self.is_up = False
            self.plane_dialog.localPosition += Vector((0.0, -4.0, 0.0)) 
        