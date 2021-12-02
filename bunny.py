import random

class BunnyHop:
    def __init__(self, size: int = 100) -> None:
        # size is up to but not including, valid indexes are [0, size)
        self._size = size
        self._bunny_location = 0
        self.setup_board()

    @property
    def size(self) -> int:
        return self._size

    def setup_board(self) -> None:
        self._bunny_location = random.randint(0, self._size - 1)

    def check(self, hole: int) -> bool:
        if hole == self._bunny_location:
            return True
        self._set_next_location()
        return False

    def _set_next_location(self) -> None:
        next_move = random.choice((-1, 1))
        new_location = self._bunny_location + next_move
        if new_location == self._size:
            new_location -= 2 # If the new location moves past the upper bound, step to the left
        elif new_location == -1:
            new_location += 2 # If the new location moves past the lower bound, step to the right
        self._bunny_location = new_location


def main():
    total = 10000
    found = 0
    even = 0
    odd = 0
    for _ in range(total):
        bunny = BunnyHop(100)
        found_bunny = False
        for i in range(bunny.size):
            if bunny.check(i):
                found_bunny = True
                even += 1
                break

        if not found_bunny:
            for i in range(1, bunny.size):
                if bunny.check(i):
                    found_bunny = True
                    odd += 1
                    break

        if found_bunny:
            found += 1

    print(f"found: {found}/{total} {found/total}")
    print(f"Even: {even} {even/total},  Odd: {odd} {odd/total}")

if __name__ == "__main__":
    main()