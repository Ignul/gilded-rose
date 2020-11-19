# -*- coding: utf-8 -*-
from __future__ import print_function
from gilded_rose import GildedRose
from items.object_assign import Naming


if __name__ == "__main__":
    print ("OMGHAI!")
    naming = Naming()
    items = [
             naming.object_assign(name="+5 Dexterity Vest", sell_in=10, quality=20),
             naming.object_assign(name="Aged Brie", sell_in=2, quality=0),
             naming.object_assign(name="Elixir of the Mongoose", sell_in=5, quality=7),
             naming.object_assign(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             naming.object_assign(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             naming.object_assign(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             naming.object_assign(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             naming.object_assign(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             naming.object_assign(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 8
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
