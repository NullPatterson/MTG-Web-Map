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
### Card ID:
Types-ColorIdentity-CMC-IndexInList

Card types are
Legendary - 0
Artifact - 1
Battles - 2
Creature - 3
Enchantments - 4
Instants - 5
Lands - 6
Planeswalkers - 7
Sorceries - 8

#### Example
A Legendary Artifact Enchatment Creature with CMC of 5 and color identity BG and is the 255th item would have an ID of:
0134-BG-5-254

### Colors:
Black = B
Blue = U
White = W
Red = R
Green = G
Colorless = N