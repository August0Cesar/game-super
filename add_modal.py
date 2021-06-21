import bgui
import bgui.bge_utils
import bge
from collections import OrderedDict


class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)
        self.count = 0
        # Add widgets here
        # Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

        # A themed frame
        self.win = bgui.Frame(self, size=[0.6, 0.8],
                              options=bgui.BGUI_DEFAULT | bgui.BGUI_CENTERED)
        # self.win.colors = [(255, 0, 0, 0) for i in range(4)]

        # A Label widget
        self.lbl = bgui.Label(self.win, text='I sure wish someone would push that button...',
                              pt_size=35, pos=[0, 0.7], options=bgui.BGUI_CENTERX)

        # A FrameButton widget
        self.btn = bgui.FrameButton(self.win, text='Click Me!', size=[0.3, 0.1], pos=[0, 0.4],
                                    options=bgui.BGUI_CENTERX)

        # Add funtion callback for button
        self.btn.on_click = self.button_click

    def button_click(self, widget):
        self.count += 1
        self.lbl.text = f'Clickou {self.count}'


class AddModalComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        # pass
        self.sys = bgui.bge_utils.System('../../themes/default')
        self.sys.load_layout(SimpleLayout, None)

    def update(self):
        self.sys.run()
