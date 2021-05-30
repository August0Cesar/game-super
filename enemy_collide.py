import bge

class EnemyCollide(bge.types.KX_GameObject):
    

    def __init__(self, old_owner, cont):
        self.cont = cont
        self.value_attack = 5
        self.is_collision = False

    def start(self):
        self.collisionCallbacks.append(self.__onCollision)

    def update(self):
        pass
    
    def __onCollision(self, obj):
        if 'cube_player_controller' == obj.name and not self.is_collision:
            self.is_collision = True
            obj['vida'] -= self.value_attack

#Modules
def start(cont):
    old_object = cont.owner
    mutated_object = EnemyCollide(cont.owner, cont)
    mutated_object.start()

def update(cont):
    cont.owner.update()