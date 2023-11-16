from clases.clases import Bag, Player


def game():
    print('Добро пожаловать в игру Лото!')
    print('Введите количество игроков за которых играет компьютер')
    ai_pl = int(input())
    print('Введите количество игроков')
    hm_pl = int(input())
    players_count = 1
    print('Зовем игроков, изготовляем и перемешываем кубики.....')
    bag = Bag.create_bag()
    players = []
    for _ in range(ai_pl):
        players.append(Player(players_count, is_human=False))
        players_count += 1
    for _ in range(hm_pl):
        players.append(Player(players_count, is_human=True))
        players_count += 1
    while True:
        barrel = bag.get_element()
        if not barrel:
            print('Мешочек с бочонками пуст!')
            return
        for pl in players:
            if pl.is_human and not pl.is_loose:
                print(f'Новый бочонок {barrel} Всего бочонков осталось {bag.count}')
                print(f'Ваш игрок {pl.player_num}')
                pl.show_cart()
                print('Остальные игроки')
                for pl_to_show in players:
                    if not (pl is pl_to_show):
                        pl_to_show.show_cart()
            pl.step(barrel.number)
            if pl.is_win():
                print(f'Игрок номер {pl.player_num} выиграл!')
                return


if __name__ == '__main__':
    game()
