import pygame
import pygame_gui
import simulation

class UI:
    def __init__(self, screenIn):
        self.screen = screenIn
        # initialise the GUI library
        self.manager = pygame_gui.UIManager((screenIn.get_width(), screenIn.get_height()), theme_path="UITheme.json")

    def createUI(self):
        # make rects for positions of each panel and their advanced versions
        controlPanelRect = pygame.Rect(0, 0, self.screen.get_width(), 150)
        controlPanelRect.bottomleft = (0, self.screen.get_height())
        controlAdvancedPanelRect = controlPanelRect.copy()  # advanced panel is the same size as normal for now

        selectionPanelRect = pygame.Rect(0, 0, 300, self.screen.get_height()-controlPanelRect.height)
        selectionPanelRect.topright = (self.screen.get_width(), 0)
        selectionAdvancedPanelRect = selectionPanelRect.copy()  # advanced panel is the same size as normal for now

        # make panel objects
        self.controlPanel = ControlPanel(self.manager, controlPanelRect, controlAdvancedPanelRect)     # bottom panel
        self.selectionPanel = SelectionPanel(self.manager, selectionPanelRect, selectionAdvancedPanelRect)   # right panel
        self.panelList = [self.controlPanel, self.selectionPanel]


    def handleEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:  # TODO: increase this to include other events
            for panelObject in self.panelList:  # loops through each panel and checks if the event is relevant to the panel
                if event.ui_element.panel == panelObject.name:
                    panelObject.handleEvents(event)
                    continue    
        self.manager.process_events(event)

    def update(self, dt):
        self.manager.update(dt)

    def drawUI(self):
        self.manager.draw_ui(self.screen)



class Panel:
    elementList = []
    name = "base"

    def __init__(self, managerIn, rectIn, advancedRectIn, advancedModeIn=False):
        self.manager = managerIn
        self.rect = rectIn
        self.advancedRect = advancedRectIn
        self.advancedMode = advancedModeIn

        self.makePanel()
        self.populatePanel()

    # make the GUI panel using rect (normal or advanced depending on self.advancedMode)
    def makePanel(self):
        if self.advancedMode:
            self.x, self.y, self.w, self.h = self.advancedRect
            self.panel = pygame_gui.elements.UIPanel(self.advancedRect, manager=self.manager)
        else:
            self.x, self.y, self.w, self.h = self.rect
            self.panel = pygame_gui.elements.UIPanel(self.rect, manager=self.manager)

    # should always be overridden by subclass methods
    def populatePanel(self):
        print(f"error: base class populatePanel method called for panel at {self.rect.x}, {self.rect.y}")

    # defining constructing a button
    def makeButton(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):    # TODO: GUI not styling the button with the objectID inputted vvv
        # make the button
        newButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(*positionTupleIn), text=textIn, manager=self.manager, container=self.panel, object_id=GUITagIn)
        # assign it a custom ID and panel attribute to keep track of it
        newButton.id, newButton.panel = IDIn, self.name
        
        # add it to this object's elementList
        self.elementList.append(newButton)
    

    # defining constructing a button using relative inputs
    def makeButtonRelative(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # turning fractions into coordinates
        x, y, w, h = positionTupleIn
        x *= self.w
        y *= self.h
        if x < 0:
            x += self.w
        if y < 0:
            y += self.h
        # turning coords in referencing the centre to referencing the corner
        x -= w/2
        y -= h/2
        self.makeButton((x, y, w, h), textIn, IDIn, GUIClassIn, GUITagIn)

    def hide(self):
        self.panel.hide()

    def show(self):
        self.panel.show()

# CONTROL PANEL
class ControlPanel(Panel):
    name = "control"
    def __init__(self, managerIn, rectIn, advancedRectIn, advancedModeIn=False):
        super().__init__(managerIn, rectIn, advancedRectIn, advancedModeIn)

    def populatePanel(self):
        if self.advancedMode:
            pass
        else:
            # self.makeButton((20, 10, 100, 40), "Test", "testButton")
            self.makeButtonRelative((0.05, 0.5, 100, 40), "Slower", "testButton")
            self.makeButtonRelative((0.15, 0.5, 100, 40), "", "testButton", "image", "play")
            self.makeButtonRelative((0.25, 0.5, 100, 40), "Faster", "testButton")

    def handleEvents(self, event):
        if event.ui_element.id == "testButton":
            print("Control button test works!")


# SELECTION PANEL
class SelectionPanel(Panel):
    name = "selection"
    def __init__(self, managerIn, rectIn, advancedRectIn, advancedModeIn=False):
        super().__init__(managerIn, rectIn, advancedRectIn, advancedModeIn)

    def populatePanel(self):
        if self.advancedMode:
            pass
        else:
            self.makeButton((20, 10, 100, 40), "Test", "testButton")

    def handleEvents(self, event):
        if event.ui_element.id == "testButton":
            print("Selection button test works!")


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


# var1.kill() to remove
# panel1.hide() to hide panel
# var1 = pygame_GUI.elementspygame_gui.elements.<UIButton>() to create
# RECT: (XYWH)
# XY USES PYGAME: TOP LEFT FOR 0