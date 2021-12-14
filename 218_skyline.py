"""
218. The Skyline Problem
Hard

3447

183

Add to List

Share
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]



Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
"""

def skyline(buildings):
    skyline = []
    height_q = []
    end_q = []
    for b in buildings:
        while end_q and end_q[0][1]<b[0]:
            end_b = pop_end_q(end_q)
            pop_height_q(height_q, end_b)
            if not height_q:
                skyline.append((end_b[1], 0))
            elif height_q[0][2]<end_b[2]:
                skyline.append((end_b[1], end_q[0][2]))

        while end_q and end_q[0][1]==b[0]:
            end_b = pop_end_q(end_q)
            pop_height_q(height_q, end_b)
            if not height_q or height_q[0][2]!=b[2]:
                skyline.append((b[1], b[2]))

        push_end_q(end_q, b)
        if not height_q or height_q[0][2]<b[2]:
            skyline.append((b[0], b[2]))
        push_height_q(height_q, b)
    while end_q:
        end_b = pop_end_q(end_q)
        pop_height_q(height_q, end_b)
        if not height_q:
            skyline.append((end_b[1], 0))
        elif height_q[0][2] < end_b[2]:
            skyline.append((end_b[1], end_q[0][2]))
    return skyline


def push_end_q(q, e):
    i=0
    while i<len(q):
        if e[1]<q[i][1]:
            break
        i+=1
    if i==len(q):
        q.append(e)
    else:
        q.insert(i, e)

def pop_end_q(q):
    return q.pop(0)


def push_height_q(q, e):
    i=0
    while i<len(q):
        if e[2]>q[i][2]:
            break
        i+=1
    if i==len(q):
        q.append(e)
    else:
        q.insert(i, e)

def pop_height_q(q, e):
    q.remove(e)

print(skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))