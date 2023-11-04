class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False

        count = Counter(hand)
        sorted_hand = sorted(hand)

        for card in sorted_hand:
            if count[card] == 0:
                continue

            for i in range(W):
                if count[card + i] > 0:
                    count[card + i] -= 1
                else:
                    return False

        return True
