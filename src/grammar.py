#!/usr/bin/python
import random

tony = """
LIMITED_EDITION -> CHOCOLADESOORT SMAKEN
SMAKEN -> SMAAK | SMAAK SMAAK | SMAAK SMAAK SMAAK
SMAAK -> FRUIT | FRUITS CRUMBLE | NOTEN | DRANK | SNOEPGOED | KRUIDEN | OVERIG
CRUMBLE -> crumble
FRUIT -> sinaasappel | ananas | peer | banaan | kokos | kers | cranberry | mango | kiwi | citroen | limoen | zwarte-bes | abrikoos
FRUITS -> peren | bananen | kersen | cranberry | rabarber | appel
NOTEN -> hazelnoot | macadamia | walnoot | pecan | amandel | pinda | cashewnoot
DRANK -> whiskey | rum | amaretto | cola | koffie
SNOEPGOED -> marshmallow | marsepein | popcorn | discodip | noga | merengue | karamel | carrot-cake
KRUIDEN -> zeezout | zwarte-peper | chili | rozemarijn | anijs | bergamot | kaneel
OVERIG ->   honing | coffee-crunch
CHOCOLADESOORT -> melk | puur | wit
"""

class Grammar:
	def __init__(self):
		self.rules = {}

	def add_rule(self,lhs,rhs):
		self.rules[lhs] = []
		rhs = rhs.split('|') # returns list of options
		for r in rhs:
			self.rules[lhs].append(r.split())

	def generate(self,symbol):
		sentence = []
		choice = random.choice(self.rules[symbol]) # pick random
		for part in choice:
			if part in self.rules.keys():
				sentence.append(self.generate(part))
			else:
				sentence.append(part)
		return sentence

	def parse_rule(self,line):
		try:
			lhs,rhs = line.split('->')
		except:
			return
		lhs = lhs.strip()
		rhs = rhs.strip()
		self.add_rule(lhs,rhs)

	def parse_grammar(self,grammarstring):
		rules = grammarstring.split('\n')
		for rule in rules:
			self.parse_rule(rule)

def flatten(foo):
    for x in foo:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in flatten(x):
                yield y
        else:
            yield x

def generate_tony_flavours():
	ldg = Grammar() # limited_edition_grammar
	ldg.parse_grammar(tony)
	for i in range(0,10):
		print('-'.join(flatten(ldg.generate('LIMITED_EDITION'))))


if __name__ == "__main__":
    generate_tony_flavours()
