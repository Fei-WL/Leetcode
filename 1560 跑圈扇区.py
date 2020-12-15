class Solution:
    def mostVisited(self, n: int, rounds):
        new_rounds = [t - 1 for t in rounds]
        people = new_rounds[0]
        index = 0
        while True:
            if people != new_rounds[index]:
                new_rounds.insert(index, people)

            if index + 1 < len(new_rounds):
                index += 1
            else:
                break
            people = (people + 1) % n

        rounds = [t + 1 for t in new_rounds]

        end = len(rounds) % n if len(rounds) % n != 0 else n

        result = sorted(rounds[:end])

        return result
s = Solution()
print(s.mostVisited(3, [3,2,1,2,1,3,2,1,2,1,3,2,3,1]))