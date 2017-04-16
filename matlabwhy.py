import random

class MatlabWhy(object):
	def __init__(self):
		self.nouns = ['bunny', 'Product Owner', 'foot', 'lunchbox', 'contraption', 'developer', 'shoe']
		self.adjectives = ['terrified', 'smelly', 'well-meaning', 'hoodie-wearing', 'beautiful']
		self.verbs = ['said so', 'wanted it', 'was watching']
		self.bne = 'but not excessively'
		self.start = ['because the', 'the']

	def capitalize(self, sentence):
		return sentence[:1].upper() + sentence[1:] 

	def word_from_list(self, lst):
		word = random.randint(0, len(lst)-1)
		return str(lst[word])

	def construct_sentence(self):
		sentence = [self.word_from_list(self.start)]
		adj = self.word_from_list(self.adjectives)
		sentence.append(adj)
		if random.random() > 0.75:
			sentence.append(self.bne)
			sentence.append(adj)
		sentence.append(self.word_from_list(self.nouns))
		sentence.append(self.word_from_list(self.verbs)+".")
		return self.capitalize(" ".join(sentence))