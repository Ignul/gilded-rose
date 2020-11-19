# Importing everything one by one for readability
from items.brie import Brie
from items.conjured import Conjured
from items.sulfuras import Sulfuras
from items.common import Common
from items.backstage_pass import BackstagePass

# Object assigning
class Naming(object):

    # Pretty self explanatory - get an object, assign it to the proper class
    def object_assign(self, name, sell_in, quality):
        if name == "Aged Brie": return Brie(name, sell_in, quality)
        elif name == "Sulfuras, Hand of Ragnaros": return Sulfuras(name, sell_in, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert": return BackstagePass(name, sell_in, quality)
        elif name == "Conjured Mana Cake": return Conjured(name, sell_in, quality)
        else: return Common(name, sell_in, quality)