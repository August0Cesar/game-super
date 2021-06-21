import bge
from collections import OrderedDict
from mathutils import Vector

from utils.animate import animate

class PlatformJump(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("delay", 120)
    ])

    def start(self, args):
        self.delay_count = 0
        self.delay = args["delay"]
        self.frame_to_push = 0
        self.is_play_anim_push = False

    def update(self):
        self.delay_count += 1
        
        if self.object["is_scale"] and self.delay_count == self.delay:
            animate(armature=self.object, name="Scale", start_frame=1, end_frame=22)
        
        if self.object.get("is_scale", True) and self.delay_count > self.delay:
            self.delay_count = 0


