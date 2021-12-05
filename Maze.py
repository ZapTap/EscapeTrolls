from typing import Iterator

class Maze:
	def __init__(self) -> None:
		# Import maze from file
		with open('start-maze', 'rt') as file:
			self._map = [[char for char in list(line) if char != '\n'] for line in file]
		self.CalculateNodes()


	def __str__(self) -> str:
		# Provides string representing the maze arrangement
		return '\n'.join(map(''.join, self._map))


	def _isValidSpace(self, coords: tuple) -> bool:
		x, y = coords
		if 0 <= y < len(self._map) and 0 <= x < len(self._map[y]):
			return (cell := self._map[y][x]) == ' ' or cell == 'X'

	def CalculateNodes(self):
		# This was difficult to read as a list comprehension
		# Collects all points in the map that are nodes
		def FindAllNodes() -> Iterator[list[tuple, list]]:
			for y, row in enumerate(self._map):
				for x, cell in enumerate(row):
					if self._isValidSpace((x, y)):
						yield [(x, y), []]

		def FindAllNeighbors():
			dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
			for node in self._nodes:
				candidates = []
				neighbors = []

				# Get every neighboring array loc and add to candidates list
				for __dir in dirs:
					x = node[0][0] + __dir[0]
					y = node[0][1] + __dir[1]
					candidates.append((x, y))

				# Check each location for validity
				for candidate in candidates:
					x, y = candidate
					if self._isValidSpace(candidate):
						neighbors.append(candidate)
				node[1] += neighbors


		self._nodes = [a for a in FindAllNodes()]
		FindAllNeighbors()
