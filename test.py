from ursina import*
import time
import random
from ursina import input_handler
import pickle

input_handler.bind('w', 'up arrow')
input_handler.bind('s', 'down arrow')
input_handler.bind('a', 'left arrow')
input_handler.bind('d', 'right arrow')

app=Ursina(fullscreen=True, debug_mode=False, editor_ui_enabled=False)
 
window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.exit_button.enabled = True
window.cog_button.enabled=False
window.always_on_top=True
window.color=color.black

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.collider="box"
        
        self.start_textures={"left": (load_texture(f'assets/start_left{i:03d}.gif') for i in range(1, 5)), "right": (load_texture(f'assets/start_right{i:03d}.gif') for i in range(1, 5))}
        
        self.run_textures={"left": (load_texture(f'assets/left_running{i:03d}.gif') for i in range(1, 4)), "right": (load_texture(f'assets/right_running{i:03d}.gif') for i in range(1, 4))}
        self.texture=self.start_textures["right"]
        self.model="quad"
        self.current_textures=self.run_textures


    def controller(self):
        if held_keys["up arrow"]:  
            self.y+=self.speed*time.dt
        if held_keys["down arrow"]: 
            self.y-=self.speed*time.dt
        if not (held_keys["right arrow"] or held_keys["left arrow"] or held_keys["up arrow"] or held_keys["down arrow"]):
            pass
            #self.current_textures = self.start
        if held_keys["right arrow"]:  
            #self.current_textures = self.run_textures["right"]
            self.x+=self.speed*time.dt
        if held_keys["left arrow"]:   
            #self.current_textures = self.run_textures["left"]
            self.x-=self.speed*time.dt    

player=Player()

app.run()