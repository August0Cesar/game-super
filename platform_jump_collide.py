import bge
from collections import OrderedDict
from mathutils import Vector

from utils.animate import animate

class PlatformJumpCollide(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.platform = self.object.scene.objects["Plataform_Jump_without_base"]
        self.object_hit = None
        self.object.collisionCallbacks.append(self.on_collision)

    def update(self):
        self.verify_animate_to_push()
        
    def verify_animate_to_push(self):
        if self.object.isPlayingAction() and self.object.getActionName() == "Copy_Location":
            if int(self.object.getActionFrame()) == 5:
                character = bge.constraints.getCharacter(self.object_hit)
                character.jumpSpeed = 30
                character.jump()
        else:
            if self.object_hit:
                character = bge.constraints.getCharacter(self.object_hit)
                character.jumpSpeed = 15
            self.platform["is_scale"] = True
    
    def on_collision(self, object_collide):
        if not object_collide is None:
            self.object_hit = object_collide
            self.platform["is_scale"] = False
            animate(armature=self.object, name="Copy_Location", start_frame=1, end_frame=13)
            animate(armature=self.platform, name="Push", start_frame=1, end_frame=23)
            
            
