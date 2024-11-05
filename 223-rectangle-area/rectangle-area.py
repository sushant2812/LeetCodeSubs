class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        cx1 = max(ax1, bx1) #MAX OF LOWER
        cx2 = min(ax2, bx2) #MIN OF UPPER
        cy1 = max(ay1, by1) #MAX OF LOWER
        cy2 = min(ay2, by2) #MIN OF UPPER
        area =max(0,cx2-cx1)*max(0,cy2-cy1)
        area_first = abs(ax1-ax2)*abs(ay1-ay2)
        area_second = abs(bx1-bx2)*abs(by1-by2)
        return area_first+area_second-area