class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hmap = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:    'X',
            40:    'XL',
            50:    'L',
            90:    'XC',
            100:    'C',
            400:    'CD',
            500:    'D',
            900:    'CM',
            1000:    'M'
        }

        ans=""
        num_str=str(num)
        while num>0:
            i=0
            for key, value in hmap.items():
                if key > num:
                    break
                i=key
            ans=ans+hmap[i]
            num-=i
        
        return ans

sol=Solution()
print(sol.intToRoman(3749))