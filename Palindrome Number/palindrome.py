from typing import Any

class PalindromeNumber:
    def SimplePalidrome(self, num: int) -> Any:
        '''
        Check if the provided number is a Palindrome

        Args:
            num (int): A integer to check
        
        Returns (bool): A boolean answer
        '''
        num = str(num)
        if num == num[::-1]:
            return True
        return False

palindrome = PalindromeNumber()
print(palindrome.SimplePalidrome(1001))