import pygame
import pygame_gui
from simulation import *

class UI:
    def __init__(self, screenIn, simulationIn):
        self._screen = screenIn
        self._simulation = simulationIn
        # initialise the GUI library
        self._manager = pygame_gui.UIManager((screenIn.get_width(), screenIn.get_height()), theme_path="UITheme.json")

    def createUI(self):
        # make rects for positions of each panel and their advanced versions
        controlPanelRect = pygame.Rect(0, 0, self._screen.get_width(), 150)
        controlPanelRect.bottomleft = (0, self._screen.get_height())
        controlAdvancedPanelRect = controlPanelRect.copy()  # advanced panel is the same size as normal for now

        selectionPanelRect = pygame.Rect(0, 0, 300, self._screen.get_height()-controlPanelRect.height)
        selectionPanelRect.topright = (self._screen.get_width(), 0)
        selectionAdvancedPanelRect = selectionPanelRect.copy()  # advanced panel is the same size as normal for now

        # make panel objects
        self._controlPanel = ControlPanel(self._manager, self._simulation, controlPanelRect, controlAdvancedPanelRect)     # bottom panel
        self._selectionPanel = SelectionPanel(self._manager, self._simulation, selectionPanelRect, selectionAdvancedPanelRect)   # right panel
        self._panelList = [self._controlPanel, self._selectionPanel]


    def handleEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:  # TODO: increase this to include other events other than just button presses
            for panelObject in self._panelList:  # loops through each panel and checks if the event is relevant to the panel
                if event.ui_element.panel == panelObject._name:
                    panelObject.handleEvents(event)
                    continue    
        self._manager.process_events(event)

    def update(self, dt):
        self._manager.update(dt)

    def drawUI(self):
        self._manager.draw_ui(self._screen)



class Panel:
    _elementList = []
    _name = "base"

    def __init__(self, managerIn, simulationIn, rectIn, advancedRectIn, advancedModeIn=False):
        self._manager = managerIn
        self._simulation = simulationIn
        self._rect = rectIn
        self._advancedRect = advancedRectIn
        self._advancedMode = advancedModeIn

        self._makePanel()
        self._populatePanel()

    # make the GUI panel using rect (normal or advanced depending on self._advancedMode)
    def _makePanel(self):
        if self._advancedMode:
            self._x, self._y, self._w, self._h = self._advancedRect
            self._panel = pygame_gui.elements.UIPanel(self._advancedRect, manager=self._manager)
        else:
            self._x, self._y, self._w, self._h = self._rect
            self._panel = pygame_gui.elements.UIPanel(self._rect, manager=self._manager)

    # should always be overridden by subclass methods
    def _populatePanel(self):
        print(f"error: base class populatePanel method called for panel at {self._rect.x}, {self._rect.y}")

    # defining constructing a button
    def _makeButton(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):    # TODO: GUI not styling the button with the objectID inputted vvv
        # make the button
        newButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(*positionTupleIn), text=textIn, manager=self._manager, container=self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newButton.id, newButton.panel = IDIn, self._name
        
        # add it to this object's elementList
        self._elementList.append(newButton)
    

    # defining constructing a button using relative inputs
    def _makeButtonRelative(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # turning fractions into coordinates
        x, y, w, h = positionTupleIn
        x *= self._w
        y *= self._h
        if x < 0:
            x += self._w
        if y < 0:
            y += self._h
        # turning coords in referencing the centre to referencing the corner
        x -= w/2
        y -= h/2
        self._makeButton((x, y, w, h), textIn, IDIn, GUIClassIn, GUITagIn)

    def hide(self):
        self._panel.hide()

    def show(self):
        self._panel.show()

# CONTROL PANEL
class ControlPanel(Panel):
    _name = "control"
    def __init__(self, managerIn, simulationIn, rectIn, advancedRectIn, advancedModeIn=False):
        super().__init__(managerIn, simulationIn, rectIn, advancedRectIn, advancedModeIn)

    def _populatePanel(self):
        if self._advancedMode:
            pass
        else:
            # self._makeButton((20, 10, 100, 40), "Test", "testButton", GUITagIn="test")
            self._makeButtonRelative((0.1, 0.5, 100, 40), "", "backwardsButton", "image", "backwards")
            self._makeButtonRelative((0.2, 0.5, 100, 40), "", "pauseButton", "image", "play")
            self._makeButtonRelative((0.3, 0.5, 100, 40), "", "forwardsButton", "image", "forwards")


    def handleEvents(self, event):
        if event.ui_element.id == "testButton":
            print("Control button test works!")
        elif event.ui_element.id == "pauseButton":
            print("Pause button works!")
            self._simulation.pause()
        elif event.ui_element.id == "forwardsButton":
            print("forwards button works!")
            self._simulation.speedUp()
        elif event.ui_element.id == "backwardsButton":
            print("backwards button works!")
            self._simulation.speedDown()


# SELECTION PANEL
class SelectionPanel(Panel):
    _name = "selection"
    def __init__(self, managerIn, simulationIn, rectIn, advancedRectIn, advancedModeIn=False):
        super().__init__(managerIn, simulationIn, rectIn, advancedRectIn, advancedModeIn)

    def _populatePanel(self):
        if self._advancedMode:
            pass
        else:
            self._makeButton((20, 10, 100, 40), "Test", "testButton")

    def handleEvents(self, event):
        if event.ui_element.id == "testButton":
            print("Selection button test works!")

# in handleEvents:
# if "#test" in event.ui_element.object_ids:
#     print("testing the test!")
# 
# 
# newButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(20, 10, 100, 40), text="", manager=self._manager, container=self._panel, object_id="#play")


# var1.kill() to remove
# panel1.hide() to hide panel
# var1 = pygame_GUI.elementspygame_gui.elements.<UIButton>() to create
# RECT: (XYWH)
# XY USES PYGAME: TOP LEFT FOR 0