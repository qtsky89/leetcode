class UndergroundSystem:

    def __init__(self):
        # key = id, value = (station, t)
        # {45: ("Leyton", 3)}
        self._session = {}

        # key = (stationName, stationName), value = [diff1, diff2 ...]
        # {("Paradice", "London"): [40, 35, 20...]}
        self._times = {}

    def checkIn(self, id: int, start_station: str, start_time: int) -> None:
        self._session[id] = (start_station, start_time)

    def checkOut(self, id: int, end_station: str, end_time: int) -> None:
        start_station, start_time = self._session[id]
        del self._session[id]

        if (start_station, end_station) in self._times:
            self._times[(start_station, end_station)].append(end_time - start_time)
        else:
            self._times[(start_station, end_station)] = [end_time - start_time]

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        return sum(self._times[(start_station, end_station)]) / len(self._times[(start_station, end_station)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)