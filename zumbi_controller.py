import bge
from state_zumbi import StateZumbiEnum
from tools_games import follow_direction

if not hasattr(bge, "__component__"):
    global scene
    scene = bge.logic.getCurrentScene()

'''
IA Enemy
Para o script funcionar é preciso criar uma property chamada states do tipo int
e um sensor near chamado near_player e um actuator Edit Object chamado see_enemy
'''

def start(cont):
    cont.owner['estates'] = StateZumbiEnum.IDLE.value
    

def update(cont):
    enemy = cont.owner
    if not enemy['name_player_controller'] in scene.objects:
        return
        
    cube_player_controller = scene.objects[enemy['name_player_controller']]
    

    distance_player = enemy.getDistanceTo(cube_player_controller)
    armature_enemy = enemy.childrenRecursive['Armature_Enemy']
    sensor_near_player = cont.sensors["near_player"]

    if enemy['vida'] <= 0:
        enemy['estates'] = StateZumbiEnum.DEATH.value
    
    
    if enemy['estates'] == StateZumbiEnum.IDLE.value:
    
        armature_enemy.playAction("Zumbi_idle", 1, 142, priority=1, blendin=4,
                                    play_mode=bge.logic.KX_ACTION_MODE_LOOP)
        if sensor_near_player.positive:
            enemy['estates'] = StateZumbiEnum.PERSEGUIR.value  

    elif enemy['estates'] == StateZumbiEnum.PERSEGUIR.value:
        # olhar player
        cont.actuators['see_enemy'].object = cube_player_controller
        cont.activate(cont.actuators['see_enemy'])
        
        if distance_player <= 2: # Perto do Player
            enemy['estates'] = StateZumbiEnum.ATTACK.value
        else:
            __animate(armature_enemy, "Zumbi_running", 1, 25)
            __follow_player(enemy, cube_player_controller) 

    elif enemy['estates'] == StateZumbiEnum.ATTACK.value: 
        if armature_enemy.getActionFrame() > 32 and armature_enemy.getActionFrame() < 33:
            cont.activate(armature_enemy.actuators['add_collision'])

        if armature_enemy.getActionFrame() > 52 and distance_player > 2:
                enemy['estates'] = StateZumbiEnum.PERSEGUIR.value

        __animate(armature_enemy, "Zumbi_attack", 1, 53)

    elif enemy['estates'] == StateZumbiEnum.DEATH.value:
        __animate(armature_enemy, "Zumbi_death", 1, 103)
        if armature_enemy.getActionFrame() > 100:
            enemy.endObject()


def __follow_player(enemy, cube_player_controller):
    location_to_player = enemy.getVectTo(cube_player_controller)
    speed = 25
    enemy.applyMovement(location_to_player[1]/ speed) 

def __animate(armature, name, start_frame, end_frame, blend=4):
		"""Runs an animation"""
		armature.playAction(name, start_frame, end_frame, blendin=blend)