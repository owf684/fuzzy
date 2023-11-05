import sys
import pygame
sys.path.append("./LevelEditor/components")
sys.path.append("./Objects/components")
import object_creator_component
import object_container_ui_component
import button_ui_component
import grid_ui_component
import tool_bar_ui_component
import attribute_ui_component
import object_placer_component 
import text_box_ui_component
from vector import Vector
class LevelEditor:

    def __init__(self):
        # get display info
        self.display_info = pygame.display.Info()
        self.screen_width = int(self.display_info.current_w*.8)
        self.screen_height = int(self.display_info.current_h*.8)

        # setup object creator
        self.c_object_creator = object_creator_component.ObjectCreatorComponent()
        self.c_object_creator.s_directory_path ='./GameData/jsons'
        self.c_object_creator.create_json_list()
        self.c_object_creator.create_objects_dict()
        self.c_object_creator.organize_objects()

        # setup grid component
        self.grid = grid_ui_component.GridUIComponent()

        # setup tool bar
        self.tool_bar = tool_bar_ui_component.ToolBarUIComponent()
        
        # setup editor ui
        self.object_container_ui = object_container_ui_component.ObjectContainerUIComponent()
        self.object_container_ui.init_ui(self.c_object_creator)

        # setup button ui
        self.play_pause_button = button_ui_component.ButtonUIComponent()
        self.back_button = button_ui_component.ButtonUIComponent()
        self.add_object_button = button_ui_component.ButtonUIComponent()
        self.l_button_ui_elements = {}
        self.setup_button_ui()

        # setup attributes ui
        self.attribute_ui = attribute_ui_component.AttributeUIComponent()

        # setup object place
        self.object_placer = object_placer_component.ObjectPlacerComponent()

        #setup a text boxt
        self.text_box_ui = text_box_ui_component.TextBoxUIComponent()
   
        self.attribute_ui.l_text_boxes = self.text_box_ui.l_text_boxes
        self.text_box_ui.previous_attribute_components = self.attribute_ui.l_previous_attribute_components

        self.selected_object = None
        self.edit = True

    def update(self,**kwargs):
        d_inputs=kwargs['InputDict']
        game_objects = kwargs['GameObjects']

        self.c_object_creator.category_handler(d_inputs)

        for key, button in self.l_button_ui_elements.items():
            button.update(Key=key,InputDict=d_inputs,ALevelEditor=self)

        self.attribute_ui.update_selected_object(d_inputs,game_objects)
        self.attribute_ui.update_object_attributes(d_inputs)

        self.object_container_ui.update_object_container_ui(self.c_object_creator)

        self.object_placer.update(InputDict=d_inputs,GameObjects=game_objects,ALevelEditor=self)
   
        self.text_box_ui.get_input()

    def setup_button_ui(self):
        # create sprite sheets
        self.play_pause_button.sprite.create_sprite_sheet("./Assets/UI/Buttons/play_pause.png",4,Vector(64,64))
        self.add_object_button.sprite.create_sprite_sheet("./Assets/UI/Buttons/add_button.png",2,Vector(64,64))
        self.back_button.sprite.create_sprite_sheet("./Assets/UI/Buttons/back_button.png",2,Vector(32,32))
   
        # setup positions
        self.play_pause_position = Vector(self.screen_width,25)
        self.play_pause_button.sprite.position.x = self.screen_width
        self.play_pause_button.sprite.position.y = 25
        self.add_object_button.sprite.position.x = self.screen_width + self.play_pause_button.sprite.sprite_sheet[-1].get_width() + 5
        self.add_object_button.sprite.position.y = 25
        self.back_button.sprite.position.x = self.screen_width+10
        self.back_button.sprite.position.y = 170

        # create sprite sheet rects
        self.play_pause_button.sprite.create_sprite_sheet_rect()
        self.add_object_button.sprite.create_sprite_sheet_rect()
        self.back_button.sprite.create_sprite_sheet_rect()

        # add to ui element
        self.l_button_ui_elements = {'play':    self.play_pause_button,
                                     'add' :    self.add_object_button,
                                     'back':    self.back_button}
    

        