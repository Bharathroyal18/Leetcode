class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        original=celsius
        ans=[]
        Kelvin = original + 273.15
        Fahrenheit = original * 1.80 + 32.00
        ans.append(Kelvin)
        ans.append(Fahrenheit)
        return ans
        