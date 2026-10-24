class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]

        def day_of_year(date):
            month = int(date[:2])
            day = int(date[3:])

            total = day
            for i in range(month - 1):
                total += days[i]

            return total

        a1 = day_of_year(arriveAlice)
        a2 = day_of_year(leaveAlice)
        b1 = day_of_year(arriveBob)
        b2 = day_of_year(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, end - start + 1)