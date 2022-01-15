class Solution:

    def findMaxConsecutivesOnes(self, nums):
        '''Max consecutives ones in a binary array.

        nums: <list> binarry array.
        return: <int> max consecutives ones.
        '''

        # initialize count
        count = 0

        # initialize result
        result = 0

        for i in range(len(nums)):
            
            # reset count when 0 is found
            if (nums[i] == 0):
                count = 0

            # If 1 is found, increment count
            # and update result if count
            # becomes more.
            
            else:
                count += 1
                result = max(result, count)

        return result

    def isEven(self, num):
        '''True if int is even.

        num: <int> number to check if is even.
        return: <bool> True if is even.
        '''
        return not (num % 2)

    def countDigits(self, num):
        '''Count number of digits of a int.

        num: <int> number to count digits.
        return: <int> total of digts.
        '''

        # initialize digits
        digits=1

        while (num // 10) >0:
            digits+=1
            num = num // 10

        return digits

        return digits
    def totalNumbersWithEvenNumOfDigits(self, nums):
        '''Count total numbers with even num of digits.

        num: <list> list of ints to be check.
        return: <int> total num of numbers with even num of digits.
        '''

        # initialize count
        count = 0

        for i in range(len(nums)):
            
            # reset count when 0 is found
            if self.isEven(self.countDigits(nums[i])):
                count += 1

        return count


if __name__ == '__main__':
    nums = [22345678,33,1,4]
    print(Solution().totalNumbersWithEvenNumOfDigits(nums))

