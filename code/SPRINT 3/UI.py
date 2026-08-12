import pygame
import pygame_gui

class UI:
    def __init__(self, screenIn):
        self.screen = screenIn
        # initialise the GUI library
        self.manager = pygame_gui.UIManager((screenIn.get_width(), screenIn.get_height()))

        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Say Hello', manager=self.manager)

    def handleEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.hello_button:
                print('Hello World!')
        
        self.manager.process_events(event)

    def update(self, dt):
        self.manager.update(dt)

    def drawUI(self):
        self.manager.draw_ui(self.screen)