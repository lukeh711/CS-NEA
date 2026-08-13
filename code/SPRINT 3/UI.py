import pygame
import pygame_gui

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
        selectionAdvancedPanelRect = selectionPanelRect.copy()  # advanced panel is the same size as normal for now

        # make panel objects
        self.controlPanel = Panel(self.manager, controlPanelRect, controlAdvancedPanelRect)     # bottom panel
        self.selectionPanel = Panel(self.manager, selectionPanelRect, selectionAdvancedPanelRect)   # right panel


    def handleEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.hello_button:
                print('Hello World!')
        
        self.manager.process_events(event)

    def update(self, dt):
        self.manager.update(dt)

    def drawUI(self):
        self.manager.draw_ui(self.screen)



class Panel:
    def __init__(self, managerIn, rectIn, advancedRectIn, advancedModeIn=False):
        self.manager = managerIn
        self.rect = rectIn
        self.advancedRect = advancedRectIn
        self.advancedMode = advancedModeIn

        self.makePanel()
        self.populatePanel()

    def makePanel(self):    # make the GUI panel using rect (normal or advanced depending on self.advancedMode)
        if self.advancedMode:
            self.panel = pygame_gui.elements.UIPanel(self.advancedRect, manager=self.manager)
        else:
            self.panel = pygame_gui.elements.UIPanel(self.rect, manager=self.manager)

    def populatePanel(self):
        if self.advancedMode:
            pass
        else:
            pass

    def hide(self):
        pass

    def show(self):
        pass


# TEMP testing elements
# settingsPanel = pygame_gui.elements.UIPanel((50, 50, 150, 200), manager=self.manager)
# self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 5), (100, 50)), text='Say Hello', manager=self.manager, container=settingsPanel)

# controlPanelRect = pygame.Rect(0, 0, self.screen.get_width(), 150)    # make the pause/play/fast forward control panel rect
# controlPanelRect.bottomleft = (0, self.screen.get_height())   # move it to the bottom of the screen
# self.controlPanel = pygame_gui.elements.UIPanel(controlPanelRect, manager=self.manager) # make the GUI panel using that rect

# controlPanelHeight = 150
# selectionPanelRect = pygame.Rect(0, 0, 300, self.screen.get_height()-controlPanelHeight) # make the object selection panel rect
# selectionPanelRect.topright = (self.screen.get_width(), 0)  # move it to the bottom of the screen
# self.selectionPanel = pygame_gui.elements.UIPanel(selectionPanelRect, manager=self.manager) # make the GUI panel using that rect

# var1.kill() to remove
# var1 = pygame_GUI.elementspygame_gui.elements.<UIButton>() to create
# RECT: (XYWH)
# XY USES PYGAME: TOP LEFT FOR 0