from random import randrange


class BaseLoto:
    MIN_NUM = 1
    MAX_NUM = 90


class Barrel:
    def __init__(self, num=None):
        self._number = num
        self.is_crossed_out = False

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, num):
        self._number = num

    def __str__(self):
        return str(self._number)

    def __repr__(self):
        if self.is_crossed_out:
            return '--'
        elif not self._number:
            return '  '
        else:
            return f'{self._number}'


class Bag(BaseLoto):
    def __init__(self):
        self._list_of_barrels = None

    @classmethod
    def create_bag(cls):
        inst = cls()
        inst._list_of_barrels = [Barrel(num) for num in range(cls.MIN_NUM, cls.MAX_NUM + 1)]
        return inst

    @property
    def count(self):
        return len(self._list_of_barrels)

    def get_element(self):
        if self.count:
            return self._list_of_barrels.pop(randrange(start=0, stop=self.count))
        else:
            return None


class Cart(BaseLoto):
    VERT_SIZE = 3
    HORIZ_SIZE = 9
    POS_NUMS = 5

    def __init__(self):
        self._cart = None
        self._nums = set()
        self._positions = {}
        self._remaining_nums = self.VERT_SIZE * self.POS_NUMS
        self._create_cart()

    @staticmethod
    def rand_pos(num_pos, hor_size):
        """
        The function generates random positions for numbers
        """
        tmp = set()
        while len(tmp) < num_pos:
            tmp.add(randrange(start=0, stop=hor_size))
        return tmp

    def _create_cart(self):
        # gen empty cart
        self._cart = [[Barrel() for _ in range(self.HORIZ_SIZE)] for _ in range(self.VERT_SIZE)]
        # gen numbers
        while len(self._nums) < self.VERT_SIZE * self.POS_NUMS:
            self._nums.add(randrange(self.MIN_NUM, self.MAX_NUM + 1))
        nums_to_gen = (i for i in self._nums)
        # fill in cart with numbers
        for num_line in range(len(self._cart)):
            for pos in self.rand_pos(self.POS_NUMS, self.HORIZ_SIZE):
                tmp = next(nums_to_gen)
                barrel = self._cart[num_line][pos]
                barrel.number = tmp
                # save position of number
                self._positions[tmp] = num_line, pos

    def find_number(self, num):
        if num in self._nums:
            row, col = self._positions[num]
            barrel = self._cart[row][col]
            barrel.is_crossed_out = True
            self._remaining_nums -= 1
            return True
        return False

    def is_win(self):
        return self._remaining_nums == 0

    def show_cart(self):
        for row in self._cart:
            print(row)


class Player(Cart):
    def __init__(self, pl_num, is_human):
        super().__init__()
        self._player_num = pl_num
        self._is_human = is_human
        self._is_lose = False

    @property
    def player_num(self):
        return self._player_num

    @property
    def is_human(self):
        return self._is_human

    @property
    def is_loose(self):
        return self._is_lose

    def step(self, num):
        if self._is_lose:
            return
        is_find_num = self.find_number(num)
        if self.is_human:
            print('Зачеркнуть цифру?  (y/n)')
            a = ''
            while True:
                a = input()
                if a == 'y' or a =='n':
                    break
            if a == 'y':
                if not is_find_num:
                    print('К сожалению такой цифры нет. Вы проиграли :(')
                    self._is_lose = True
                else:
                    print('Есть такая цифра!')
            else:
                if is_find_num:
                    print('К сожалению такая цифра есть. Вы проиграли :(')
                    self._is_lose = True
                else:
                    print('Верно, такой цифры нет!')

    def show_cart(self):
        print('-' * 5 + f'Карточка игрока {self.player_num}' + '-' * 5)
        super().show_cart()
        print('-' * 35)



