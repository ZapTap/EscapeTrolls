class Maze:
	def __init__(self):
		with open('start-maze', 'rt') as file:
			print(file.readline())
