from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
      '''
      1.
        a  -  b 
         |   |
           c

        a / b = 2.0
        b / c = 3.0

      2.
      a  /  b = 0.2
      b  /  c = 2.5
      b  /  d = 5.0
      '''

      '''
      first make graph using map
      key (tuple) value(float)
      a = [(b, 2.0)]
      b = [(a, 1/2), (c, 3.0)]
      c = [(b, 1/3)]
      '''

      graph = {}

      for i in range(len(equations)):
        key, value = equations[i]
        
        if key not in graph:
          graph[key] = []
        graph[key].append((value, values[i]))
        
        if value not in graph:
          graph[value] = []
        graph[value].append((key, 1/values[i]))

      ret = []
      '''
      second. find the path, if I coulnd't find the path then -1.0
      '''
      
      for i in range(len(queries)):
        start, end = queries[i]
        ret.append(self._calculate(start, end, graph))
      
      return ret

    def _calculate(self, start: float, end: float, graph: dict) -> int:
      q = deque([[start, 1.0, set()]])
      
      while q:
        item, cur_cal, visited = q.popleft()

        if item not in graph:
          continue
        elif item == end:
          return cur_cal

        visited.add(item)
        
        for i in range(len(graph[item])):
          next_item, next_cal =  graph[item][i]

          if next_item not in visited:
            q.append([next_item, cur_cal * next_cal, set(visited)])
      
      return -1.0
          

      





      
      
        
      

      

