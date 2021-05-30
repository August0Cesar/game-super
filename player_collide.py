import bge

class PlayerCollide(bge.types.KX_GameObject):
    

    def __init__(self, old_owner, cont):
        self.cont = cont
        self.value_attack = 20
        self.is_collision = False

    def start(self):
        self.collisionCallbacks.append(self.__onCollision)

    def update(self):
        ...
    
    def __onCollision(self, obj):
        if not obj is None:
            if 'enemy' == obj['enemy'] and not self.is_collision:
                obj.actuators["Damage"].startSound()
                if 'enemy_mash' in obj.childrenRecursive:
                    obj.childrenRecursive['enemy_mash'].playAction("Damage", 1, 15, blendin=4)
                else:
                    obj.childrenRecursive['enemy_mash_2'].playAction("Damage", 1, 15, blendin=4)
                obj['vida'] -= self.value_attack
                self.is_collision = True

#Modules
def start(cont):
    old_object = cont.owner
    mutated_object = PlayerCollide(cont.owner, cont)
    mutated_object.start()

def update(cont):
    cont.owner.update()