class TestBarrelCls:

    def test_init(self, loto_barrel):
        bar = loto_barrel
        assert bar.number is None

    def test_num_set(self, loto_barrel):
        bar = loto_barrel
        bar.number = 7
        assert bar.number == 7

    def test_repr_none(self, loto_barrel):
        bar = loto_barrel
        assert bar.__repr__() == '  '

    def test_repr_num(self, loto_barrel):
        bar = loto_barrel
        bar.number = 7
        assert bar.__repr__() == '7'

    def test_repr_crossed(self, loto_barrel):
        bar = loto_barrel
        bar.is_crossed_out = True
        assert bar.__repr__() == '--'


class TestBagCls:

    def test_count(self, loto_bag):
        bag = loto_bag
        assert bag.count == bag.MAX_NUM

    def test_return_bag(self, loto_bag, loto_barrel):
        bag = loto_bag
        bar = loto_barrel
        assert type(bar) == type(bag.get_element())


class TestCartCls:

    def test_init_cart(self, loto_cart):
        cart = loto_cart
        size = cart.VERT_SIZE * cart.HORIZ_SIZE
        count_size = 0
        for row in cart._cart:
            count_size += len(row)
        assert size == count_size

    def test_cart_contains_bar(self, loto_cart, loto_barrel):
        cart = loto_cart
        bar = loto_barrel
        assert type(cart._cart[0][0]) == type(bar)

    def test_cart_win(self, loto_cart):
        cart = loto_cart
        for num in range(cart.MIN_NUM, cart.MAX_NUM + 1):
            cart.find_number(num)
        assert cart.is_win()

    def test_fill_num(self, loto_cart):
        count_num = 0
        cart = loto_cart
        for row in cart._cart:
            for num in row:
                if num.number is not None:
                    count_num += 1
        assert count_num == cart.VERT_SIZE * cart.POS_NUMS

    def test_uniq_num_in_cart(self, loto_cart):
        uniq_nums = set()
        cart = loto_cart
        for row in cart._cart:
            for num in row:
                tmp_num = num.number
                if tmp_num is not None:
                    if num not in uniq_nums:
                        uniq_nums.add(num)
                    else:
                        assert False
        assert True

    class TestPlayerCls:

        def test_win_player(self, loto_player):
            pl = loto_player
            for num in range(pl.MIN_NUM, pl.MAX_NUM + 1):
                pl.step(num)
            assert pl.is_win()

    def test_ret_loose(self, loto_player):
        pl = loto_player
        assert pl.is_loose == False

    def test_ret_is_human(self, loto_player):
        pl = loto_player
        assert pl.is_human == False
