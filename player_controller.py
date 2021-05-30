import bge
from mathutils import Vector, Matrix


class PlayerController(bge.types.KX_GameObject):
    

    def __init__(self, old_owner, cont):
        self.cont = cont
        self.value_attack = 40
        self.is_collision = False
        self.move_speed = 0
        self.walkSpeed = 0.1
        self.character = None
        self.arm = None

    def start(self):
        self.character = bge.constraints.getCharacter(self)

    def update(self):
        if self['estates'] == 0:
            self.character_movement()
            self.character_jump()
    
    def character_jump(self):
        keyboard = bge.logic.keyboard.inputs
        keyTAP = bge.logic.KX_INPUT_JUST_ACTIVATED

        if keyTAP in keyboard[bge.events.SPACEKEY].queue:
            self.character.jump()
    
    def character_movement(self):
        keyboard = bge.logic.keyboard.inputs

        x = 0
        y = 0
        speed = self.walkSpeed

        if keyboard[bge.events.WKEY].active and not self['attack']:
            y = 1
        elif keyboard[bge.events.SKEY].active and not self['attack']: 
            y = -1

        if keyboard[bge.events.AKEY].active and not self['attack']:   
            x = -1
        elif keyboard[bge.events.DKEY].active and not self['attack']: 
            x = 1

        vec = Vector([x, y, 0])
        if vec.length != 0:
            vec.normalize()
            vec *= speed
        if self['attack']:
            vec = Vector([0, 0, 0])
        self.character.walkDirection = self.worldOrientation * vec
    
    def __animate(self, animData, blend=4):
        self.playAction(animData[0], animData[1], animData[2], blendin=blend)


#Modules
def start(cont):
    player = PlayerController(cont.owner, cont)
    player.start()

def update(cont):
    cont.owner.update()