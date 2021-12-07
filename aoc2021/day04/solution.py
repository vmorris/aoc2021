from aoc2021.util import get_input_day04
from aoc2021.day04.card import Card

def mark(cards, number):
    print(f"There are {len(cards)} cards remaining.")
    print(f"Marking {number} off.")
    for card in cards:
        card.mark(number)

def check(cards, part):
    for index, card in enumerate(cards):
        bingo = card.check()
        if part == "one":
            if bingo is not None:
                return card
        if part == "two":
            if bingo is not None and len(cards) == 1:
                return card
            elif bingo is not None:
                print(f"Removing card {card} as winner:")
                print(card.matrix)
                print(card.marked)
                cards.remove(card)

def solve_part1(entries):
    numbers = entries[0]
    cards = list()
    _cards = entries[1]
    for card in _cards:
        cards.append(Card(card))
    for number in numbers:
        mark(cards, number)
        winning_card = check(cards, part="one")
        if winning_card:
            break
    return winning_card.sum_unmarked() * number


def solve_part2(entries):
    numbers = entries[0]
    cards = list()
    _cards = entries[1]
    for card in _cards:
        cards.append(Card(card))
    for number in numbers:
        mark(cards, number)
        last_card = check(cards, part="two")
        if last_card:
            break
    print(last_card.matrix)
    print(last_card.marked)
    print(number)
    return last_card.sum_unmarked() * number


if __name__ == "__main__":  # pragma: no cover
    entries = get_input_day04("aoc2021/day04/input")
    #print(solve_part1(entries))
    print(solve_part2(entries))
