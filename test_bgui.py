import bgui
import bgui.bge_utils
import bge


class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)

        # Add widgets here
        # Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

        # A themed frame
        self.win = bgui.Frame(self, size=[0.6, 0.8],
                              options=bgui.BGUI_DEFAULT | bgui.BGUI_CENTERED)

        # A Label widget
        self.lbl = bgui.Label(self.win, text='I sure wish someone would push that button...',
                              pt_size=25, pos=[0, 0.7], options=bgui.BGUI_CENTERX)

        # A FrameButton widget
        self.btn = bgui.FrameButton(self.win, text='Play Animation!', size=[0.3, 0.1], pos=[0, 0.4],
                                    options=bgui.BGUI_CENTERX)

        # Add funtion callback for button
        self.btn.on_click = self.button_click

    def button_click(self, widget):
        print('clicou')
        # self.btn.visible = False


def main(cont):
    own = cont.owner
    mouse = bge.logic.mouse

    if 'sys' not in own:
        # Create our system and show the mouse
        own['sys'] = bgui.bge_utils.System('../../themes/default')
        own['sys'].load_layout(SimpleLayout, None)
        mouse.visible = True
    else:
        own['sys'].run()
