import bge
from state_zumbi import StateZumbiEnum

'''
IA Enemy
Para o script funcionar é preciso criar uma property chamada states do tipo int
e um sensor near chamado near_player e um actuator Edit Object chamado see_enemy
'''

def start(cont):
    cont.owner['estates'] = StateZumbiEnum.IDLE.value
    

def update(cont):
        
    cube_player_controller = cont.owner.scene.objects["cube_player_controller"]
    

    distance_player = cont.owner.getDistanceTo(cube_player_controller)
    armature_enemy = cont.owner.childrenRecursive['Armature_Enemy']
    sensor_near_player = cont.sensors["near_player"]

    if cont.owner['vida'] <= 0:
        cont.owner['estates'] = StateZumbiEnum.DEATH.value
    
    
    if cont.owner['estates'] == StateZumbiEnum.IDLE.value:
    
        armature_enemy.playAction("Zumbi_idle", 1, 142, priority=1, blendin=4,
                                    play_mode=bge.logic.KX_ACTION_MODE_LOOP)
        if sensor_near_player.positive:
            cont.owner['estates'] = StateZumbiEnum.PERSEGUIR.value  

    elif cont.owner['estates'] == StateZumbiEnum.PERSEGUIR.value:
        # olhar player
        cont.actuators['see_enemy'].object = cube_player_controller
        cont.activate(cont.actuators['see_enemy'])
        
        if distance_player <= 2: # Perto do Player
            cont.owner['estates'] = StateZumbiEnum.ATTACK.value
        else:
            __animate(armature_enemy, "Zumbi_running", 1, 25)
            __follow_player(cont.owner, cube_player_controller) 

    elif cont.owner['estates'] == StateZumbiEnum.ATTACK.value: 
        if armature_enemy.getActionFrame() > 32 and armature_enemy.getActionFrame() < 33:
            cont.activate(armature_enemy.actuators['add_collision'])

        if armature_enemy.getActionFrame() > 52 and distance_player > 2:
                cont.owner['estates'] = StateZumbiEnum.PERSEGUIR.value

        __animate(armature_enemy, "Zumbi_attack", 1, 53)

    elif cont.owner['estates'] == StateZumbiEnum.DEATH.value:
        __animate(armature_enemy, "Zumbi_death", 1, 103)
        if armature_enemy.getActionFrame() > 100:
            cont.owner.endObject()


def __follow_player(enemy, cube_player_controller):
    location_to_player = enemy.getVectTo(cube_player_controller)
    speed = 25
    enemy.applyMovement(location_to_player[1]/ speed) 

def __animate(armature, name, start_frame, end_frame, blend=4):
		"""Runs an animation"""
		armature.playAction(name, start_frame, end_frame, blendin=blend)