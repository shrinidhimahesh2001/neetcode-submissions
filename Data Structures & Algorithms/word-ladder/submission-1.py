class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList):
            return 0
        queue = collections.deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        ladder=1
        while queue:
            q_size = len(queue)
            for _ in range(q_size):
                word = queue.popleft()
                for newWord in wordList:
                    if newWord in visited:
                        continue
                    diff = 0
                    for i in range(len(word)):
                        if word[i] != newWord[i]:
                            diff += 1
                        if diff >= 2:
                            break
                    if diff == 1:
                        if newWord == endWord:
                            return ladder + 1
                        visited.add(newWord)
                        queue.append(newWord)
            ladder+=1
        return 0