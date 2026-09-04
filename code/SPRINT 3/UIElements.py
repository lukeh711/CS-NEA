import pygame
import pygame_gui
from simulation import *


#------GUI-ELEMENT------

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


    # MAKING ELEMENTS
    def _relativeToAbsolute(self, positionTupleIn):
        x, y, w, h = positionTupleIn
        # if the inputted number is a float, treat it as a fraction
        # if the inputted number is an integer, treat it as an absolute value
        if type(x) == float:
            x *= self._w
        if type(y) == float:
            y *= self._h
        if type(w) == float:
            w *= self._w
        if type(h) == float:
            h *= self._h
        # making negative numbers wrap around to the other side
        if x < 0:
            x += self._w
        if y < 0:
            y += self._h
        if w < 0:
            w += self._w
        if h < 0:
            h += self._h
        # turning coords from referencing the corner to referencing the centre
        x -= w/2
        y -= h/2
        return (x, y, w, h)

    def _makeButton(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make the button
        newElement = pygame_gui.elements.UIButton(pygame.Rect(*positionTupleIn), textIn, self._manager, self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newElement.ID = IDIn
        # add it to this object's elementList
        self._elementList.append(newElement)
        return newElement

    def _makeButtonRelative(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeButton(positionTupleOut, textIn, IDIn, GUIClassIn, GUITagIn)

    def _makeCheckBox(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make the checkbox
        newElement = pygame_gui.elements.UICheckBox(pygame.Rect(*positionTupleIn), textIn, self._manager, self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newElement.ID = IDIn
        # add it to this object's elementList
        self._elementList.append(newElement)
        return newElement

    def _makeCheckBoxRelative(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeCheckBox(positionTupleOut, textIn, IDIn, GUIClassIn, GUITagIn)

    def _makeTextInput(self, positionTupleIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make the text input
        newElement = pygame_gui.elements.UITextEntryLine(pygame.Rect(*positionTupleIn), self._manager, self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        newElement.ID = IDIn
        newElement.sigFigs = 3
        self._elementList.append(newElement)
        return newElement

    def _makeTextInputRelative(self, positionTupleIn, IDIn, GUIClassIn=None, GUITagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeTextInput(positionTupleOut, IDIn, GUIClassIn, GUITagIn)

    def _makeAttributeBox(self, positionTupleIn, positionTypeIn, textIn, IDIn, GUITextBoxClassIn=None, GUITextBoxTagIn=None, GUITextInputClassIn=None, GUITextInputTagIn=None):
        if positionTypeIn == "vertical":
            textBoxPositionTuple = self.multiplyTuples(positionTupleIn, (1,1,1,0.7))
            textInputPositionTuple = self.addTuples(self.multiplyTuples(positionTupleIn, (1,1,1,0.3)), (0,positionTupleIn[3]*0.7,0,0))
        elif positionTypeIn == "horizontal":
            textBoxPositionTuple = self.multiplyTuples(positionTupleIn, (1,1,0.7,1))
            textInputPositionTuple = self.addTuples(self.multiplyTuples(positionTupleIn, (1,1,0.3,1)), (positionTupleIn[2]*0.7,0,0,0))
        else:
            raise ValueError(f"failed to create attributeBox of type {positionTypeIn}.")
        # make the text box and text input
        newElement1 = self._makeTextBox(textBoxPositionTuple, textIn, GUITextBoxClassIn, GUITextBoxTagIn)
        newElement2 = self._makeTextInput(textInputPositionTuple, IDIn, GUITextInputClassIn, GUITextInputTagIn)

        # assign it a custom ID and panel attribute to keep track of it
        newElement1.ID = IDIn
        newElement2.ID = IDIn
        newElement2.sigFigs = 3
        self._elementList.append(newElement1)
        self._elementList.append(newElement2)
        return (newElement1, newElement2)

    def multiplyTuples(self, a, b):
        return tuple(a*b for a, b in zip(a, b))

    def addTuples(self, a, b):
            return tuple(a+b for a, b in zip(a, b))
    
    def _makeAttributeBoxRelative(self, positionTupleIn, positionTypeIn, textIn, IDIn, GUITextBoxClassIn=None, GUITextBoxTagIn=None, GUITextInputClassIn=None, GUITextInputTagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeAttributeBox(positionTupleOut, positionTypeIn, textIn, IDIn, GUITextBoxClassIn=None, GUITextBoxTagIn=None, GUITextInputClassIn=None, GUITextInputTagIn=None)

    def _makeTextBox(self, positionTupleIn, textIn, IDIn=None, GUIClassIn=None, GUITagIn=None):
        # make the text box
        newElement = pygame_gui.elements.UITextBox(textIn, pygame.Rect(*positionTupleIn), self._manager, container=self._panel, object_id=pygame_gui.core.ObjectID(object_id=f"#{GUITagIn}" if GUITagIn else None, class_id=f"@{GUIClassIn}" if GUIClassIn else None))
        # assign it a custom ID and panel attribute to keep track of it
        if IDIn is not None:
            newElement.ID = IDIn
        self._elementList.append(newElement)
        return newElement

    def _makeTextBoxRelative(self, positionTupleIn, textIn, IDIn=None, GUIClassIn=None, GUITagIn=None):
        # make coords relative
        positionTupleOut = self._relativeToAbsolute(positionTupleIn)
        self._makeTextBox(positionTupleOut, textIn, IDIn, GUIClassIn, GUITagIn)

    def hide(self):
        self._panel.hide()

    def show(self):
        self._panel.show()

    @property
    def h(self):
        return self._h




#------PANEL------

class Panel(GUIElement):
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

    # MAKING ELEMENTS
    def _makeButton(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeButton(positionTupleIn, textIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._name
        return newElement

    def _makeCheckBox(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeCheckBox(positionTupleIn, textIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._name
        return newElement

    def _makeTextInput(self, positionTupleIn, IDIn, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeTextInput(positionTupleIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._name
        return newElement

    def _makeAttributeBox(self, positionTupleIn, positionTypeIn, textIn, IDIn, GUITextBoxClassIn=None, GUITextBoxTagIn=None, GUITextInputClassIn=None, GUITextInputTagIn=None):
        newElement = super()._makeAttributeBox(positionTupleIn, positionTypeIn, textIn, IDIn, GUITextBoxClassIn=None, GUITextBoxTagIn=None, GUITextInputClassIn=None, GUITextInputTagIn=None)
        for element in newElement:
            element.panel = self._name
        return newElement

    def _makeTextBox(self, positionTupleIn, textIn, IDIn=None, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeTextBox(positionTupleIn, textIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._name
        return newElement

    def _makePopup(self, typeIn):
        if typeIn.lower() == "delete":
            currentPopup = ConfirmDeletePopup(self._manager, self._screen, 300, 250, self._name)
            self._popupList.append(currentPopup)
        elif typeIn.lower() == "makeobject":
            print("Popup made!")
            currentPopup = MakeObject(self._manager, self._screen, 500, 700, self._name)
            self._popupList.append(currentPopup)
        else:
            raise ValueError(f"Failed to create popup of type {typeIn}")


    def removePopup(self, targetPopup):
        targetPopup.delete()
        self._popupList.remove(targetPopup)

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
        # popup events
        if hasattr(event.ui_element, "popup"):
            # finds popup object, then breaks to leave currentPopup referring to the correct object
            for currentPopup in self._popupList:
                if currentPopup._name == event.ui_element.popup:
                    break
            
            # MAKE OBJECT POPUP
            if event.ui_element.popup == "makeObject":
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if ID == "confirm":
                        newObject = currentPopup.newObject
                        if newObject:
                            self._simulation.addObject(newObject)
                        self.removePopup(currentPopup)
                    elif ID == "cancel":
                        self.removePopup(currentPopup)

        # other events
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if ID == "testButton":
                print("Control button test works!")
            elif ID == "pauseButton":
                self._simulation.pauseToggle()
            elif ID == "forwardsButton":
                self._simulation.speedUp()
            elif ID == "backwardsButton":
                self._simulation.speedDown()
            elif ID == "addObject":
                self._addObject()

    def _addObject(self):
        self._makePopup("makeObject")

    def update(self):
        pass


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
            self._makeTextInputRelative((0.2, 0.4, 100, 40), "horizontalVelocity")
            self._makeTextInputRelative((0.2, 0.5, 100, 40), "verticalVelocity")
            self._makeAttributeBoxRelative((0.5, 0.3, 110, 100), "vertical", "Horizontal velocity:", "horizontalVelocity")
            self._makeAttributeBoxRelative((0.5, 0.5, 110, 100), "vertical", "Vertical velocity:", "verticalVelocity")
            self._makeAttributeBoxRelative((0.7, 0.7, 220, 50), "horizontal", "Vertical velocity:", "verticalVelocity")

    def _makeTextInput(self, positionTupleIn, IDIn, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeTextInput(positionTupleIn, IDIn, GUIClassIn, GUITagIn)
        newElement.unfocusPause = False
        return newElement

    def handleEvents(self, event):
        ID = event.ui_element.ID
        # popup events
        if hasattr(event.ui_element, "popup"):
            # finds popup object, then breaks to leave currentPopup referring to the correct object
            for currentPopup in self._popupList:
                if currentPopup._name == event.ui_element.popup:
                    break

            # DELETE POPUP
            if event.ui_element.popup == "delete":
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if ID == "confirm":
                        self.removePopup(currentPopup)
                        self.deleteSelection()
                    elif ID == "cancel":
                        self.removePopup(currentPopup)

        #other events
        else:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if ID == "testButton":
                    print("Selection button test works!")
                if ID == "deleteObject":
                    self.confirmDeleteSelection()
            # elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED
            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                event.ui_element.unfocus()
                event.ui_element.unfocusPause = False
                self._simulation.play()
                print("Entered text:", event.text)
                print("Altering object attribute now")
                ID = event.ui_element.ID
                if ID == "verticalVelocity":
                    self.selectedObject.velocity[0] = event.text
                elif ID == "horizontalVelocity":
                    self.selectedObject.velocity[1] = event.text
    

    def update(self):
        # run each frame and update any elements that update regularly
        for element in self._elementList:
            if element.visible:
                if isinstance(element, pygame_gui.elements.UITextEntryLine):
                    if element.is_focused and element.visible:
                        self._simulation.pause()
                        element.unfocusPause = True
                    else:
                        if element.unfocusPause:
                            self._simulation.play()
                            element.unfocusPause = False
                        self.updateTextInput(element)

    def updateTextInput(self, elementIn):
        if elementIn.ID == "horizontalVelocity":
            elementIn.set_text(self.sigFigs(elementIn.sigFigs, self.selectedObject.velocity[0]))
        elif elementIn.ID == "verticalVelocity":
            elementIn.set_text(self.sigFigs(elementIn.sigFigs, self.selectedObject.velocity[1]))

    def sigFigs(self, sigFigs, value):
        return '%s' % float(f'%.{sigFigs}g' % value)


    def changeSelected(self, IDIn):
        if IDIn is not None:
            print(f"selected is now {IDIn}")
            self.selectedObject = self._simulation.findObject(IDIn)

    def confirmDeleteSelection(self):
        alreadyExists = False
        # ensuring no popup already exists
        for popup in self._popupList:
            if popup.name == "delete":
                alreadyExists = True
        if not alreadyExists:
            self._makePopup("delete")

    def deleteSelection(self):
        if self.selectedObject is not None:
            self._simulation.removeObject(self.selectedObject)
        self.hide()




#------POPUP------

# self._panel - name of the panel which made the popup
# self.popup - the type of popup it is
class Popup(GUIElement):
    def __init__(self, managerIn, screenIn, widthIn, heightIn, panelNameIn):
        self._w = widthIn
        self._h = heightIn
        self._panelName = panelNameIn
        super().__init__(managerIn, screenIn)

    def _makePanel(self):
        self._rect = pygame.Rect(0, 0, self._w, self._h)
        self._rect.center = (self._screen.get_width()//2, self._screen.get_height()//2)
        self._makeGUIPanel(self._rect)

    def _makeButton(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeButton(positionTupleIn, textIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._panelName
        newElement.popup = self._name

    def _makeCheckBox(self, positionTupleIn, textIn, IDIn, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeCheckBox(positionTupleIn, textIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._panelName
        newElement.popup = self._name

    def _makeTextInput(self, positionTupleIn, IDIn, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeTextInput(positionTupleIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._panelName
        newElement.popup = self._name

    def _makeTextBox(self, positionTupleIn, textIn, IDIn=None, GUIClassIn=None, GUITagIn=None):
        newElement = super()._makeTextBox(positionTupleIn, textIn, IDIn, GUIClassIn, GUITagIn)
        newElement.panel = self._panelName
        newElement.popup = self._name

    def delete(self):
        self._panel.kill()



class ConfirmDeletePopup(Popup):
    _name = "delete"

    def __init__(self, managerIn, screenIn, widthIn, heightIn, panelNameIn):
        super().__init__(managerIn, screenIn, widthIn, heightIn, panelNameIn)
    
    def _populatePanel(self):
        self._makeTextBoxRelative((0.5, 0.3, 0.8, 0.5), "Are you sure you want to delete this object?")
        self._makeButtonRelative((0.25, 0.8, 120, 40), "I'm sure", "confirm", GUIClassIn="red")
        self._makeButtonRelative((0.75, 0.8, 120, 40), "Cancel", "cancel")

    @property
    def name(self):
        return self._name


class MakeObject(Popup):
    _name = "makeObject"
    newObject = None

    def __init__(self, managerIn, screenIn, widthIn, heightIn, panelNameIn):
        super().__init__(managerIn, screenIn, widthIn, heightIn, panelNameIn)
    
    def _populatePanel(self):
        self._makeTextBoxRelative((0.5, 0.3, 0.8, 0.5), "Delete me!")
        self._makeButtonRelative((0.25, 0.8, 120, 40), "I'm sure", "confirm", GUIClassIn="red")
        self._makeButtonRelative((0.75, 0.8, 120, 40), "Cancel", "cancel")

    @property
    def name(self):
        return self._name

# in handleEvents:
# if "#test" in event.ui_element.object_ids:
#     print("testing the test!")

# var1.kill() to remove
# panel1.hide() to hide panel
# var1 = pygame_GUI.elementspygame_gui.elements.<UIButton>() to create
# RECT: (XYWH)
# XY USES PYGAME: TOP LEFT FOR 0