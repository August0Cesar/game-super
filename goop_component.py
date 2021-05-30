import bge
import enum
import time
from random import randint
from utils.animate import animate
# from mathutils import *
from collections import OrderedDict

if not hasattr(bge, "__component__"):
    global scene
    scene = bge.logic.getCurrentScene()

class GoopComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("speed", 10)
    ])

    def start(self, args):
        self.play_animation = False
        self.armature = self.object.childrenRecursive["arm_goop"]
        

    def update(self):
        if self.object["estado"] == StateGoopEnum.IDLE.value:
            animate(armature=self.armature, name="idle_goop", start_frame=1, end_frame=20)
        
        if self.object["estado"] == StateGoopEnum.PATRULHA.value: # Patrulha
            pass

        if self.object["estado"] == StateGoopEnum.ATTACK.value:
            animate(armature=self.armature, name="attack_goop.001", start_frame=1, end_frame=18)

            if self.armature.getActionFrame() > 5 and not self.armature.getActionFrame() < 9:
                self.armature["start_collide"] = True
            else:
                self.armature["start_collide"] = False

class StateGoopEnum(enum.Enum):
   IDLE = 0
   PATRULHA = 1
   ATTACK = 3
   DEATH = 4