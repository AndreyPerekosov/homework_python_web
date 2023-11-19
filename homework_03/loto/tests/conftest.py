from pytest import fixture
from clases.clases import Barrel, Bag, Cart, Player


@fixture(scope='function')
def loto_barrel():
    return Barrel()


@fixture(scope='function')
def loto_bag():
    return Bag.create_bag()


@fixture(scope='function')
def loto_cart():
    return Cart()


@fixture(scope='function')
def loto_player():
    return Player(1, False)
