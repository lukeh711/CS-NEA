import pygame_gui
from UIElements import *

class UI:
    elementUpdateSpeed = 1.0    # number of element updates per frame (0.5 means UI elements that change each frame update at half of the framerate of the screen) NOTE: values above 1.0 will be compressed down to 1.0 when rendered by pygame so should be avoided
    _elementUpdateOperations = 0    # the rolling number of .update operations for each panel to do each frame
    def __init__(self, screenIn, simulationIn):
        self._screen = screenIn
        self._simulation = simulationIn
        # initialise the GUI library
        self._manager = pygame_gui.UIManager((screenIn.get_width(), screenIn.get_height()), theme_path="UITheme.json")


    def createUI(self):
        # make panel objects
        self._controlPanel = ControlPanel(self._manager, self._screen, self, self._simulation)     # bottom panel
        self._selectionPanel = SelectionPanel(self._manager, self._screen, self, self._simulation, hidden=True)   # right panel
        self._panelList = [self._controlPanel, self._selectionPanel]


    def handleEvents(self, event):
        self._manager.process_events(event)
        if hasattr(event, "ui_element"):    # checks if the event is UI related
            for panelObject in self._panelList:  # loops through each panel and checks if the event is relevant to the panel
                if hasattr(event.ui_element, "panel"):
                    if event.ui_element.panel == panelObject._name:
                        panelObject.handleEvents(event)
                        break

    def mouseOnUI(self, mousePosition):
        for panel in self._panelList:
            if panel.mouseOnPanel(mousePosition):
                return True
        else:
            return False

    def changeSelected(self, IDIn):
        self._selectionPanel.show()
        self._selectionPanel.changeSelected(IDIn)

    def disselect(self):
        self._selectionPanel.hide()
        self._selectionPanel.changeSelected(None)


    def update(self, dt):
        self._elementUpdateOperations += self.elementUpdateSpeed
        self._manager.update(dt)
        while self._elementUpdateOperations >= 1:
            for panel in self._panelList:
                panel.update()
            self._elementUpdateOperations -= 1
        
            

    def drawUI(self):
        self._manager.draw_ui(self._screen)

    @property
    def controlPanel(self):
        return self._controlPanel