'''
[73,74,75,71,69,72,76,73]
                i

(74,1)
initialize with temps[0]

76

while q and temp > q[0][0]
    ans[o[q[0][1]]] = i - q[0][1]
    q.popleft()

q.append(temp)

q = [
    75,2
]

a = [1, 1, 0, 2, 1, 0, 0, 0]


initialized to [0] * len(temperatures)
iterate from 1 to len(temps)
    

a = [

]

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        q.append(tuple([temperatures[0], 0]))
        o = [0] * len(temperatures)

        for i in range(1,len(temperatures)):
            temp = temperatures[i]
            while q and temp > q[-1][0]:
                o[q[-1][1]] = i - q[-1][1]
                q.pop()

            q.append(tuple([temp,i]))
        
        return o


'''
[73,74,75,71,69,72,76,73]
                        i 

stack = [
    3
    2
]

ans = [
    1, 1
]

Official Solution
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [1, 2, ]
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        
        return answer
