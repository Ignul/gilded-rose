# Conjured" items degrade in Quality twice as fast as normal item
# Copy - paste common update method, multiply numbers by 2 basically

from items.item import Item


class Conjured(Item):

    def update(self):
        # You should've sold the item by now, it degrades twice as fast.
        if self.sell_in <= 0:
            self.quality = self.quality - 4
        # Standard degradation
        elif self.sell_in > 0:
            self.quality = self.quality - 2
        self.sell_in = self.sell_in - 1
