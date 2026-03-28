class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        numBoats = 0
        i, j = 0, len(people)-1
        while i <= j:
            print(f"people: {people[i]}")
            print(f"people: {people[j]}")
            
            if i == j:
                print(f"1 adding {people[i]}")
                numBoats+=1
                break
            elif (people[i] + people[j]) <= limit:
                print(f"adding {people[i]}  and  {people[j]}")
                j-=1
                i+=1
                numBoats+=1
            else:
                print(f"adding {people[j]}")
                j-=1
                numBoats+=1
        return numBoats
