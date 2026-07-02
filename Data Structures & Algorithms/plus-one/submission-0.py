class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry > 0:
            if i >= 0:
                carry += digits[i]
                if carry > 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] = carry
                    break
            else:
                digits = [1] + digits
                break
            i -= 1
        return digits