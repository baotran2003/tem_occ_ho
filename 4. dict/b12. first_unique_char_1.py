"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1
"""

def first_unique_char(s: str) -> int:
    frequency_map: dict[str, int] = {}

    for char in s:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    print(frequency_map)

    for index, char in enumerate (s):
        if frequency_map[char] == 1:
            return index

    return -1


if __name__ == "__main__":
    s1 = "leetcode"
    print(first_unique_char(s1))