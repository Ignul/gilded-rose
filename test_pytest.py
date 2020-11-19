import pytest
from items.backstage_pass import BackstagePass
from items.brie import Brie
from items.common import Common
from items.conjured import Conjured
from items.sulfuras import Sulfuras
from gilded_rose import GildedRose

def test_update_common_quality_by_one():
    # Should be reducing quality by 1
    common_item = Common('Juice box', 20, 25)
    gilded_rose = GildedRose([common_item])

    gilded_rose.update_quality()
    assert common_item.quality == 24

def test_update_common_sellin_by_one():
    # Should be reducing sell_in by 1
    common_item = Common('Juice box', 15, 25)
    gilded_rose = GildedRose([common_item])

    gilded_rose.update_quality()
    assert common_item.sell_in == 14

def test_update_common_quality_by_two():
    # Should be reducing quality by two, cause according to sell_in it should be sold
    common_item = Common('Juice box', 0, 25)
    gilded_rose = GildedRose([common_item])

    gilded_rose.update_quality()
    assert common_item.quality == 23

def test_update_backstage_increase_quality_by_two():
    # Cause there are 9 days left, quality increase by two
    backstage_pass = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 9, 45)
    gilded_rose = GildedRose([backstage_pass])

    gilded_rose.update_quality()
    assert backstage_pass.quality == 47

def test_update_backstage_increase_quality_by_three():
    # Cause there are 9 days left, quality increase by three
    backstage_pass = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 4, 45)
    gilded_rose = GildedRose([backstage_pass])

    gilded_rose.update_quality()
    assert backstage_pass.quality == 48

def test_update_backstage_increase_quality_by_one():
    # Cause there are 21 days left, quality increase by one
    backstage_pass = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 21, 45)
    gilded_rose = GildedRose([backstage_pass])

    gilded_rose.update_quality()
    assert backstage_pass.quality == 46

def test_update_backstage_quality_over_50():
    # Quality can't go over 50, +1 should be not included in quality
    backstage_pass = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 21, 50)
    gilded_rose = GildedRose([backstage_pass])

    gilded_rose.update_quality()
    assert backstage_pass.quality == 50

def test_update_backstage_quality_0():
    # After concert the quality should be 0
    backstage_pass = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 0, 50)
    gilded_rose = GildedRose([backstage_pass])

    gilded_rose.update_quality()
    assert backstage_pass.quality == 0

def test_update_backstage_sellin():
    # Routine sell_in check
    backstage_pass = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 25, 30)
    gilded_rose = GildedRose([backstage_pass])

    gilded_rose.update_quality()
    assert backstage_pass.sell_in == 24

def test_update_brie_quality_over50():
    # Brie quality can't go over 50
    brie = Brie("Aged Brie", 24, 50)
    gilded_rose = GildedRose([brie])

    gilded_rose.update_quality()
    assert brie.quality == 50

def test_update_brie_quality_increase_by_1():
    # Brie increases quality by one as long as its sell_in is not negative
    brie = Brie("Aged Brie", 24, 30)
    gilded_rose = GildedRose([brie])

    gilded_rose.update_quality()
    assert brie.quality == 31

def test_update_brie_quality_increase_by_2():
    # Brie quality increases by two when the sell_in date is negative
    brie = Brie("Aged Brie", -1, 30)
    gilded_rose = GildedRose([brie])

    gilded_rose.update_quality()
    assert brie.quality == 32

def test_update_brie_quality_over_50():
    # Quality can't go over 50
    brie = Brie("Aged Brie", -1, 50)
    gilded_rose = GildedRose([brie])

    gilded_rose.update_quality()
    assert brie.quality == 50

def test_update_brie_sellin():
    # Sellin date decreasing by one
    brie = Brie("Aged Brie", 20, 30)
    gilded_rose = GildedRose([brie])

    gilded_rose.update_quality()
    assert brie.sell_in == 19

def test_update_conjured_sellin():
    # Sellin date decreasing by one
    conjured = Conjured("Conjured Mana Cake", 20, 30)
    gilded_rose = GildedRose([conjured])

    gilded_rose.update_quality()
    assert conjured.sell_in == 19

def test_update_conjured_quality_by_two():
    # Quality decrease by two when sellin is positive
    conjured = Conjured("Conjured Mana Cake", 20, 30)
    gilded_rose = GildedRose([conjured])

    gilded_rose.update_quality()
    assert conjured.quality == 28

def test_update_conjured_quality_by_four():
    # Quality decrease by four when sellin is negative
    conjured = Conjured("Conjured Mana Cake", -1, 30)
    gilded_rose = GildedRose([conjured])

    gilded_rose.update_quality()
    assert conjured.quality == 26

def test_update_sulfuras_nochange():
    # Sulfuras according to the rules never changes it's sellin or quality
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    gilded_rose = GildedRose([sulfuras])

    gilded_rose.update_quality()
    assert sulfuras.quality == 80
    assert sulfuras.sell_in == -1

# A lot more tests can be done, checking if user input is valid, etc.