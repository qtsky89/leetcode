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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host_name = startUrl[7:].split('/')[0]

        q = deque([startUrl])

        visited = set()
        while q:
            item = q.popleft()
            if host_name == item[7:].split('/')[0]:
                visited.add(item)
            else:
                continue

            next_items = htmlParser.getUrls(item)

            for next_item in next_items:
                if next_item not in visited:
                    q.append(next_item)
        return visited
            