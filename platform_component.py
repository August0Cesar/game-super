import bge
from collections import OrderedDict

class PlatformComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("Time Subir", 50) 
    ])

    def start(self, args):
        self.level_time = args.get("Time Subir")
        self.time_up = 0


    def update(self):

        self.time_up +=1
        if self.time_up == self.level_time:
            self.time_up = 0
            if self.object["Subir"]:
                self.object["Subir"] = False
            else:
                self.object["Subir"] = True
