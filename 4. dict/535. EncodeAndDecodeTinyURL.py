class Codec:
    def __init__(self):
        # Từ điển lưu trữ cặp (id: longUrl)
        self.map = {}
        self.id = 0
        self.BASE_URL = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Nhận URL dài, sinh ra URL ngắn và lưu vào dictionary."""
        self.id += 1  # Tăng ID
        self.map[self.id] = longUrl  # Gán giá trị vào dictionary với Key = self.id
        return self.BASE_URL + str(self.id)

    def decode(self, shortUrl: str) -> str:
        """Nhận URL ngắn, lấy ID ra và tra lại trong dictionary để trả về URL dài."""
        # Cắt bỏ phần "http://tinyurl.com/" để lấy ID dạng chuỗi
        id_string = shortUrl.replace(self.BASE_URL, "")

        # Ép kiểu chuỗi thành số nguyên để làm Key tra cứu
        key = int(id_string)

        # Lấy giá trị từ dictionary dựa vào Key
        return self.map.get(key)


# ==========================================
# HÀM MAIN ĐỂ TEST
# ==========================================
if __name__ == "__main__":
    # 1. Khởi tạo đối tượng
    codec = Codec()

    # Data test
    url1 = "https://leetcode.com/problems/design-tinyurl"
    url2 = "https://github.com/facebook/react"

    print("--- 1. TEST ENCODE (Rút gọn link) ---")
    short1 = codec.encode(url1)
    print(f"Original: {url1}")
    print(f"Shortened: {short1}\n")

    short2 = codec.encode(url2)
    print(f"Original: {url2}")
    print(f"Shortened: {short2}\n")

    print("--- 2. TRẠNG THÁI DICTIONARY TRONG BỘ NHỚ ---")
    print(f"self.map = {codec.map}\n")

    print("--- 3. TEST DECODE (Giải mã link) ---")
    decoded1 = codec.decode(short1)
    print(f"Input short URL: {short1}")
    print(f"Decoded long URL: {decoded1}\n")

    decoded2 = codec.decode(short2)
    print(f"Input short URL: {short2}")
    print(f"Decoded long URL: {decoded2}")