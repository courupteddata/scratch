import random

class BunnyHop:
    def __init__(self, size: int = 100) -> None:
        # size is up to but not including, valid indexes are [0, size)
        self._size = size
        self._bunny_location = 0
        self.place_bunny()

    @property
    def size(self) -> int:
        return self._size

    def place_bunny(self) -> None:
        self._bunny_location = random.randint(0, self._size - 1)

    def check(self, location: int) -> bool:
        if location == self._bunny_location:
            return True
        self._adjust_bunny()
        return False

    def _adjust_bunny(self) -> None: # On a wrong selection, adjust the bunny
        self._bunny_location += random.choice((-1, 1))
        if self._bunny_location == self._size:
            self._bunny_location -= 2 # If the new location moves past the upper bound, step to the left
        elif self._bunny_location == -1:
            self._bunny_location += 2 # If the new location moves past the lower bound, step to the right


def _main():
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
    _main()