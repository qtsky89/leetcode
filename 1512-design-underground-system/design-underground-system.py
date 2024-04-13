class UndergroundSystem:
    '''
    session = {
        'id' : (stationName, startTime)
    }

    hash_table = {
        (startStation, endStation) : [t1, t2, t3]
    }

    '''

    def __init__(self):
        self.session = {}
        self.times = {}
        

    def checkIn(self, id: int, start_station: str, start_time: int) -> None:
        self.session[id] = (start_station, start_time)
        
    def checkOut(self, id: int, end_station: str, end_time: int) -> None:
        start_station, start_time = self.session[id]

        if (start_station, end_station) in self.times:
            self.times[(start_station, end_station)].append(end_time-start_time)
        else:
            self.times[(start_station, end_station)]  = [end_time-start_time]

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        return sum(self.times[(start_station, end_station)])/len(self.times[(start_station, end_station)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)