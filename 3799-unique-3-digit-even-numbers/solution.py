class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        r=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and i != k:  
                        n = digits[i]*100 + digits[j]*10 + digits[k]
                        if n % 2 == 0 and n >= 100:  
                            r.add(n)
        return len(r)
