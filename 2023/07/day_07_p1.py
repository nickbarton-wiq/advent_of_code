from typing import List, Dict


def get_data():
    with open('2023/day_07.input') as f:
        return f.read().splitlines()


def parse_data(data):
    hands_list = [line.split() for line in data]
    output = []
    for hand_and_bid in hands_list:
        hand = hand_and_bid[0]
        bid = hand_and_bid[1]
        output.append([hand, bid])
    return output


class Hand():
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)

    @property
    def cards(self) -> Dict[str, int]:
        """Returns a dictionary with the cards in the hand as keys and the number of re-occurring cards as values"""
        cards = {}
        for card in self.hand:
            if card not in cards:
                cards[card] = 1
            else:
                cards[card] += 1
        return dict(sorted(cards.items(), key=lambda item: item[1]))

    @property
    def type(self) -> str:
        """Returns the type of the hand as a string"""
        if self.five_of_a_kind():
            return 'Five of a kind'
        elif self.four_of_a_kind():
            return 'Four of a kind'
        elif self.full_house():
            return 'Full house'
        elif self.three_of_a_kind():
            return 'Three of a kind'
        elif self.two_pair():
            return 'Two pair'
        elif self.one_pair():
            return 'One pair'
        elif self.high_card():
            return 'High card'
        else:
            return 'Something went wrong'

    def type_rank(self) -> int:
        """Returns the type of the hand as a number"""
        if self.five_of_a_kind():
            return 7
        elif self.four_of_a_kind():
            return 6
        elif self.full_house():
            return 5
        elif self.three_of_a_kind():
            return 4
        elif self.two_pair():
            return 3
        elif self.one_pair():
            return 2
        elif self.high_card():
            return 1
        else:
            return 0

    def five_of_a_kind(self) -> bool:
        """Checks if the hand is a five of a kind"""
        if len(self.cards) == 1:
            if self.get_first_card_count(0) == 5:
                return True
        return False

    def four_of_a_kind(self) -> bool:
        """Checks if the hand is a four of a kind"""
        if len(self.cards) == 2 and self.get_last_card_count() == 4:
            return True
        return False

    def full_house(self) -> bool:
        """Checks if the hand is a full house"""
        if len(self.cards) == 2 and self.get_last_card_count() == 3 and self.get_first_card_count(0) == 2:
            return True
        return False

    def three_of_a_kind(self) -> bool:
        """Checks if the hand is a three of a kind"""
        if len(self.cards) == 3 and self.get_last_card_count() == 3:
            return True
        return False

    def two_pair(self) -> bool:
        """Checks if the hand is a two pair"""
        if len(self.cards) == 3 and self.get_last_card_count() == 2 and self.get_first_card_count(0) == 1:
            return True
        return False

    def one_pair(self) -> bool:
        """Checks if the hand is a one pair"""
        if len(self.cards) == 4 and self.get_last_card_count() == 2:
            return True
        return False

    def high_card(self) -> bool:
        """Checks if the hand is a high card"""
        if len(self.cards) == 5:
            return True
        return False

    def get_last_card_count(self) -> int:
        """Gets the count of the least occuring card in the hand"""
        return list(self.cards.items())[-1][1]

    def get_first_card_count(self, n) -> int:
        """Gets the count of the most ocurring in the hand"""
        return list(self.cards.items())[n][1]

    def get_nth_card(self, n) -> str:
        """Gets the nth card in the hand, ordered as received from the dealer"""
        return self.hand[n]

    def hand_strength(self) -> tuple:
        """Converts a hand into a tuple representing its strength. The tuple is used to compare hands"""
        card_order = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3,
                      "3": 2, "2": 1}
        return tuple(card_order[card] for card in self.hand)


def create_hands(data) -> List[Hand]:
    """Creates a list of Hand objects from the data"""
    return [Hand(hand[0], hand[1]) for hand in data]


def rank_hands_by_type(hands: List[Hand]) -> List[Dict[str, Hand]]:
    """Ranks hands by type, returns a list of dictionaries with the hand type as key and the hand as value"""
    hand_rank_list = []
    for i in range(1, 8):
        hand_rank = {}
        for hand in hands:
            if hand.type_rank() == i:
                if hand.type_rank() not in hand_rank:
                    hand_rank[i] = [hand]
                else:
                    hand_rank[i].append(hand)
        hand_rank_list.append(hand_rank)
    return hand_rank_list


def rank_hands_by_type_and_strength(hand_rank_list: List[Dict[str, Hand]]) -> List[Hand]:
    """Ranks all hands by type and then by strength, then calculate and return the score"""
    ranked_hands = []
    for hand_rank in hand_rank_list:
        if len(hand_rank) > 0:
            hand_list = next(iter(hand_rank.values()))
            sorted_hands = rank_hands_by_strength(hand_list)
            for hand in sorted_hands:
                ranked_hands.append(hand)
    return ranked_hands


def rank_hands_by_strength(hands: List[Hand]) -> List[Hand]:
    """Sort hands of the same type based on their strength"""
    return sorted(hands, key=lambda x: x.hand_strength())


def score_hands(hands: List[Hand]) -> int:
    """Calculates the score of a hand"""
    hands_score = [x.bid * i for i, x in enumerate(hands, start=1)]
    score = sum(hands_score)
    return score


if __name__ == '__main__':
    data = get_data()
    parsed_data = parse_data(data)
    hands = create_hands(parsed_data)
    hands = rank_hands_by_type(hands)
    hands = rank_hands_by_type_and_strength(hands)
    score = score_hands(hands)
    print(score)
