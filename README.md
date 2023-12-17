# sudo-deckbuilder
 No idea what i am doing but my goal is to create something similar to edhrec but can be tailored ot better fit specific playstyles

## Database
The database of cards this project will be referencing will be pulled from Scryfall's bulk data at: https://data.scryfall.io/oracle-cards/oracle-cards-20231216220200.json
The data from the json object that will be pulled is:
name
lang (*Will use "en" as a key to check the language*)
image_uris.normal (*A png option is also available if i decide to try it*)
mana_cost
cmc
type_line
oracle_text
colors
color_identity
keywords
legalities
prices.usd

## Shorthand (Derived from Scryfall Syntax)
### Colors:
Black = B
White = W
Red = R
Blue = U
Green = G
Colorless = N