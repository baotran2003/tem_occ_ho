# arr[0, 1, 2, 3 ,5] k =5
# [[0, 5], [2, 3]]

if __name__ == "__main__":
     arr: list[int] = [0, 1, 2, 3 ,5]
     k: int = 5
     n = len(arr)

     result_arr: list[list[int]] = []

     for j in range (n):
         complement: int = k - arr[j]
         for i in range(j):
             if arr[i] == complement:
                 result_arr.append([i, j])

     print(result_arr)