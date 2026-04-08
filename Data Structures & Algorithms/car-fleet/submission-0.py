class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = [[p,q] for p, q in zip(position, speed)]
        pos_speed = sorted(pos_speed, reverse=True)

        for p, s in pos_speed:
            time = (target-p)/s
            stack.append(time)
            print(stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


         

        