import pygame
import pygame_gui
from simulation import *

class UI:
    def __init__(self, screenIn):
        self._screen = screenIn
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
        self._controlPanel = ControlPanel(self._manager, controlPanelRect, controlAdvancedPanelRect)     # bottom panel
        self._selectionPanel = SelectionPanel(self._manager, selectionPanelRect, selectionAdvancedPanelRect)   # right panel
        self._panelList = [self._controlPanel, self._selectionPanel]


    def handleEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:  # TODO: increase this to include other events other than just button presses
            for panelObject in self._panelList:  # loops through each panel and checks if the event is relevant to the panel
                if event.ui_element.panel == panelObject.name:
                    panelObject.handleEvents(event)
                    continue    
        self._manager.process_events(event)

    def update(self, dt):
        self._manager.update(dt)

    def drawUI(self):
        self._manager.draw_ui(self._screen)



class Panel:
    elementList = []
    name = "base"

    def __init__(self, managerIn, rectIn, advancedRectIn, advancedModeIn=False):
        self._manager = managerIn
        self._rect = rectIn
        self._advancedRect = advancedRectIn
        self._advancedMode = advancedModeIn

        self.__makePanel()
        self.__populatePanel()

    # make the GUI panel using rect (normal or advanced depending on self._advancedMode)
    def __makePanel(self):
        if self._advancedMode:
            self._x, self._y, self._w, self._h = self._advancedRect
            self._panel = pygame_gui.elements.UIPanel(self._advancedRect, manager=self._manager)
        else:
            self._x, self._y, self._w, self._h = self._rect
            self._panel = pygame_gui.elements.UIPanel(self._rect, manager=self._manager)

    # should always be overridden by subclass methods
    def __populatePanel(self):
        print(f"error: base class populatePanel method called for panel at {self._rect.x}, {self._rect.y}")

    # defining constructing a button
    def __makeButton(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):    # TODO: GUI not styling the button with the objectID inputted vvv
        # make the button
        newButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(*positionTupleIn), text=textIn, manager=self._manager, container=self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newButton.id, newButton.panel = IDIn, self._name
        
        # add it to this object's elementList
        self._elementList.append(newButton)
    

    # defining constructing a button using relative inputs
    def __makeButtonRelative(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
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
    name = "control"
    def __init__(self, managerIn, rectIn, advancedRectIn, advancedModeIn=False):
        super().__init__(managerIn, rectIn, advancedRectIn, advancedModeIn)

    def __populatePanel(self):
        if self._advancedMode:
            pass
        else:
            # self._makeButton((20, 10, 100, 40), "Test", "testButton")
            self.__makeButtonRelative((0.05, 0.5, 100, 40), "Slower", "testButton")
            self.__makeButtonRelative((0.15, 0.5, 100, 40), "", "pauseButton", "image", "play")
            self.__makeButtonRelative((0.25, 0.5, 100, 40), "Faster", "testButton")


    def handleEvents(self, event):
        if event.ui_element.id == "testButton":
            print("Control button test works!")
        elif event.ui_element.id == "pauseButton":
            print("Pause button works!")
            Simulation.pause()


# SELECTION PANEL
class SelectionPanel(Panel):
    name = "selection"
    def __init__(self, managerIn, rectIn, advancedRectIn, advancedModeIn=False):
        super().__init__(managerIn, rectIn, advancedRectIn, advancedModeIn)

    def __populatePanel(self):
        if self._advancedMode:
            pass
        else:
            self.__makeButton((20, 10, 100, 40), "Test", "testButton")

    def handleEvents(self, event):
        if event.ui_element.id == "testButton":
            print("Selection button test works!")
            Simulation.pause()

# # assign any extra classes or tags to the GUI tags for custom theming
# if GUIClassIn:
#     if type(GUIClassIn) == str:
#         newButton.class_ids.append(f"@{GUIClassIn}")
#     elif type(GUIClassIn) == list:
#         for currentClass in GUIClassIn:
#             newButton.class_ids.append(f"@{currentClass}")
# if GUITagIn:
#     if type(GUITagIn) == str:
#         newButton.object_ids.append(f"#{GUITagIn}")
#     elif type(GUITagIn) == list:
#         for tag in GUITagIn:
#             newButton.object_ids.append(f"#{tag}")
# 
# 
# newButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(20, 10, 100, 40), text="", manager=self._manager, container=self._panel, object_id="#play")


# var1.kill() to remove
# panel1.hide() to hide panel
# var1 = pygame_GUI.elementspygame_gui.elements.<UIButton>() to create
# RECT: (XYWH)
# XY USES PYGAME: TOP LEFT FOR 0