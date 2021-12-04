class Maze:
	def __init__(self) -> None:
		# Import maze from file
		with open('start-maze', 'rt') as file:
			self._map = [[char for char in list(line) if char != '\n'] for line in file]


	def __str__(self) -> str:
		# Provides string representing the maze arrangement
		return '\n'.join(map(''.join, self._map))
