import sys
sys.path.append('./Objects')
sys.path.append('./Objects/components')
import environment_object
class WarpPipeExtension(environment_object.EnvironmentObject):
		def __init__(self):
			super().__init__()
			self.current_sprite.create_sprite('./GameData/Assets/Environment/warp_pipe_extended.png')
			self.physics.pause = True
			self.save_state.object_json_file='./GameData/jsons/warp_pipe_extension.json'


		def update(self):
			None

def create_object():
	return WarpPipeExtension()
