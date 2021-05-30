import bge
from mathutils import Vector
from collections import OrderedDict
from utils.animate import animate


class Component(bge.types.KX_PythonComponent):
    
    args = OrderedDict([
        ("Time push", 15),
        ("Time pull", 15)
    ])

    def start(self, args):
        self.time_pull = args.get("Time pull")
        self.time_push = args.get("Time push")
        self.delay = 0
        self.delay_anim_init = 0
        self.pos_init = True 
        self.play_anim_init = False
        self.play_anim_back = False
        self.base_movel = self.object.childrenRecursive[0]

    def update(self):

        if self.object["start_logic"]:
            if self.pos_init:
                self.delay += 1
            else:
                self.delay_anim_init += 1
            
            if self.delay > self.time_push and self.pos_init:
                self.play_anim_back = False

                if not self.play_anim_init:
                    self.play_anim = True
                    animate(self.base_movel, "Base_Movel", 0, 20)
                self.delay = 0
                self.pos_init = False
            

            if self.delay_anim_init > self.time_pull and not self.pos_init:
                self.play_anim_init = False

                if not self.play_anim_back:
                    self.play_anim_back = True
                    animate(self.base_movel, "Base_Movel", 20, 0)
                self.delay_anim_init = 0
                self.pos_init = True
            
            # print(f'Dealy => {self.delay}')
            # print(f'Delay Back =>  {self.delay_anim_init}')

