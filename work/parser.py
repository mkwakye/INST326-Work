import re

def make_pairings(character_list):
	set_of_pairings = set()

	#["hamlet", "witch2", "witch2", "hamlet", "witch3"]

	for char1 in character_list:
		for char2 in character_list:
			pairing = frozenset(set([char1, char2]))

			if len(pairing) > 1:
				set_of_pairings.add(pairing)

	return set_of_pairings

class Works:
	def __init__(self, path):
		with open(path) as f:
			self.text = f.read()

		self.scenes = self.text.split('SCENE')[:-1]
		print(self.scenes)

	def find_character(self):
		self.character = []

		for scene in self.scenes:
			characters = re.findall(r"(([A-Z]|\s)+)\.[\r\n]", scene)
			characters = [i[0].strip() for i in characters if len(i[0].strip()) > 3]
			
			if characters != [""]:
				self.character.append(set(characters))

	def create_adjecency_list(self):
		with open("list.csv", "w") as f:
			for i in self.character:
				pairings = make_pairings(i)

				for couple in pairings:
					f.write(str(list(couple)[0]) + "," + str(list(couple)[1]) + "\n")

if __name__ == '__main__':
	book = Works("shakespear.txt")
	book.find_character()
	book.create_adjecency_list()
