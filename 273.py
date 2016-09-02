class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        base=["","Hundred","Thousand","Million","Billion"]
        one = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]   #nx1
        ten = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]    #10-19
        ten_a = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]   # nx10
        result=[]
        
        if num==0:
            return "Zero"
        
        billion=num/1000000000
        if billion!=0:
            result.append(self.numberToWords(billion))
            result.append("Billion")
            num=num-billion*1000000000
        
        million=num/1000000
        if million!=0:
            result.append(self.numberToWords(million))
            result.append("Million")
            num=num-million*1000000
        
        thousand=num/1000
        if thousand!=0:
            result.append(self.numberToWords(thousand))
            result.append("Thousand")
            num=num-thousand*1000
        
        hundred=num/100
        if hundred!=0:
            result.append(self.numberToWords(hundred))
            result.append("Hundred")
            num=num-hundred*100
 
        if num>0 and num<10:
            result.append(one[num])
        
        if num>=10 and num<20:
            result.append(ten[num-10])
        
        if num>=20:
            tens=num/10
            result.append(ten_a[tens])
            num=num-tens*10
            if num!=0:
                result.append(one[num])
        
        return " ".join(result)
            
#東大試験
