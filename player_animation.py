import bge
# from mathutils import Vector, Matrix


class PlayerAnimation(bge.types.BL_ArmatureObject):

    def __init__(self, old_owner, cont):
        self.cont = cont
        self.cont_update = None
        self.character = None
        self.click_attack = False

    def start(self):
        self.character = bge.constraints.getCharacter(self.parent)
        self.__lastPosition = self.worldPosition.copy()
        self.__moveDirection = None
    
    def update(self):
        self.__reset_animations()
        self.__moveDirection = self.worldPosition - self.__lastPosition
        self.__lastPosition = self.worldPosition.copy()

        if self.character.onGround:
            self.__handleGroundAnimations()
        else:
           self.__animate(['salto', 21, 21])
    
    def __reset_animations(self):
        if self.getActionFrame() > 36 and self.getActionName() == 'player_attack':
            self['attack'] = False
            self.parent['attack'] = False
 
    def __handleGroundAnimations(self):
        mouse = bge.logic.mouse.inputs
        keyTAP = bge.logic.KX_INPUT_JUST_ACTIVATED

        if self.getActionFrame() > 31 and self.getActionFrame() < 32 and self.getActionName() == 'player_attack':
            self.add_collision()

        if keyTAP in mouse[bge.events.LEFTMOUSE].queue:
            self.parent['attack'] = True
            self['attack'] = True
            self.__animate(['player_attack', 1, 37], blend=4)
        
        speed = self.__moveDirection.length
        
        if speed <= 0.003 and not self['attack']:
            self.__animate(['Idle_payer', 1, 301], blend=6)
        elif not self['attack']:
            self.__animate(['running', 1, 23], blend=6)

    def __animate(self, anim_data: list, blend=4):
        self.playAction(anim_data[0], anim_data[1], anim_data[2], blendin=blend)
    
    def add_collision(self):
        self.controllers[3].activate(self.actuators['add_collision'])


#Modules
def start(cont):
    player_animation = PlayerAnimation(cont.owner, cont)
    player_animation.start()

def update(cont):
    cont.owner.update()