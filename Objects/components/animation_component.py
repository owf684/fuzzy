import pygame
class AnimationComponent:

    def __init__(self):
        try:
            self.elapsed_time = 0
            self.current_time = 0
            self.last_frame_time = 0

            self.frame_index = 0
            self.frame_duration = 0
            self.frame_count = 0
    
            self.timer_started = False

            self.current_time_2 = 0
            self.elapsed_time_2 = 0
            self.last_frame_time_2 = 0
            
        except Exception as Error:
            print("ERROR::anim_util.py::__init__()", Error)
            
    def determine_frame_count(self):
        try:
             
            self.current_time = pygame.time.get_ticks()
            self.elapsed_time = self.current_time - self.last_frame_time

            if self.elapsed_time >= self.frame_duration:
                self.frame_index = (self.frame_index + 1) % self.frame_count
                self.last_frame_time = self.current_time

        except Exception as Error:
            print("ERROR::anim_util.py::determine_frame_count", Error)
            
   
    def determine_time_elapsed(self):
        try:

            self.current_time_2 = pygame.time.get_ticks()
            self.elapsed_time_2 = self.current_time_2 - self.last_frame_time_2
            return self.elapsed_time_2
        except Exception as Error:
            print("ERROR::anim_util.py::determine_time_elapsed", Error)

    def reset_time_variables(self):
        try:

            self.elapsed_time_2 = 0
            self.current_time_2 = 0
            self.last_frame_time_2 = 0
            self.frame_index = 0
        except Exception as Error:
            print("ERROR::anim_util.py::reset_time_variables", Error)