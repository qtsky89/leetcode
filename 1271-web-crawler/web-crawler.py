# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = startUrl.split('/')[2]

        q = deque([startUrl])
        visited = set()
        ret = []

        while q:
            url = q.popleft()

            if url not in visited:
                visited.add(url)
                ret.append(url)

            # check next url
            for u in htmlParser.getUrls(url):
                if u.split('/')[2] == host and u not in visited:
                    q.append(u)
        
        return ret

