class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        bills => 5 5 5 10 20

        total_bill
        {
            5 : 1
        }

        bills => 5, 5, 10, 10, 20
                               ^
        total_bill
        {
            10: 2
        }


        whenver I have to give them a change, give biggest one should work.

        5 => very important
        10 => less important
        ...
        '''

        total_bill = defaultdict(int)

        for bill in bills:
            if bill == 5:
                total_bill[bill] += 1
            elif bill == 10:
                total_bill[bill] += 1

                if total_bill[5] == 0:
                    return False
                total_bill[5] -= 1

            elif bill == 20:
                total_bill[bill] += 1

                # we have 10, 5
                if total_bill[10] > 0 and total_bill[5] > 0:
                    total_bill[10] -= 1
                    total_bill[5] -= 1
                elif total_bill[5] > 2:
                    total_bill[5] -= 3
                else:
                    return False
        return True

