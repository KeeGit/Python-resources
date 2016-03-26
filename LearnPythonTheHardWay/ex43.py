class Scene(object):

	def enter(self):
		pass

		
class Engine(object):

	def __init__(self, scene_map):
		pass
		
	def play(self):
		pass
	
class Death(Scene):

	def enter(self):
		pass
		
class CentralCorridor(Scene):

	def enter(self):
		print "Hero: Gothon, I challenge you to say a table of 2, if you want to defeat me."
		print "Enter table of 2 at the prompt, to two times ten."
		table_2 = int(raw_input(">"))
		
		if table_2 == [0 2 4 6 8 10]:
			print "Hero is defeated. Gotham wins."
		else:
			print "Gotham dies. Hero proceeds."
		pass
		
class LaserWeaponArmoury(Scene):

	def enter(self):
		print """You have entered the Laser Weapon Armoury room.
		 You have to type the unlock code to access the bomb.
		 You have only four attempts, and the unlock code is 4-digits long."""
		
		for i in range(5):
			guess_num = int(raw_input(">"))
			if guess_num == 6420:
				print "Keypad unlocked. Access to neutron bomb open."
		    else:
				print "Try again."
		
	pass
		
class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):
	
	def enter(self):
		pass
		
		
class Map(object):

	def __init__(self, start_scene):
		pass
	
	def next_scene(self, scene_name):
		pass
	
	def opening_scene(self):
		pass
		
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()