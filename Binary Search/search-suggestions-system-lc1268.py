# page 35

import bisect
from typing import List


class Solution2Pointer:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, h = 0, len(products) - 1
        result = []

        for i, char in enumerate(searchWord):

            '''
            we want to pass over l's and h's corresponding to which either the length is too small to accommodate
            the present index or which do not have char at their ith index
            What might seem slightly confusing at first is how the same condition is being used for both l and h. 
            However, the reason is very simple, since they have been initalised at the poles, every element in the range
            must satisfy the same conditions. So, if l and h meet these conditions, we can say that all elements in between do so too.
            '''

            while l <= h and (len(products[l]) <= i or products[l][i] != char):
                l += 1

            while l <= h and (len(products[h]) <= i or products[h][i] != char):
                h -= 1

            result.append(products[l:min(h + 1, l + 3)])

        return result


# using bisect (binary search)
class SolutionBisect:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result, prefix, i = [], '', 0

        for char in searchWord:
            prefix += char

            # find the left-most insertion point in the products arrat for prefix,
            # such that it is greater than or equal to i, i.e., the previous lower bound

            i = bisect.bisect_left(products, prefix, i)

            # notice how we didn't find h here and straight-away checked the next 3 items. That's cool too
            result.append([product for product in products[i:i + 3] if product.startswith(prefix)])

        return result
