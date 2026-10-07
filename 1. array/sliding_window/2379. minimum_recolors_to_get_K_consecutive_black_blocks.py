class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_recolor_white: int = 0
        # First Window
        for i in range(k):
            if blocks[i] == "W":
                count_recolor_white += 1

        min_recolor_white: int = count_recolor_white

        # Sliding Window
        left: int = 0
        for right in range(k, len(blocks)):
            # l=r-k
            # expand right
            if blocks[right] == "W":
                count_recolor_white += 1

                # shirnk left
                if blocks[left] == "W":
                    count_recolor_white -= 1
                    left += 1

            min_recolor_white = min(min_recolor_white, count_recolor_white)

        return min_recolor_white

if __name__ == "__main__":
    so: Solution = Solution()
    blocks: str = "WWWWBBBBBB"
    k: int = 4
    print(so.minimumRecolors(blocks, k))