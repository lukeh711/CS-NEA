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
        # make panel objects
        self._controlPanel = ControlPanel(self._manager, self._screen, self, self._simulation)     # bottom panel
        self._selectionPanel = SelectionPanel(self._manager, self._screen, self, self._simulation, hidden=True)   # right panel
        self._panelList = [self._controlPanel, self._selectionPanel]


    def handleEvents(self, event):
        self._manager.process_events(event)
        if hasattr(event, "ui_element"):    # checks if the event is UI related
            for panelObject in self._panelList:  # loops through each panel and checks if the event is relevant to the panel
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

    def createPopup(self, widthIn, heightIn):
        return ConfirmDeletePopup(self.manager, self._screen, widthIn, heightIn)

    def update(self, dt):
        self._manager.update(dt)

    def drawUI(self):
        self._manager.draw_ui(self._screen)

    @property
    def controlPanel(self):
        return self._controlPanel



#----GUI-ELEMENT----

class GUIElement:
    _elementList = []
    _panel = None

    def __init__(self, managerIn, screenIn):
        self._manager = managerIn
        self._screen = screenIn

        self._makePanel()
        self._populatePanel()

    def _makeGUIPanel(self, panelRect):
        self._x, self._y, self._w, self._h = panelRect
        self._panel = pygame_gui.elements.UIPanel(panelRect, manager=self._manager)

    #TODO fix panel specific thingies for buttons and other elements

    def _relativeToAbsolute(self, positionTupleIn):
        # turning fractions into coordinates
        x, y, w, h = positionTupleIn
        x *= self._w
        y *= self._h
        if x < 0:
            x += self._w
        if y < 0:
            y += self._h
        # turning coords from referencing the corner to referencing the centre
        x -= w/2
        y -= h/2
        return (x, y, w, h)

    def _makeButton(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make the button
        newElement = pygame_gui.elements.UIButton(pygame.Rect(*positionTupleIn), textIn, self._manager, self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newElement.ID, newElement.panel = IDIn, self._name
        # add it to this object's elementList
        self._elementList.append(newElement)

    def _makeButtonRelative(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeButton(positionTupleOut, textIn, IDIn, GUIClassIn, GUITagIn)

    def _makeCheckBox(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make the checkbox
        newElement = pygame_gui.elements.UICheckBox(pygame.Rect(*positionTupleIn), textIn, self._manager, self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newElement.ID, newElement.panel = IDIn, self._name
        # add it to this object's elementList
        self._elementList.append(newElement)

    def _makeCheckBoxRelative(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeCheckBox(positionTupleOut, textIn, IDIn, GUIClassIn, GUITagIn)

    def _makeTextInput(self, positionTupleIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make the text input
        newElement = pygame_gui.elements.UITextEntryLine(pygame.Rect(*positionTupleIn), self._manager, self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newElement.ID, newElement.panel = IDIn, self._name
        self._elementList.append(newElement)

    def _makeTextInputRelative(self, positionTupleIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeTextInput(positionTupleOut, IDIn, GUIClassIn, GUITagIn)

    def hide(self):
        self._panel.hide()

    def show(self):
        self._panel.show()

    @property
    def h(self):
        return self._h


#----PANEL----

class Panel(GUIElement):
    _name = "basePanel"
    _popupList = []

    def __init__(self, managerIn, screenIn, UIIn, simulationIn, advancedModeIn=False, hidden=False):
        self._advancedMode = advancedModeIn
        self._UI = UIIn
        super().__init__(managerIn, screenIn)
        self._simulation = simulationIn

        if hidden:
            self.hide()

    def _makeCurrentPanel(self):
        if self._advancedMode:
            currentRect = self._advancedRect
        else:
            currentRect = self._rect
        self._makeGUIPanel(currentRect)

    def _createPopup(self, typeIn):
        if typeIn == "delete":
            currentPopup = self._UI.makePopup(200, 200)
        else:
            raise ValueError(f"Failed to create popup of type {typeIn}")

    def mouseOnPanel(self, mousePosition):
        # TODO: add popup box confirmation
        if self._advancedMode:
            return self._advancedRect.collidepoint(*mousePosition)
        else:
            return self._rect.collidepoint(*mousePosition)


# CONTROL PANEL
class ControlPanel(Panel):
    _name = "control"
    def __init__(self, managerIn, screenIn, UIIn, simulationIn, advancedModeIn=False, hidden=False):
        super().__init__(managerIn, screenIn, UIIn, simulationIn, advancedModeIn, hidden)

    def _makePanel(self):
        # define rect objects for this panel
        self._rect = pygame.Rect(0, 0, self._screen.get_width(), 150)
        self._rect.bottomleft = (0, self._screen.get_height())
        self._advancedRect = self._rect.copy()  # advanced panel is the same size as normal for now
        self._makeCurrentPanel()

    def _populatePanel(self):
        if self._advancedMode:
            pass
        else:
            # self._makeButton((20, 10, 100, 40), "Test", "testButton")
            #                                             text, ID, GUI class, GUI ID
            self._makeButtonRelative((0.1, 0.5, 100, 40), "", "backwardsButton", "image", "backwards")
            self._makeButtonRelative((0.2, 0.5, 100, 40), "", "pauseButton", "image", "play")
            self._makeButtonRelative((0.3, 0.5, 100, 40), "", "forwardsButton", "image", "forwards")
            self._makeButtonRelative((0.8, 0.5, 100, 40), "Add Object", "addObject", "green")
            self._makeButtonRelative((0.9, 0.5, 100, 40), "New Graph", "newGraph", "green")


    def handleEvents(self, event):
        ID = event.ui_element.ID
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if ID == "testButton":
                print("Control button test works!")
            elif ID == "pauseButton":
                print("Pause button works!")
                self._simulation.pause()
            elif ID == "forwardsButton":
                print("forwards button works!")
                self._simulation.speedUp()
            elif ID == "backwardsButton":
                print("backwards button works!")
                self._simulation.speedDown()


# SELECTION PANEL
class SelectionPanel(Panel):
    _name = "selection"
    def __init__(self, managerIn, screenIn, UIIn, simulationIn, advancedModeIn=False, hidden=False):
        super().__init__(managerIn, screenIn, UIIn, simulationIn, advancedModeIn, hidden)

    def _makePanel(self):
        # define rect objects for this panel
        self._rect = pygame.Rect(0, 0, self._screen.get_width()//3, self._screen.get_height()-self._UI.controlPanel.h)
        self._rect.topright = (self._screen.get_width(), 0)
        self._advancedRect = self._rect.copy()  # advanced panel is the same size as normal for now
        self._makeCurrentPanel()

    def _populatePanel(self):
        if self._advancedMode:
            pass
        else:
            # self._makeButton((20, 10, 100, 40), "Test", "testButton")
            #                                       rect, (text), ID, (GUI class), (GUI ID)
            self._makeButtonRelative((0.25, 0.9, 120, 40), "Delete object", "deleteObject", "red", "")
            self._makeCheckBoxRelative((0.1, 0.1, 40, 40), "Show", "idekreplacethis", "", "")
            self._makeTextInputRelative((0.2, 0.3, 100, 40), "testTextInput")
            

    def handleEvents(self, event):
        ID = event.ui_element.ID
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if ID == "testButton":
                print("Selection button test works!")
            if ID == "deleteObject":
                self.deleteSelection()

    def changeSelected(self, IDIn):
        if IDIn is not None:
            print(f"selected is now {IDIn}")
            self.selectedObject = self._simulation.findObject(IDIn)

    def deleteSelection(self):
        # TODO: confirmation dialogue checking you meant to click on that
        if self.selectedObject is not None:
            self._simulation.removeObject(self.selectedObject)
        self.hide()


#----POPUP----

class Popup(GUIElement):
    def __init__(self, managerIn, screenIn, widthIn, heightIn):
        self._w = widthIn
        self._h = heightIn
        super().__init__(managerIn, screenIn)

    def _makePanel(self):
        self._rect = pygame.Rect(0, 0, self._w, self._h)
        self._rect.center = (self._screen.get_width()//2, self._screen.get_height()//2)
        self._makeGUIPanel(self._rect)


class ConfirmDeletePopup(Popup):
    def __init__(self, managerIn, screenIn, widthIn, heightIn, textIn):
        super().__init__(managerIn, screenIn, widthIn, heightIn)
        self.text = textIn
    
    def _populatePanel(self):
        self._makeButtonRelative((0.5, 0.8, 40, 130), "I'm sure", "confirm", GUIClassIn="red")
        


# in handleEvents:
# if "#test" in event.ui_element.object_ids:
#     print("testing the test!")

# var1.kill() to remove
# panel1.hide() to hide panel
# var1 = pygame_GUI.elementspygame_gui.elements.<UIButton>() to create
# RECT: (XYWH)
# XY USES PYGAME: TOP LEFT FOR 0