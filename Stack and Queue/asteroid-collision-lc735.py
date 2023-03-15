# page 25
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            remaining = True

            while stack and stack[-1] > 0 and asteroid < 0:
                if -asteroid == stack[-1]:  # mutual destruction
                    stack.pop()
                    remaining = False
                    break

                elif -asteroid > stack[-1]:  # negative asteroid alive
                    stack.pop()

                else:  # negative asteroid destroyed
                    remaining = False
                    break

            if remaining:
                stack.append(asteroid)

        return stack
