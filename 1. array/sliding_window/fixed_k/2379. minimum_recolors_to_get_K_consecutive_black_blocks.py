class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # count_recolor_white: int = 0
        # # First Wind
        # for i in range(k):
        #     if blocks[i] == "W":
        #         count_recolor_white += 1
        #
        # min_recolor_white: int = count_recolor_white
        #
        # # Sliding
        # left: int = 0
        # for right in range(k, len(blocks)):
        #     # l=r-k
        #     # expand right
        #     if blocks[right] == "W":
        #         count_recolor_white += 1
        #
        #     # shirnk left
        #     if blocks[left] == "W":
        #         count_recolor_white -= 1
        #     left += 1
        #
        #     min_recolor_white = min(min_recolor_white, count_recolor_white)
        #
        # return min_recolor_white

        left: int = 0
        count_whites: int = 0
        min_recolor: int = float('inf')
        right: int = 0

        while right < len(blocks):
            # expand
            if blocks[right] == "W":
                count_whites += 1

            # wind size
            if right - left + 1 == k:
                min_recolor = min(min_recolor, count_whites)

                #shirnk
                if blocks[left] == "W":
                    count_whites -= 1

                left += 1
            # move r
            right += 1
        return min_recolor

if __name__ == "__main__":
    so: Solution = Solution()
    blocks: str = "WBWBBBW"
    k: int = 2
    print(so.minimumRecolors(blocks, k))