import random

class Money:
	def __init__(self, start):
		self.cash = start

	def bet(self):

		try:
			self.amount = int(input("Bet: "))
		except:
			print("Error")
		if self.amount < self.cash:
			self.cash -= self.amount
			return True
		else:
			return False

	def increase(self):
		#for split and doubledown purposes
		pass


class Game:
	def __init__(self, deck):
		self.player = []
		self.croupier = []
		self.cards = deck

	def isace(self, deck):
		for number,element in enumerate(deck):
			if element == 11:
				deck[number] = 1
				return False
				break

		pass

	def give(self):
		return random.choice(list(self.cards.values()))

	def deal(self):
		self.player = [self.give(), self.give()]
		self.croupier = [self.give(), self.give()]

	def hit(self, deck):
		deck.append(self.give)
		if sum(deck) > 21 and isace(deck) == True:
			self.end()

	def doubledown(self, deck):
		deck.append(self.give)
		self.end(self.player, self.croupier)
		pass		

	def split(self, deck):
		self.first = [deck[0], self.give()]
		self.second = [deck[1], self.give()]
		pass

	def end(self, player, croupier):
		while sum(croupier) < 17:
			self.hit(croupier)
		if sum(player) < sum(croupier) and sum(croupier) > 21:
			return False
		elif sum(player) == sum(croupier):
			return None
		elif sum(player) > sum(croupier) and sum(player) > 21:
			return True
		else:
			return False
