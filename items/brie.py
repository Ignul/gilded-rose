# "Aged Brie" actually increases in Quality the older it gets
# Once the sell by date has passed, Quality degrades twice as fast

from items.item import Item


class Brie(Item):

    def update(self):
        if self.quality < 50 and self.sell_in > 0:
            self.quality = self.quality + 1
        # Date has passed, it increases in quality x2 ?
        elif self.quality <= 48 and self.sell_in <= 0:
            self.quality = self.quality + 2
        self.sell_in = self.sell_in - 1
