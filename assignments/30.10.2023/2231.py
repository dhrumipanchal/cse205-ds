class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))

        
        even_digits = []
        odd_digits = []

        
        for digit in digits:
            digit = int(digit)  
            if digit % 2 == 0:
                even_digits.append(digit)
            else:
                odd_digits.append(digit)

        
        even_digits.sort(reverse=True)
        odd_digits.sort(reverse=True)

       
        even_index = 0
        odd_index = 0
        for i in range(len(digits)):
            if int(digits[i]) % 2 == 0:  
                digits[i] = str(even_digits[even_index])
                even_index += 1
            else:
                digits[i] = str(odd_digits[odd_index])
                odd_index += 1

        
        largest_num = int(''.join(digits))

        return largest_num