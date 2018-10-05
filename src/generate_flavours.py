#!/usr/bin/env python3

import cfg_generator
import logging
from tony_cfg import tony_en as cfg

def format_output(generatedoutput):
    ingredients = list(cfg_generator.flatten(generatedoutput))
    logging.info("fixing percentage...")
    for index,ingredient in enumerate(ingredients):
        if "%" in ingredient: # vieze fix percentage
            puur_index = index-1
            ingredients[index]= ingredients[puur_index] + " " + ingredients[index]
            ingredients.pop(puur_index)
    logging.info("fixing crumble...")
    for index,ingredient in enumerate(ingredients):
        if ingredient == "crumble": # crumble can never be the first item
            fruit_index = index-1
            ingredients[index]= ingredients[fruit_index] + " " + "crumble"
            ingredients.pop(fruit_index)
    logging.info("Fixing duplicates...")
    ingredients = list(dict.fromkeys(ingredients))
    if len(ingredients) > 2:
        smaak = '{} with {} and {}'.format(ingredients[0], ', '.join(ingredients[1:-1]), ingredients[-1])
    else:
        smaak = '{} with {}'.format(ingredients[0], " ".join(ingredients[1:]))
    return smaak

def generate_tony_flavours(cnt):
    ldg = cfg_generator.Grammar() # limited_edition_grammar
    ldg.parse_grammar(cfg)
    for i in range(0,cnt):
        generatedoutput = ldg.generate('S')
        #print('-'.join(flatten(ldg.generate('S'))))
        print(format_output(generatedoutput))

if __name__ == "__main__":
     generate_tony_flavours(10)
