class JoyStick2D():
	def __init__(self,spi=None):
		self.spi = 	spi
		self.swt_channel = 0
		self.vrx_channel = 1
		self.vry_channel = 2	
		self.mid_point = (512,500)
		self.mid_x = 513
		self.mid_y = 498
		self.stdev = 2
		self.x_max = (1013,1023)
		self.x_min = (1,10)
		self.y_min = (1,10)	
		self.y_max = (1013,1023)		

		self.mcp = MCP3208()	

	def mapjs2scr(self,jsx,jsy):
		jsy = JOYSTICK_DIM[1] - jsy
		scr_x = (jsx * SCREEN_DIM[0]) // JOYSTICK_DIM[0]
		scr_y = (jsy * SCREEN_DIM[1]) // JOYSTICK_DIM[1]
		return (scr_x,scr_y)
	
	def get_pos(self):
		xpos = self.mcp.read_adc(self.vrx_channel)
        	ypos = self.mcp.read_adc(self.vry_channel)
 		#pos_scr = self.mapjs2scr(xpos,ypos)
		return (xpos,ypos)

	def get_direction(self):
		dir = [0,0,0,0] # left,right,up,down,stop
		(xpos,ypos) = self.get_pos()
		'''
		X		Y		L	R	U	D	S 	dir
		===========================================================
		0-256	0-256	1	0	1	0	0	upper left
		0-256	256-770	1	0	0	0	0	left
		0-256	770-1023	1	0	0	1	0	lower left
		256-770	770-1023	0	0	0	1	0	lower
		770-1023	770-1023	0	1	0	1	0	lower right
		770-1023	256-770	0	1	0	0	0	right		
		770-1023	0-256	0	1	1	0	0	upper right
		256-770	0-256	0	0	1	0	0	up
		============================================================
		'''
		if (xpos <= 256) and (ypos <= 256) :
			dir = [1,0,1,0,0] # upper left
		elif (xpos < 256) and ((ypos >= 256) and (ypos <= 770)) :
			dir=[1,0,0,0,0] # left
		elif (xpos < 256) and (ypos > 770 and (ypos <= 1023)) :
			dir = [1,0,0,1,0] # lower left
		elif (xpos >= 256 and xpos <= 770) and ( ypos > 770 and ypos <= 1023 ):
			dir =  [0,0,0,1,0] # lower
		elif (xpos > 770 and xpos <= 1023) and (ypos > 770 and ypos <= 1023):
			dir = [0,1,0,1,0] #lower right
		elif (xpos > 770 and xpos <= 1023) and (ypos >= 256 and ypos <= 770):
			dir = [0,1,0,0,0] # right
		elif (xpos > 770 and xpos <= 1023) and (ypos >= 0 and ypos < 256):
			dir = [0,1,1,0,0] # upper right
		elif (xpos >= 256 and xpos <= 770) and (ypos >=0 and ypos < 256):
			dir = [0,0,1,0,0] # up
		else :
			dir = [0,0,0,0,1]
		
		return dir
		
	def get_angle(self,xpos,ypos):
		dx = xpos - self.mid_x  
		dy = ypos - self.mid_y
		if (abs(dx) < self.stdev) and (abs(dy) < self.stdev) :
			#return -90
			return None
		angle = math.atan2(dy,dx)
		return int(math.degrees(angle))
