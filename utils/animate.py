def animate(armature, name, start_frame, end_frame, blend=4):
		armature.playAction(name, start_frame, end_frame, blendin=blend)