
class BubbleSort:
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class InsertionSort:
    def sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)

if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]

    sorter = Sorter(BubbleSort())
    print(f"Bubble sorted: {sorter.sort_data(data[:])}")

    sorter.set_strategy(InsertionSort())
    print(f"Insertion sorted: {sorter.sort_data(data[:])}")
