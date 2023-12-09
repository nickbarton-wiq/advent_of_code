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
        self.bid = bid

    @property
    def cards(self):
        cards = {}
        for card in self.hand:
            if card not in cards:
                cards[card] = 1
            else:
                cards[card] += 1    

    def five_of_a_kind(self):
        for count in self.hand:
            if card != "hand" or card != "bid":
                if count == 5:
                    return True
        return False


    def four_of_a_kind(hand):
        for card, count in hand.items():
            if card != "hand" or card != "bid":
                if count == 4:
                    return True
        return False


def score_hand(data):
    for hand in data:
        cards = {"hand": hand[0], "bid": hand[1]}
        


if __name__ == '__main__':
    # data = get_data()
    # parsed_data = parse_data(data)
    # score_hand(parsed_data)

    print(five_of_a_kind({'hand': '32T3K', 'bid': '765', '3': 5}))
    print(five_of_a_kind({'hand': '32T3K', 'bid': '765', '3': 4, '2': 1}))
