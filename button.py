base_color = (255,255,255)		#Button text changes to this text when clicked is false
clicked_color = (0,200,100)		# text color when clicked is true
class Button():
	# Default buttons that has text with no image
	def __init__(self, pos, text_input, font,clicked):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.clicked = clicked
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, base_color)
		self.image= None
		self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	# adds image to button and removes text,font
	def withImage(self, pos, image):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.clicked = False
		self.text = None
		self.font = None
		self.image = image
		self.text = self.image
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		return self

		
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
			return
		
		#changing text color only applies on default buttons with text 
		if self.clicked:
			self.text = self.font.render(self.text_input, True, clicked_color)
		else:
			self.text = self.font.render(self.text_input, True, base_color)

		screen.blit(self.text, self.text_rect)

	def clicked(self):
		return self.clicked
	
	def setClicked(self,flag):
		self.clicked = flag
	
	#check if button pressed
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			if self.image is None:
				self.text = self.font.render(self.text_input, True, clicked_color)
			return True
		return False
