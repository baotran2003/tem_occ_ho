from typing import List

class Solution:
    # def removeDuplicates(self, s: str) -> str:
    #     stack: List[int] = []
    #
    #     for char in s:
    #         if not stack:
    #             stack.append(char)
    #         else:
    #             if char == stack[-1]:
    #                 stack.pop()
    #             else:
    #                 stack.append(char)
    #
    #     return "".join(stack)

    def string_still_contains_duplicate(self, st: str):
        # check xem chuoi s co 2 ky tu giong nhau ko ?
            # yes -> return ve index dau tien if st[index] == st[index + 1]
            # no -> return -1
        # Example: abbaca -> return 1 -> pop st[1] and st[2] -> aaca
        #           ->   return 0 -> pop st[0] and st[1]    -> ca
        #           ko giong nhau giu nguyen chuoi

        for i in range (len(st) - 1):
            if st[i] == st[i + 1]:
                return i
        # ko tim thay cap nao
        return -1

    def removeDuplicates(self, s: str):
        while True:
            index: int = self.string_still_contains_duplicate(st = s)
            if index == -1:
                break
            s1: str = s[:index]
            s2: str = s[index + 2:]
            s = s1 + s2
        return s


if __name__ == "__main__":
    so: Solution = Solution()
    s: str = "abbaca"
    print(so.removeDuplicates(s))