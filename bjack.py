from random import randint
from libs import Konsola

def Random():
	return randint(2,11)

class Money():
	def __init__(self):
		self.kasa = 500 
		self.stawka = 0
	def bet(self):
		while True:
		
			try:
				print("Twoja aktualne fundusze: ", self.kasa)
				self.stawka = int(input("Wielkosc zakladu: "))
			except KeyboardInterrupt:
				quit()
			except:
				print("Wpisz poprawną liczbę! ")
				continue
			else:
				pass
			if self.kasa >= self.stawka:
				self.kasa -= self.stawka
				return print("Twoje pieniadze: ",self.kasa)
			else:
				print("Masz za malo pieniedzy!")
				continue

class Deck(Money):

	def __init__(self):
		Money.__init__(self)
		self.gracz = []
		self.krupier = []

	def ace(self,tablica, reduce):
		if reduce:
			x = 0
			for element in tablica:
				if element == 11:
					tablica[x] = 1
					break
				x += 1
				for element in tablica:
					if element == 11:
						return True
					return False


	def start(self):
		#rozdanie dwoch kart krupierowi (odkrycie jednej) oraz dwoch graczowi
		self.gracz = [10, 10]
		self.krupier = [Random(), Random()]
		return self.gracz, self.krupier


	def hit(self):
		#dobranie kolejnej karty
		self.gracz.append(Random())

	def doubledown(self):
		if self.kasa >= self.stawka:
			self.kasa -= self.stawka
			self.stawka = self.stawka*2
			self.gracz.append(Random())
			self.stand()
			pass
		else:
			print("Masz niewystarczajace fundusze!")

	def split(self):
		if self.gracz[0] == self.gracz[1] and self.kasa >= self.stawka:
			done = False
			self.kasa -= self.stawka
			pierwsza = [self.gracz[0], Random()]
			druga = [self.gracz[0], Random()]
			while not done:
				print("Pierwsza reka: ", pierwsza)
				schoice = int(input("Hit - 1, Stand - 2"))
				if schoice == 1:
					pierwsza.append(Random())
				else:
					self.stand()
					done = True
			while done:
				print("Druga reka: ", druga)
				schoice = int(input("Hit - 1, Stand - 2"))
				if schoice == 1:
					druga.append(Random())
				else:
					self.stand()
					done = False
		else:
			pass
		pass

	def stand(self):
		#nie dobieranie kolejnej karty, koniec gry
		print("Zakończyłeś grę: ")
		while sum(self.krupier) < 17:
			#jezeli karty krupiera maja wspolna wartosc < 17 musi dobrac karty
			print("Krupier musi dobrac karte")
			self.krupier.append(Random())
		print("Karty Krupiera to:", self.krupier)
		print("Twoje karty to: ", self.gracz)
		if sum(self.gracz) < sum(self.krupier) < 21:
			print("Przegrales")
		elif sum(self.gracz) == sum(self.krupier):
			self.kasa += self.stawka
			print("Remis")
		else:
			print("Wygrales!")
			self.kasa += self.stawka*1.5

	def over(self):
		#odpowiednik fury z blackjacka, jezeli suma kart przekroczy 21
		if sum(self.gracz) > 21:
			if gra.ace(self.gracz,0) and sum(self.gracz) > 21:
				gra.ace(self.gracz, 1)
				print(self.gracz)
			print("Przegrales!, liczba jest wyższa od 21!")
			return True
		else:
			return False
konsola = Konsola()
gra = Deck()
while True:
	gra.bet()
	gra.start()
	konsola.clear()
	while gra.over() == False:
		print("Twoje karty to: ", gra.gracz, "Suma Twoich kart: ", sum(gra.gracz))
		print("Karty krupiera: ", gra.krupier[1])
		choice = int(input("Hit - 1 Double Down - 2 Split - 3 Stand - 4: "))
		if choice == 1:
			gra.hit()
			konsola.clear()
		elif choice == 2:
			gra.doubledown()
			break
		elif choice == 3:
			gra.split()
			break
		else:
			gra.stand()	
			break
