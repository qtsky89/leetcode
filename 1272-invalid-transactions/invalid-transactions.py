class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions.sort(key=lambda x:int(x.split(',')[1])) #sort by time

        d = deque()

        invalids = set()
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(',')

            if int(amount) > 1000:
                invalids.add(i)
            
            for j in range(len(d)-1, -1, -1):
                d_name, d_time, d_amount, d_city = transactions[d[j]].split(',')

                time_diff = int(time) - int(d_time)

                if time_diff > 60:
                    break

                if d_name == name and d_city != city:
                    invalids.add(i)
                    invalids.add(j)
            d.append(i)
        
        return [transactions[invalid] for invalid in invalids]
            