class Solution:
    def generateCount(self, string: str, lst: list):
        count = list(map(lambda x: string in x, lst))
        return sum(count)

    def prefixCount(self, N, Q, mainstring, substring):
        counter = []
        nwlst = [i[0] for i in mainstring]
        for singleString in substring:
            counter.append(self.generateCount(*singleString, nwlst))
        return counter


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        li = []
        for i in range(N):
            li.append(input().split())
        Q = int(input())
        query = []
        for i in range(Q):
            query.append(input().split())

        ob = Solution()
        ans = ob.prefixCount(N, Q, li, query)
        for i in range(Q):
            print(ans[i])

# N = 5, Q = 5
# li[] = {'abracadabra', 'geeksforgeeks',
#       'abracadabra', 'geeks', 'geeksthrill'}
# query[] = {'abr', 'geeks', 'geeksforgeeks',
#          'ge', 'gar'}

# Output: 2 3 1 3 0

# Explaination:
# Query 1: The string 'abr' is prefix of
# two 'abracadabra'.
# Query 2: The string 'geeks' is prefix of three
# strings 'geeksforgeeks', 'geeks' and 'geeksthrill'.
# Query 3: The string 'geeksforgeeks' is prefix
# of itself present in li.
# Query 4: The string 'ge' also is prefix of three
# strings 'geeksforgeeeks', 'geeks', 'geeksthrill'.
# Query 5: The string 'gar' is not a prefix of any
# string in li.
