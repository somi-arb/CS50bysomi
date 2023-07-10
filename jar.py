class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._size + n > self._capacity:
            raise ValueError("Not enough capacity to deposit cookies.")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(5)

    jar.deposit(4)

    jar.withdraw(1)

    print(jar)


if __name__ == "__main__":
    main()
