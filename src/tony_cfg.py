tony_nl = """
S -> LIMITED_EDITION
LIMITED_EDITION -> CHOCOLADESOORT SMAKEN
SMAKEN -> SMAAK | SMAAK SMAAK | SMAAK SMAAK SMAAK
SMAAK -> FRUIT | FRUITS CRUMBLE | NOTEN | DRANK | SNOEPGOED | KRUIDEN | GROENTEN | OVERIG | RAAR
CRUMBLE -> crumble
FRUIT -> sinaasappel | ananas | framboos | peer | banaan | kokos | kers | cranberry | mango | kiwi | citroen | limoen | yuzu | zwarte bes | abrikoos | rozijn | vijg | gember | bosbes | meloen
FRUITS -> peren | bananen | kersen | cranberry | rabarber | appel
NOTEN -> hazelnoot | macadamia | walnoot | pecan | amandel | pinda | cashewnoot | pompoenpitten | zonnebloempitten | sesamzaadjes | pistache
DRANK -> whiskey | rum | amaretto | cola | koffie | cappuccino | groene thee | matcha | gin | tonic | rooibos
SNOEPGOED -> marshmallows | marsepein | zoete popcorn | zoute popcorn | discodip | noga | merengue | karamel | carrotcake | pretzel | bastogne | toffee | knettersuiker | suikerspin | speculoos | crème brûlée | cookie dough | chocolate-chip | straciatella | cheesecake | stroopwafel | honingraat | fudge | haagse hopjes | pepernoten | pepermunt | negerzoen | winegums | praline
GROENTEN -> komkommer | geraspte wortel | rode biet | nori | pastinaak | pompoen | soyaboontjes | mais
KRUIDEN -> zeezout | zwarte peper | chili | rozemarijn | anijs | bergamot | kaneel | jasmijn | madame jeanette | rode peper | witte peper | laurier | venkelzaad | kardemom | kruidnagel | nootmuskaat 
OVERIG ->   honing | coffeecrunch | stoofpeer | butterscotch | gepofte rijst | viooltjes | wasabi | rode curry | groene curry | jalapenopeper | balsamico | lavendel | rozenblaadjes 
RAAR -> mayonaise | ketchup | soyasaus | bouillon | slagroom | zoute drop | zalmsnippers
CHOCOLADESOORT -> melkchocolade | donkere melkchocolade | blonde chocolade | extra pure chocolade | pure chocolade | witte chocolade
"""

tony_en = """
S -> LIMITED_EDITION
LIMITED_EDITION -> CHOCOLATETYPE INGREDIENTS
CHOCOLATETYPE -> milk chocolate | dark milk chocolate | blonde chocolate | extra dark chocolate | dark chocolate | white chocolate
INGREDIENTS -> INGREDIENT | INGREDIENT INGREDIENT | INGREDIENT INGREDIENT INGREDIENT
INGREDIENT -> FRUIT | FRUIT CRUMBLE | NUTS | DRINK | SWEET | SPICE | VEGETABLE | MISC | WEIRD
CRUMBLE -> crumble
FRUIT -> orange | pineapple | raspberry | pear | banana | coconut | cherry | cranberry | mango | kiwi | lemon | lime | yuzu | black currant | apricot | raisin | figs | ginger | blueberry | melon | rhubarb
NUTS -> hazelnuts | macadamias | walnuts | pecans | almonds | peanuts | cashews | pumpkin seeds | sunflower seeds | sesame seeds | pistachios
DRINK -> whiskey | rum | amaretto | cola | coffee | cappuccino | green tea |matcha | gin | tonic | rooibos
SWEET -> marshmallows | marzipan | sweet popcorn | salty popcorn | nougat | merengue | caramel | carrotcake | pretzel | toffee | cotton candy | speculoos | crème brûlée | cookie dough | chocolate chips | straciatella | cheesecake | honeycomb | fudge | peppermint | winegums | praline
VEGETABLE -> cucumber | grated carrot | beet | nori | parsnip | pumpkin | soy beans | corn
SPICE -> sea salt | black pepper | chili | rosemary | aniseed | bergamot | cinnamon | jasmine | madame jeanette | bell pepper | white pepper | pink pepper | laurel | fennel seeds | cardamom | clove | nutmeg
MISC -> honey | coffeecrunch | butterscotch | wasabi | red curry | green curry | jalapeno peppers | balsamic vinegar | lavender | rose petals | cornflakes
WEIRD -> mayonnaise | ketchup | soy sauce | broth | whipped cream | liquorice | salmon
"""
