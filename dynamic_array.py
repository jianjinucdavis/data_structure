

class DynamicArray:
    def __init__(self):
        self.array = []
        self.size = 0
        self.capacity = 0
        self.n_elements_copied = 0
        self.n_copying = 0

    def _is_valid_array(self):
        return self.capacity >= len(self.array) >= 0 and \
               len(self.array) == self.size

    def push_back(self, m):
        if self.size <= self.capacity - 1:
            self.size += 1
            self.array.append(m)
        else:
            # increment capacity by 2x
            self.capacity = 1 if self.capacity == 0 else 2 * self.capacity
            temp_array = self.array.copy()
            self.array = temp_array
            self.n_elements_copied += len(temp_array)
            self.n_copying += 1 if len(temp_array) > 0 else 0
            del temp_array
            self.size += 1
            self.array.append(m)
        assert self._is_valid_array(), "ARRAY INVALID"

    def pop_back(self):
        if self.size - 1 <= self.capacity/2:
            self.capacity = self.capacity/2
            self.array.pop()
            temp_array = self.array.copy()
            self.array = temp_array
            self.n_elements_copied += len(temp_array)
            self.n_copying += 1 if len(temp_array) > 0 else 0
            del temp_array
            self.size -= 1
        else:
            self.array.pop()
            self.size -= 1
        assert self._is_valid_array(), "ARRAY INVALID"

    def __dict__(self):
        return {
            "size": self.size,
            "capacity": self.capacity,
            "n_copying": self.n_copying,
            "n_elements_copied": self.n_elements_copied,
        }

    def print(self):
        print(self.array)


d_array = DynamicArray()
for i in range(1, 17):
    print(i)
    d_array.push_back(i)
    print(d_array.__dict__())
    print('=' * 10)

for i in range(8):
    print(i)
    d_array.push_back(100)
    print('PUSH BACK')
    print(d_array.__dict__())
    d_array.pop_back()
    print('POP BACK')
    print(d_array.__dict__())
    print('=' * 10)

print(d_array.__dict__())
d_array.print()

