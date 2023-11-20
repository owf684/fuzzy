import sys
sys.path.append('./Objects')
sys.path.append('./Objects/components')
import environment_object
class WarpPipe(environment_object.EnvironmentObject):
		def __init__(self):
			super().__init__()
			self.current_sprite.create_sprite('./GameData/Assets/Environment/warp_pipe.png')
			self.physics.pause = True
			self.save_state.object_json_file='./GameData/jsons/warp_pipe.json'
def create_object():
	return WarpPipe()