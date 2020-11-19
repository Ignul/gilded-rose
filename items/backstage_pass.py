"""
"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
Quality drops to 0 after the concert
"""

from items.item import Item


class BackstagePass(Item):

    def update(self):
        # Between 5 and 10 (included) quality increases by 2
        if self.sell_in <= 10 and self.sell_in > 5:
            self.quality = self.quality + 2
        # Less than 5 days left - increase quality by 3
        elif self.sell_in <= 5 and self.sell_in > 0:
            self.quality = self.quality + 3
        # Quality 0 after concert.
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            # Standard increase
            self.quality = self.quality + 1

        # im stupid, going over 50 is not allowed.
        if self.quality > 50:
            self.quality = 50

        self.sell_in = self.sell_in - 1
