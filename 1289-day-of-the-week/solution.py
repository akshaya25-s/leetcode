class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d=datetime.date(year,month,day)
        return d.strftime('%A')
