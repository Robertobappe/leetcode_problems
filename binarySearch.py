class Solution:
    def search(self, nums: list[int], target: int) -> int:
        baixo = 0
        alto = len(nums) - 1

        while baixo <= alto:
            meio = (baixo + alto)//2
            chute = nums[meio]

            if chute == target:
                return meio
            if chute < target:
                baixo = meio + 1
            else:
                alto = meio - 1
        return -1    


        