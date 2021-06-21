import bge
from collections import OrderedDict

class Component(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
        ("speed", 10) 
    ])

    def start(self, args):
        if not "Interface_Game_Play" in bge.logic.getSceneList():
            # bge.logic.addScene("Interface_Game_Play")
            bge.logic.addScene("Interface_Game_BG-UI")

    def update(self):
        cube_controller = self.object.parent
        
        if cube_controller['vida'] <= 0:
            
            if not "Interface_Game_Over" in bge.logic.getSceneList():
                bge.logic.addScene("Interface_Game_Over")
            bge.logic.getCurrentScene().suspend()
        direction = bge.constraints.getCharacter(cube_controller).walkDirection
        
        self.follow_direction(direction)

    def follow_direction(self, direction):
        if direction.length != 0:
            self.object.alignAxisToVect(direction, 1, 0.5)
            self.object.alignAxisToVect([0, 0, 1], 2, 1)