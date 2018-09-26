# random-tony
Generator for chocolate flavours based on a context-free grammar. 
Written in Python 3.
Grammar available in Dutch and English.

Inspired by the limited edition Tony's Chocolonely flavours.

## Why
I wanted additional practice in generating text with grammars. Also, who doesn't love Tony's Chocolonely and weird chocolate flavours?

## Usage

```
$ python src/generate_flavours.py 
blonde chocolate with black currant, chili and salmon
dark milk chocolate with mayonnaise and peanuts
extra dark chocolate with black currant crumble and cola
dark chocolate with pumpkin and rooibos
milk chocolate with whipped cream, chili and pear crumble
extra dark chocolate with kiwi crumble and tonic
milk chocolate with coffeecrunch, cashews and rooibos
extra dark chocolate with jalapeno peppers and peanuts
white chocolate with green curry and pretzel
dark chocolate with fudge
```

If needed, you can change to the Dutch version of the grammar by substituting "tony_en" for "tony_nl" in `generate_flavours.py`.

## Used sources
Generating random sentences from a context free grammar - Eli Bendersky's website
http://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar/
