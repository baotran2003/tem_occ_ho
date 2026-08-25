from typing import List, Tuple

class MyHashMap:

    """
    def __init__(self):
        self.map: List[int] = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1
    """

    def __init__(self):
        # Tạo 1000 thùng (bucket), mỗi thùng ban đầu là 1 list rỗng []
        self.size = 1000
        self.bucket: List[List[Tuple[int, int]]] = [
            [] for _ in range(self.size)
        ]

    def _hash(self, key: int) -> int:
        """Hàm băm: Ép key về chỉ số từ 0 đến 999"""
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index_bucket: int = self._hash(key)
        bucket: List[Tuple[int, int]] = self.bucket[index_bucket]

        # 1. Duyệt qua danh sách trong thùng xem key đã tồn tại chưa
        for i, (k, v) in enumerate(bucket):
            # (0, (1, 10))
            # (1, (1001, 30))
            # (2, (2001, 40))
            if k == key:
                bucket[i] = (key, value)    # neu co roi -> update key, value (that ra chi value)
                return

        # 2. Nếu chưa có -> Thêm cặp (key, value) mới vào thùng
        bucket.append((key, value))


    def get(self, key: int) -> int:
        index_bucket: int = self._hash(key)
        bucket: List[Tuple[int, int]] = self.bucket[index_bucket]

        # Duyệt trong thùng để tìm key
        for k, v in bucket:
            if k == key:
                return v
        return -1


    def remove(self, key: int) -> None:
        index_bucket: int = self._hash(key)
        bucket: List[Tuple[int, int]] = self.bucket[index_bucket]   # [[0, 200], [1, 5]]

        # Duyệt trong thùng để tìm và xóa key -> unpack = cah dung enumerate
        # (0, (0, 200))
        # (1, (1, 5))
        for i,  (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

def main():
    myMap = MyHashMap()

    print("===== Test put() =====")
    myMap.put(1, 10)
    myMap.put(2, 20)
    myMap.put(1001, 30)   # 1001 % 1000 = 1 -> collision với key = 1

    print(myMap.buckets)

    print("\n===== Test get() =====")
    print("get(1):", myMap.get(1))        # 10
    print("get(2):", myMap.get(2))        # 20
    print("get(1001):", myMap.get(1001))  # 30
    print("get(5):", myMap.get(5))        # -1

    print("\n===== Test update =====")
    myMap.put(2, 99)
    print("get(2):", myMap.get(2))        # 99

    print("\n===== Test remove() =====")
    myMap.remove(2)
    print("get(2):", myMap.get(2))        # -1

    myMap.remove(1001)
    print("get(1001):", myMap.get(1001))  # -1

    print("\n===== Buckets sau khi remove =====")
    print(myMap.buckets)


if __name__ == "__main__":
    main()