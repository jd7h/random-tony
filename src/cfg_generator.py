#!/usr/bin/python
import random

class Grammar:
    def __init__(self):
        self.rules = {}

    def add_rule(self,lhs,rhs):
        self.rules[lhs] = []
        rhs = rhs.split('|') # returns list of options
        for r in rhs:
            if r.isupper(): #if non-terminal
                self.rules[lhs].append(r.split())
            else:
                self.rules[lhs].append(r.strip())

    def generate(self,symbol):
        sentence = []
        choice = random.choice(self.rules[symbol]) # pick random)
        if type(choice) != list:
            sentence.append(choice)
            return sentence
        else:
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

    def get_terminals(self,symbol=None):
        if symbol != None:
            if symbol not in self.rules.keys():
                return []
            else:
                return [term for term in list(flatten(self.rules[symbol])) if not term.isupper()]
        else:
            return [term for term in list(flatten(self.rules.values())) if not term.isupper()]

    def get_nonterminals(self):
        lhs = set(self.rules.keys())
        lhs.remove("S")
        rhs = set([term for term in list(flatten(self.rules.values())) if term.isupper()])
        if lhs != rhs:
            return list(lhs), list(rhs)
        return list(lhs)

    # assertion: terminals are unique
    def get_parent(self,terminal):
        if terminal in self.get_terminals():
            for nonterm in self.rules:
                if terminal in self.rules[nonterm]:
                    return nonterm
        return None

def flatten(foo):
    for x in foo:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in flatten(x):
                yield y
        else:
            yield x
