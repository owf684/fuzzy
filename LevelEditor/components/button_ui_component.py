import sys
import pygame
sys.path.append("./Objects/components")
import sprite_component
from vector import Vector

class ButtonUIComponent:

    def __init__(self):
        # get display info
        self.display_info = pygame.display.Info()
        self.screen_width = int(self.display_info.current_w*.8)
        self.screen_height = int(self.display_info.current_h*.8)

        self.sprite = sprite_component.SpriteComponent()
        self.button_state = ButtonState(0,1)
        self.button_signal = ButtonSignal()
        self.toggled = False

    def set_animation_state(self,d_inputs):

        mouse_position = pygame.mouse.get_pos()
        # update animation if mouse hovers over button
        if self.sprite.rect.collidepoint(mouse_position):
            self.sprite.animation_state = self.button_state.state_1
        else:
            self.sprite.animation_state = self.button_state.state_2

        if self.sprite.rect.collidepoint(mouse_position):
             if d_inputs['left-click'] and not d_inputs['left_click_latch']:
                d_inputs['left_click_latch'] = True
                self.toggled = True                    
        if not d_inputs['left-click'] and d_inputs['left_click_latch']:
            d_inputs['left_click_latch'] = False

    def draw_button(self,screen):
        if len(self.sprite.sprite_sheet)>0:
                if self.sprite.sprite_sheet[self.sprite.animation_state] is not None:
                    screen.blit(self.sprite.sprite_sheet[self.sprite.animation_state],(self.sprite.position.x,self.sprite.position.y))

    def update(self,**kwargs):
        d_inputs = kwargs['InputDict']
        key = kwargs['Key']        
        self.set_animation_state(d_inputs)
        match key:
            case 'play':
                if self.toggled:
                    if (self.button_state.state_1 == 0): self.button_state = ButtonState(2,3)
                    elif (self.button_state.state_1 == 2): self.button_state = ButtonState(0,1)
                    self.toggled = False
                    self.button_signal.send(**kwargs)
            case 'add':
                if self.toggled:
                    self.toggled = False
                    self.button_signal.send(**kwargs)   
            case 'back':
                if self.toggled:
                    self.toggled = False 
                    self.button_signal.send(**kwargs)
            case "add-scene":
                if self.toggled:
                    self.toggled = False
                    self.button_signal.send(**kwargs)
            case 'save-scene':
                if self.toggled:
                    self.toggled = False
                    self.button_signal.send(**kwargs)
            case _:
                None
            
class ButtonState:
    
    def __init__(self,state_1,state_2):
        self.state_1 = state_1
        self.state_2 = state_2 


class ButtonSignal:

    def send(self,**kwargs):
        key = kwargs['Key']
        level_editor = kwargs['ALevelEditor']
       
        match key:
            case 'play':
                level_editor.edit = not level_editor.edit

            case 'back':
                level_editor.attribute_ui.restore_attribute_components()
            
            case 'add':
                print("add object")
            
            case 'add-scene':
                print("add scene")

            case 'save-scene':
                level_editor.c_scene.b_save_scene = True
            case _:
                None

       

