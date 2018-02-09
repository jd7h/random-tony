#!/usr/bin/python
import random

tony = """
LIMITED_EDITION -> CHOCOLADESOORT SMAKEN
SMAKEN -> SMAAK | SMAAK SMAAK | SMAAK SMAAK SMAAK
SMAAK -> FRUIT | FRUITS CRUMBLE | NOTEN | DRANK | SNOEPGOED | KRUIDEN | OVERIG | RAAR
CRUMBLE -> crumble
FRUIT -> sinaasappel | ananas | framboos | peer | banaan | kokos | kers | cranberry | mango | kiwi | citroen | limoen | yuzu | zwarte bes | abrikoos | rozijn | vijg | gember | bosbes | meloen
FRUITS -> peren | bananen | kersen | cranberry | rabarber | appel
NOTEN -> hazelnoot | macadamia | walnoot | pecan | amandel | pinda | cashewnoot | pompoenpit | zonnebloempit | sesam
DRANK -> whiskey | rum | amaretto | cola | koffie | cappuccino | groene thee | matcha | gin | tonic
SNOEPGOED -> marshmallow | marsepein | zoete popcorn | zoute popcorn | discodip | noga | merengue | karamel | carrotcake | pretzel | bastogne | toffee | knettersuiker | suikerspin | speculoos | creme brulee | cookie dough | chocolate-chip | straciatella | cheesecake | stroopwafel | honingraat | fudge | haagse hopjes | pepernoten | pepermunt | negerzoen | winegums
KRUIDEN -> zeezout | zwarte peper | chili | rozemarijn | anijs | bergamot | kaneel | jasmijn | madame jeanette | rode peper | witte peper | laurier
OVERIG ->   honing | coffeecrunch | stoofpeer | nori | butterscotch | gepofte rijst | viooltjes | soyaboon | wasabi | rode curry | groene curry | pompoen | mais | jalapenopeper | balsamico
RAAR -> mayonaise | ketchup | soyasaus | bouillon | slagroom | zoute drop | zalmsnippers | komkommer
CHOCOLADESOORT -> melk | donkere melk | blonde chocola | extra puur | puur | wit | PUUR PERCENTAGE
PUUR -> puur
PERCENTAGE -> 30% | 50% | 60% | 70% | 80% | 90%
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
