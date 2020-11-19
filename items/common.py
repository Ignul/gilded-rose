"""
At the end of each day our system lowers both values for every item
Once the sell by date has passed, Quality degrades twice as fast
The Quality of an item is never negative
The Quality of an item is never more than 50
"""
from items.item import Item


class Common(Item):

    # New day updates for the common items.
    def update(self):
        # You should've sold the item by now, it degrades twice as fast.
        if self.sell_in <= 0:
            self.quality = self.quality - 2
        # Standard degradation
        elif self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
