### Sources

practice
* https://leetcode.com/
* https://www.hackerrank.com/
* https://www.geeksforgeeks.org
* https://www.interviewbit.com/
* https://codedrills.io
* https://www.careercup.com/page?pid=google-interview-questions

mock
* https://www.pramp.com

### Problems
All the subsets of an array

All permutations of a list of chars

A sorted list of the square of each element in a sorted list of integers

Quicksort with duplicates

Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

Binary insertion

Given an encoded string, return its decoded string.

Implement a SnapshotArray that supports pre-defined interfaces (note: see link for more details). 

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.) We may rotate the i-th domino, so that A[i] and B[i] swap values. Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same. If it cannot be done, return -1.

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times. You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Given a list of query words, return the number of words that are stretchy." Note: see link for more details. 

Your car starts at position 0 and speed +1 on an infinite number line. (Your car can go into negative positions.) Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse)...Now for some target position, say the length of the shortest sequence of instructions to get there." 

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W. If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). Find all strobogrammatic numbers that are of length = n.

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root. The length of path between two nodes is represented by the number of edges between them.

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive). The binary search tree is guaranteed to have unique values.

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

Add Two Numbers As Lists.

Given 2 non negative integers m and n, find gcd(m, n).

Given two two integer arrays. Find the longest common subsequence. eg: a =[1 5 2 6 3 7], b = [5 6 7 1 2 3]. return [1 2 3] or [5 6 7]

Given various subsequences of an array, print the overall array:
Example: [1, 3, 5], [1, 3, 9], [9, 5]
Array : [1, 3, 9, 5]

Given a random list of appointments (Start Date , End Date). Find all the appointments that are colliding.

Given an array {a0, a1, a2, ... an, b0, b1, b2 ... bn}, Rearrange this array into {a0, b0, a1, b1, a2, b2, ... an, bn} inplace, O (1) space

If xi<xj,yi<yj, we say (xj,yj)dominates(xi,yi). Given a set of number pairs (xi,yi), how many indomitable pairs are there?

The two arrays [1,2,3,4,5], [2,3,4,5,6] find the first subfix and the second prefix the same longest case, such as the example is [2, 3,4,5] Length of 4. Followup: how to do two-dimensional array, how to optimize.

Given Two string, ask whether they can become the same after just one swap of two chars in one string. For example: "abcd", "bacd" Yes, you can swap ab in the first string to make it the same as the second string "abcd", "adbc" can not. Follow-up, given Two string, ask whether they can become the same after N swaps of two chars in one string g, assuming that the swap does not overlap.(str [0] <-> str [2] str [2] and str [0] will not be swapped with other locations)

Given a dictionary, output the longest List <String>. The result of a String is the previous String add a character at any position. Example: {i, in, ing, sing, sting, string}

Hint: graph depth first traverse
	
Find a “local minimum” in a binary tree: a local min is a node whose value is smaller than that of any other nodes that are connected to it.
	
Given an array of length n + 1, containing elements 1 through n and a space, Requires the use of a given swap (index i, index j) function to sort the array,
You can only swap the gap and a number, in the end, put the gap at the end. 
	
Given a list L of video names and their watch rates, write a function that will return the videos with the top 10 watch rates. Video names may appear more than once. Example:
```
L = [(‘abc’, 10), (‘def’, 15), (‘ghi’, 10), (‘abc’, 12), …, (‘xyz’, 100)]
```
The function should return [‘xyz’, ‘abc’, …, ‘def’, ‘ghi’]

	
### Sort List
Sort a linked list in O(n log n) time using constant space complexity.

Example :
```
Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5
```
### Container With Most Water
Given n non-negative integers a1, a2, ..., an,

where each represents a point at coordinate (i, ai).

'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).

Note: You may not slant the container.

Example :
```
Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6
```

### Array 3 Pointers
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
```
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.

Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
```
Example :
```
Input : 
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5 
         With 10 from A, 15 from B and 10 from C.
```
### Justified Text
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ' ' when necessary so that each line has exactly L characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:
```
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```
Note: Each word is guaranteed not to exceed L in length. 

### Multiply Strings
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.

For example, 
```
given strings "999", "999", your answer should be “998001”.
```
### Allocate Books
Given an array of integers A of size N and an integer B.

College library has N bags,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.
```
For Example

Input 1:
    A = [12, 34, 67, 90]
    B = 2
Output 1:
    113
Explanation 1:
    There are 2 number of students. Books can be distributed in following fashion : 
        1) [12] and [34, 67, 90]
        Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
        2) [12, 34] and [67, 90]
        Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
        3) [12, 34, 67] and [90]
        Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

        Of the 3 cases, Option 3 has the minimum pages = 113.

Input 2:
    A = [5, 17, 100, 11]
    B = 4
Output 2:
    100
```    
### Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.
```
Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
```

### Median of Array

There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).
```
Sample Input
A : [1 4 5]
B : [2 3]
Sample Output
3
NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. 
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
```
```
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def binSearch(self, A, k):
        l=0
        r=len(A)-1
        while l<r:
            m = (l+r)//2
            if A[m]==k:
                l=m
                r=m
                break
            if A[m]<k:
                l = m+1
            else:
                r = m-1
        return r
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        i = (len(A) + len(B))//2
        if l%2==0:
            m1 = self._findMedianSortedArrays(A, B, i)
            m2 = self._findMedianSortedArrays(A, B, i-1)
            return (m1+m2)//2
        else:
            return self._findMedianSortedArrays(A, B, i)

    def _findMedianSortedArrays(self, A, B, i=-1):

        if not A:
            return B[i]
        if not B:
            return A[i]
        ma = len(A)//2
        mb = self.binSearch(B, A[ma])
        if ma+mb+1==i:
            return A[ma]
        elif ma+mb+1>i:
            return self._findMedianSortedArrays(A[0:ma], B[0:mb+1], i)
        else:
            return self._findMedianSortedArrays(A[ma+1: len(A)], B[mb+1: len(B)], i-ma-mb-2)
```

### Next Smallest Palindrome!

Given a numeric string A representing a large number you need to find the next smallest palindrome greater than this number.

Problem Constraints
1 <= |A| <= 100

A doesn't start with zeroes and always contain digits from 0-9.

Input Format
First and only argument is an string A.

Output Format
Return a numeric string denoting the next smallest palindrome greater than A.
```
Example Input
Input 1:

 A = "23545"
Input 2:

 A = "999"


Example Output
Output 1:

 "23632"
Output 2:

 "1001"
```

```
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        odd = len(A)%2==1
        m = len(A)//2
        if odd:
          first = A[0:m]
          second = A[m+1:len(A)]
        else:
          first = A[0:m-1]
          second = A[m+1:len(A)]
          if A[m]!=A[m-1]:
              return first + max(A[m-1], A[m])+ max(A[m-1], A[m]) + first[::-1]
        if first and second:
          first_num = int(first)
          second_num = int(second[::-1])
          if int(first[::-1]) > int(second):
            if odd:
                return first+A[m]+first[::-1]
            else:
                return first+A[m-1]+A[m]+first[::-1]

        if A[m]!='9':
            if odd:
                return first + str(int(A[m])+1) + first[::-1]    
            else:
                return first + str(int(A[m])+1) + str(int(A[m])+1) + first[::-1]    
        found = False
        for i in range(len(first)-1, -1, -1):
            if i<'9':
                first[i]=str(int(i)+1)
                found=True
        if found:
          if odd:
            return first + '0' + first[::-1]    
          else:
            return first + '00' + first[::-1]          
        return '1'+'0'*(len(A)-1)+'1'
```
### Rotate Digits
We can rotate digits by 180 degrees to form new digits. 
When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 
0, 1, 9, 8, 6 respectively. 
When 2, 3, 4, 5, and 7 are rotated 180 degrees, 
they become invalid. A confusing number is a number 
that when rotated 180 degrees becomes a different number 
with each digit valid.(Note that the rotated number 
can be greater than the original number.) 
Given a positive integer N, return the number 
of confusing numbers between 1 and N inclusive.

### Shortest Transformation
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that: 
* Only one letter can be changed at a time and, 
* Each transformed word must exist in the word list.

### Longest Path
Given a matrix of N rows and M columns. From m[i][j],
 we can move to m[i+1][j], if m[i+1][j] > m[i][j], or 
 can move to m[i][j+1] if m[i][j+1] > m[i][j]. 
 The task is print longest path length if we start from (0, 0).

### Robot Cleaner
Given a robot cleaner in a room modeled as a grid. 
Each cell in the grid can be empty or blocked. 
The robot cleaner with 4 given APIs can move forward,
 turn left or turn right. Each turn it made is 90 degrees. 
 When it tries to move into a blocked cell, its bumper 
 sensor detects the obstacle and it stays on the current cell. 
 Design an algorithm to clean the entire room using only the 4 given APIs shown below." (Solution)


### Three Sum
Given an array of numbers and a target integer, find three elements from the array that sums up to target. Return the value of these three elements (0-based). (Note: This is different from Two Sum where you had to return the indices)
The triplet of the values returned should be sorted. If multiple such values exist, break ties by returning the triplet with the least first value. If there are still multiple such triplets with same first value, return the triplet with the least second value. If there are still multiple such triplets with same first and second values, return the triplet with the least third value. If there is no triplet that sums to target, return an empty array.

```
Sample 0
Input
nums: [1, 2, 3, 3, 4, 1, 1]
target: 6
Output
[1, 2, 3]
Sample 1
Input
num: [1, 2, 3, 3, 4, 1, 1]
target: 100
Output
[]
```
### All Permutations
You have to find all the permutations of integers from 1 to n without using the permutation related library functions in your code.
```
Sample 0
Input
n: 2
Output
[ [ 1 , 2 ] , [ 2 , 1 ] ]
Sample 1
Input
n: 3
Output
[ [ 1 , 2 , 3 ] , [ 1 , 3 , 2 ] , [ 2 , 1 , 3 ] , [ 2 , 3 , 1 ] , [ 3 , 2 , 1 ] , [ 3 , 1 , 2 ] ]
```
### All Unique Permutations

Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.

```
Example Input
Input 1: 
A = [1, 1, 2]
Input 2: 
A = [1, 2]


Example Output
Output 1: 
[ [1, 1, 2]
  [1, 2, 1]
  [2, 1, 1] ]
Output 2: 
[ [1, 2]
  [2, 1] ]
```
### NQueens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,

```
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```
### Palindrome Partitioning
Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
```
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
Ordering the results in the answer :

Entry i will come before Entry j if :

len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,

   ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
```   
### Smallest Supersequences 
Given an array of array of integers arrs and a random permutation p of first n integers {1,2,...,n}. Find if the given permutation p is the smallest supersequence of arrs.
A sequence is said to be a supersequence if it contains all arrays in arrs as subsequences.
A supersequence A is said to be smaller than another supersequence B, if A has less length than B. If both have same length, lexicographically smaller sequence is smaller.
```
Sample 0
Input
arrs:[[1,3],[2,3]]
p:[2,1,3]
Output
false
Explanation
[1,2,3] is the smallest supersequence in this case.
Sample 1
Input
arrs:[[1,2],[3,2]]
p:[1,3,2]
Output
true
```
### Largest Rectangle in Histogram

Given an array of integers A .

A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.

Find the area of the largest rectangle formed by the histogram.

```

Example Input
Input 1:

 A = [2, 1, 5, 6, 2, 3]
Input 2:

 A = [2]


Example Output
Output 1:

 10
Output 2:

 2


Example Explanation
Explanation 1:

The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
Explanation 2:

Largest rectangle has area 2.
```

### Minimum Jumps
Given an array of non negative numbers, each element in the array reprents maximum jump length from that position. Initially you are at first position (0th index) of the array and you want to go to the last position. Find minimum number of jumps you need to make to reach the last position.
Note that there is always a way to reach the last position.
```
Sample 0
Input
[2,1,3,5,1]
Output
2
Explanation
We can jump 2 steps from index 0 to 2 and then 2 steps from index 2 to 4. So, minimum number of jumps to reach to the last position is 2.
Sample 1
Input
[1,4,2,6,3]
Output
2
```

### Max Profit
Given N jobs, where i-th job is scheduled to be done from startTime[i] to endTime[i], with a profit of profit[i].

You need to output the maximum profit that can be made by selecting jobs such that, no two jobs are overlapping in the time range.
Note:
If you finish a job at time T, you can start another job at time T.
```
Sample 0
Input
startTime: [1, 3, 7, 2]
endTime: [2, 4, 19, 17]
profit: [5, 2, 10, 20]
Output
25
```
### Grid Unique Paths

A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :
```
Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
```


### Best Cover of Array
Given an array A consisting of only 0s and 1s. You can perform the following operation on the array:
choose any contiguous subarray of length at most K and change all the elements of the subarray to 1.
You goal is to find the minimum number of 0s remaining in the array after performing the operation at most Q times.
```
Sample 0
Input
A : [0, 0, 0, 1, 1, 1]
K : 2
Q : 2
Output
0

Explanation
We can perform the operation once on the subarray [1, 2],
the array becomes, [1, 1, 0, 1, 1].
Then we perform the operation on the subarray [3, 3],
The array becomes, [1, 1, 1, 1, 1]
Sample 1
Input
A : [1, 0, 0, 0, 1, 1]
K : 2
Q : 1
Output
1
```
### Overlapping Intervals 
Given a collection of intervals, find out how many intervals have to be removed to ensure that no interval is overlapping over another. An interval is not considered overlapping if it starts where the previous one ends.
```
For e.g., [0, 1] and [1, 2] are not overlapping intervals while [0, 2] and [1, 2] are. Here’s an example:

Input: [0, 3], [9, 12], [3, 8], [8, 10]
Answer: 1
In this case, if [8, 10] is removed, there will be no overlapping between the others. Here’s another example:

Input: [0,5], [1, 2], [3, 5]
Answer: 1
In this case, if [0, 5] is removed, there will be no overlapping between the others.
```

### Shortest Palindrome
Given a string s.

You need to convert the string into a palindrome by appending any characters in front of the given string s.

Return the single string res which is the shortest palindrome after this transformation.

Sample 0
```
Input
s: eedoc

Output
res: codeedoc
```
Sample 1
```
Input
s: aabaaa

Output
res: aaabaaa
```
### Minimizing Largest Sum
You are given an array nums (containing non-negative integers) and an integer m. You can split the original array nums into m non-empty continuous subarrays.

There can be size of nums - 1Cm - 1 total ways to split the array nums into m subarrays.

Consider a function f(way) which accepts a way to split an array nums hence m subarrays will be created, f(way) returns max(sumsubarray_1, sumsubarray_2, ...., sumsubarray_m).

You have to find min(f(way1), f(way2),....., f(waytotal_ways)).

Note: Sum of all elements of array nums is guaranteed to fit in a 32-bit integer.

Sample 0
```
Input
nums: [5, 6]
m: 1

Output
11

Explanation
As the array can be splitted in only 1 array then it will be the original array nums only contaning sum 11.
```
Sample 1
```
Input
nums: [7, 9, 9]
m: 2

Output
16

Explanation
The array nums can be splitted in 2 subarrays in following ways:

[7], [9,9]
[7, 9], [9]

The first split have sums of subarrays (7, 18), so max(7, 18) = 18.
The second split have sums of subarrays (16, 9), so max(16, 9) = 16
Our final answer is min(18, 16) = 16.
```

### Coins in the Path
There is a stone-path in Mario land. Mario will always start from the first stone and he wants to reach last stone with minimum cost.
Each stone has a cost to jump on it given in the array. Mario has jump ability represented by steps i.e he can jump to any stone in range [ i + 1, i + steps ] when standing on stone at i'th-index.

Given an integer array array of length N and an integer steps where,

N = Number of stones
array[i] = Cost to jump on ith-stone
steps = Mario's jump ability

Note: if array[i] == -1 then Mario can't jump on that stone.

Return the path of indexes (0-based indexing) with the smallest cost. If there are multiple paths with the smallest cost, then return lexicographically smallest one.
If no possible path is found then return an empty array.
```
Sample 0
Input
array: [1, 3, 2, -1, 1]
steps: 2

Output
[0, 2, 4]

Explanation
There is only one minimum cost path possible starting from index-0 is 0, 2, 4 with cost 1 + 2 + 1 = 4

Sample 1
Input
array: [2, 3, 5, 3, 1]
steps: 3

Output
[0, 1, 4]

Explanation
There are two paths possible 0, 1, 4 and 0, 3, 4 with same cost 2 + 3 + 1 = 6.So lexicographically smaller path is our answer i.e 0, 1, 4.
```

### Longest D-Subsequence
You are given an array arr and integer d. Find longest non-decreasing subsequence of arr such that the difference between consecutive elements of the sequence is less than d.
Value of d is small.
Note - A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.
```
Sample 0
Input
arr: [1]
d: 1

Output
1

Explanation
Array only has a single sequence satisfying this property.

Sample 1
Input
arr: [1, 3, 2, 4, 5]
d: 2

Output
3

Explanation
Array only has a sequence [3, 4, 5] satisfying this property.

```
### The Skyline Problem
Skyline: A skyline is the outline or shape created by a city's overall structure, which is formed when the sky meets buildings or the land.

You are given N rectangular buildings in a 2-dimensional city, your task is to compute the skyline of these buildings, eliminating hidden lines, when viewed from a distance.

All buildings share common bottom and every building is represented by a triplet (left, right, height) where,
‘left’: is x coordinate of left side (or wall).
‘right’: is x coordinate of right side
‘height’: is height of the building.

A skyline is a collection of rectangular strips. As shown in the figure B, rectangular strip is represented as a pair (left, ht) (Red Points) where left is x coordinate of left side of strip and ht is height of strip.

You should return all such points in increasing order of left(x-coordinate) along with the last point, which is termination point indicating end of skyline.
The height of termination point is always zero.

Note:
There should not be any consecutive points with equal height in the output skyline.
Eg: If the output skyline is [[1,3], [2,5], [3,5], [4,0]], it must be resolved by taking only the leftmost point and eliminating the rest with same height.
So, the vaild output will be [[1,3], [2,5], [4,0]].

FIGURE A Figure A FIGURE B Figure B
Note:

There will be atleast 1 building present.
Height of each building will be atleast 1.
Input buildings will be sorted in increasing order of left coordinate.
```
Sample 0
Input
buildings: [[1,3,4], [2,5,8], [4,8,2], [6,7,5]]

Output
[[1,4], [2,8], [5,2], [6,5], [7,2], [8,0]]
Note: This Example is of the skyline shown in figure above.

Sample 1
Input
buildings: [[1,3,4]]

Output
[[1,4], [3,0]]
```
###  Expression Calculator
Evaluate the given valid mathematical expression consisting of non-negative integers with operators +,*,-,/. You may assume, the answer can be evaluated using a 64-bit signed integer. Evaluation must follow the standard mathematical rules.
```
Sample 0
Input
s: "1+2*6/4"

Output
4

Sample 1
Input
s: "120-190*2/5+4"

Output
48
```

### Sliding Window Maximum

Given an array of integers A.  There is a sliding window of size B which 

is moving from the very left of the array to the very right. 

You can only see the w numbers in the window. Each time the sliding window moves 

rightwards by one position. You have to find the maximum for each window. 

The following example will give you more clarity.

The array A is [1 3 -1 -3 5 3 6 7], and B is 3.
```
Window position	Max
———————————-	————————-
[1  3  -1] -3  5  3  6  7	3
1 [3  -1  -3] 5  3  6  7	3
1  3 [-1  -3  5] 3  6  7	5
1  3  -1 [-3  5  3] 6  7	5
1  3  -1  -3 [5  3  6] 7	6
1  3  -1  -3  5 [3  6  7]	7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Note: If B > length of the array, return 1 element with the max of the array.
```
### Window String
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.

Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

Example :
```
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"
```
### 4 Sum
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example : 

Given array S = {1 0 -1 0 -2 2}, and target = 0

A solution set is:
```
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)
```
Also make sure that the solution set is lexicographically sorted.
### Search in rotated sorted array
Given an array of integers nums of size N and an integer target.

array nums is rotated at some pivot unknown to you beforehand.

Example : [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

You are given a target value to search. Find if the target exists in the array.

You may assume no duplicate exists in the array.

Note:

Array nums was sorted in non-decreasing order before rotation.
Do not sort the array.
Expected a solution better than linear search.
Do not use inbuilt functions.
target and array elements can be positive, 0 or negative.
```
Sample 0
Input
nums = [4, 5, 6, 7, 0, 1, 2, 3]

Target: 4

Output
true

Sample 1
Input
nums = [5, 17, 100, 3]

Target: 6

Output
false
```

### Majority Element
Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

Examples : 
```
Become a success story instead of just reading about them. Prepare for coding interviews at Amazon and other top product-based companies with our Amazon Test Series. Includes topic-wise practice questions on all important DSA topics along with 10 practice contests of 2 hours each. Designed by industry experts that will surely help you practice and sharpen your programming skills. Wait no more, start your preparation today!

Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater
than the half of the size of the array size. 

Input : {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is
greater than the half of the size of the array size.
```

### N/3 Repeat Number

You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example:
```
Input : [10, 10, 20, 30, 10, 10]
Output : 10
10 occurs 4 times which is more than 6/3.

Input : [20, 30, 10, 10, 5, 4, 20, 1, 2]
Output : -1
```
### Max Distance

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

```
Example Input
Input 1:

 A = [3, 5, 4, 2]


Example Output
Output 1:

 2
```

### Google 1
Round 1: Single Number-ii

https://leetcode.com/problems/single-number-ii
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
 
```
Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
```

Round 2: Decode String

https://leetcode.com/problems/decode-string

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 
```
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
```

Round 3:

Given a tree representation of a html parsed output, wherein every block is a node in the tree, find if two html docs contain the same text.

Round 4:

Given a 2D matrix M X N, support two operations:
Query(row1, col1, row2, col2) such that I get the sum of all numbers in the rectangle ((row1, col1), (row1, col2), (row2, col1), (row2, col2)) and
Update(row, col) to a new number

And query is a very frequent operation and update is a rare operation, so query should be really fast, but update can be slower.

Follow up: How would you solve this in a distributed fashion

Round 5:

https://leetcode.com/problems/toeplitz-matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

```
Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
Follow-up: assume that the whole matrix cannot be fit in memory and should be read from a file, assume that a few rows and all columns can be read in, how to verify?
```

### Array
#### Order Of People Heights
You are given the following :

A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the number of persons who are taller than P and standing in front of P
You need to return  list of actual order of persons’s height

Consider that heights will be unique

Example
```
Input : 
Heights: 5 3 2 6 1 4
InFronts: 0 1 2 0 3 2
Output : 
actual order is: 5 3 2 1 6 4 
So, you can see that for the person with height 5, there is no one taller than him who is in front of him, and hence Infronts has 0 for him.

For person with height 3, there is 1 person ( Height : 5 ) in front of him who is taller than him.

```
#### Move Zeros To End
Given a static-sized array of integers arr, move all zeroes in the array to the end of the array. You should preserve the relative order of items in the array.

We should implement a solution that is more efficient than a naive brute force.

Examples:
```
input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
```
### Heap and Map
#### Merge K Sorted Lists

Merge k sorted linked lists and return it as one sorted list.

Example :
```
1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
```
will result in
```
1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
```
#### 480. Sliding Window Median
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

Example 1:
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
```
### Tree
#### Least Common Ancestor

Find the lowest common ancestor in an unordered binary tree given two values in the tree.

Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.

Example :
```

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
```
For the above tree, the LCA of nodes 5 and 1 is 3.

LCA = Lowest common ancestor

Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.

#### Shortest Unique Prefix
Find shortest unique prefix to represent each word in the list.

Example:
```
Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
```
```
class MyNode:
        def __init__(self):
            self.h={}
        def insert(self, a, i=0):
              if a[i] in self.h and type(self.h[a[i]])==str:
                  e=self.h[a[i]]
                  c = MyNode()
                  c.insert(e, i+1)
                  c.insert(a, i+1)
                  self.h[a[i]]=c
              elif a[i] in self.h:
                  self.h[a[i]].insert(a, i+1)
              else:
                self.h[a[i]] = a
        def traverse(self, r={}, p=""):
            for k in self.h.keys():
                if type(self.h[k])==str:
                    r[self.h[k]] = p+k
                else:
                    self.h[k].traverse(r, p+k)
            return r

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        t = MyNode()
        for a in A:
            t.insert(a)
        h = t.traverse()
        result=[]
        for a in A:
            result.append(h[a])
        return result


```
### 2D Matrix
#### Max Rectangle in Binary Matrix 
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :
```
A : [  1 1 1
       0 1 1
       1 0 0 
    ]

Output : 4 

[
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
  [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
  [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
  [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0]
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
]

The expected return value: 
30
```
As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)

https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/
#### Trapping 2D Rainwater
Rocky is an architect. He likes to build different unique structures.
He made structure of pillars of the same width and breadth but having different heights in a region.
He wants to find out, maximum volume of water the structure can hold when it rains.
Given N x M matrix heights where,
heights[ i ][ j ] = height of pillar at ( i, j )
Return the maximum volume of water the structure can hold.
```
Sample 0
Input
heights:

	[
		[5, 5, 5, 5],
		[5, 0, 0, 5],
		[5, 0, 0, 5],
		[5, 5, 5, 5]
	]
Output
20
Sample 1
Input
heights:
	[
		[1, 2, 5, 9],
		[3, 2, 6, 11],
		[4, 9, 2, 7],
		[7, 8, 9, 10]
	]
Output
4
Explanation
Only pillar at (2,2) with height 2 can hold water of 4 cubic units.
```
#### Rotate Matrix

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:
```
If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
```
#### Valid Sudoku

Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.

The input corresponding to the above configuration :
```
["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
```
A partially filled sudoku which is valid.

Note:

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

### Binary Search
#### Find the high and low index
Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found.

The array length can be in the millions with many duplicates.

In the following example, according to the the key, the low and high indices would be:

key: 1, low = 0 and high = 0

key: 2, low = 1 and high = 1

key: 5, low = 2 and high = 9

key: 20, low = 10 and high = 10


### Math
#### Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
Example 1:
```
Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
```
https://leetcode.com/problems/number-of-digit-one/

```
class Solution(object):
    def countDigitOne(self, m):
        i = 0
        remainder=0
        total = 0
        while m:
            r = m % 10
            m = m // 10

            # (m) d_i (remainder)
            # total ones:
            #     (m) * 10^i + 10^i, if d_i>1
            #     (m) * 10^i + remainder, if d_i==1
            total += m * int(pow(10, i))

            if r == 1 and i>0:
                total = total + remainder + 1
            elif r > 1 and i>0:
                total = total + int(pow(10, i))
            remainder = remainder + int(r*pow(10,i))

            i += 1
        return total

s = Solution()
print(s.countDigitOne(99))
```
#### 483. Smallest Good Base
Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.

Example 1:
```
Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
```
#### Puzzles
Question: How many times the hands of a clock, minute, and hour hands, overlap one another in a single day, i.e., 24 hours? Explain mathematically. Also, mention the time when they will do so.

Question: Use the mathematical operations +, -, *, and / on 3, 3, 7, 7 to get 24.

Question: How will you get 10000 by adding only 8?

### Sort
#### 315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
```
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```
Example 2:
```
Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
```
#### 493. Reverse Pairs
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

 

Example 1:
```
Input: nums = [1,3,2,3,1]
Output: 2
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
```
### Linked Lists
### Stacks and Queues
#### Longest valid Parentheses

Given a string A containing just the characters ’(‘ and ’)’.

Find the length of the longest valid (well-formed) parentheses substring.

For Example
```
Input 1:
    A = "(()"
Output 1:
    2
    Explanation 1:
        The longest valid parentheses substring is "()", which has length = 2.

Input 2:
    A = ")()())"
Output 2:
    4
    Explanation 2:
        The longest valid parentheses substring is "()()", which has length = 4.
```
### Backtracking
### Dynamic Programming
#### Distinct Subsequences
Given two sequences A, B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).

Example :
```
Input 1:
    A = "abc"
    B = "abc"
    
Output 1:
    1

Explanation 1:
    Both the strings are equal.

Input 2:
    A = "rabbbit" 
    B = "rabbit"

Output 2:
    3

Explanation 2:
    These are the possible removals of characters:
        => A = "ra_bbit" 
        => A = "rab_bit" 
        => A = "rabb_it"
        
    Note: "_" marks the removed character.
```

```
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B, i=0, memo={}):
        k = self.k(A, i)
        if self.compare(A, B):
            result = 1
        elif len(k)<len(B):
            result = 0
        elif i >= len(A):
            return 0
        elif k in memo:
            # print(k, A, memo[k])
            return memo[k]
        else:
            r1 = self.numDistinct(A, B, i+1, memo)
            r2 = self.numDistinct(A[0:i]+'_'+A[i+1:len(A)], B, i+1, memo)
            result = r1+r2
        memo[k]=result
        return result

    def compare(self, A, B):
        A = A.replace('_','').split(":")[0]
        return A==B

    def k(self, A, i):
        return A.replace('_','')+":"+str(i)


s = Solution()
A="aaaababbababbaabbaaababaaabbbaaabbb"
B="bbababa"
print(s.numDistinct(A, B))
#22113

"""
bbaaababaaabbbaaabbb:16 _______________bbaaababaaabbbaaabbb 261
baaababaaabbbaaabbb:17 ________________baaababaaabbbaaabbb 27
aaababaaabbbaaabbb:18 _________________aaababaaabbbaaabbb 0
aababaaabbbaaabbb:19 __________________aababaaabbbaaabbb 0

22113

Process finished with exit code 0
"""

```
#### Palindrome Partitioning II

Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.

Examples:
```
Input 1:
    A = "aba"

Output 1:
    0

Explanation 1:
    "aba" is already a palindrome, so no cuts are needed.

Input 2:
    A = "aab"
    
Output 2:
    1

Explanation 2:
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

#### Edit Distance

Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:
```
Insert a character
Delete a character
Replace a character
```

Examples:
```
Input 1:
    A = "abad"
    B = "abac"

Output 1:
    1

Explanation 1:
    Operation 1: Replace d with c.

Input 2:
    A = "Anshuman"
    B = "Antihuman"

Output 2:
    2

Explanation 2:
    => Operation 1: Replace s with t.
    => Operation 2: Insert i.
```
#### Regular Expression II
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.

'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:

int isMatch(const char *s, const char *p)
Some examples:
```
isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
```
#### Interleaving Strings
Given A, B, C, find whether C is formed by the interleaving of A and B.

Examples:
```
Input 1:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbcbcac"

Output 1:
    1
    
Explanation 1:
    "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)

Input 2:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbbaccc"

Output 2:
    0

Explanation 2:
    It is not possible to get C by interleaving A and B.
```    
#### Shortest common superstring
Given a set of strings, A of length N.

Return the length of smallest string which has all the strings in the set as substring.

Example:
```
Input 1:
    A = ["aaaa", "aa"]

Output 1:
    4

Explanation 1:
    Shortest string: "aaaa"

Input 2:
    A = ["abcd", "cdef", "fgh", "de"]

Output 2:
    8

Explanation 2:
    Shortest string: "abcdefgh"
```    
#### Increasing Path in Matrix
Given a 2D integer matrix A of size N x M.

From A[i][j] you can move to A[i+1][j], if A[i+1][j] > A[i][j], or can move to A[i][j+1] if A[i][j+1] > A[i][j].

The task is to find and output the longest path length if we start from (0, 0).

NOTE:
If there doesn't exist a path return -1.

Example Input
```
Input 1:

 A = [  [1, 2]
        [3, 4]
     ]
Input 2:

 A = [  [1, 2, 3, 4]
        [2, 2, 3, 4]
        [3, 2, 3, 4]
        [4, 5, 6, 7]
     ]


Example Output
Output 1:

 3
Output 2:

 7


Example Explanation
Explanation 1:

 Longest path is either 1 2 4 or 1 3 4.
Explanation 2:

 Longest path is 1 2 3 4 5 6 7.

```
#### Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:
```
input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
```

### Recursive
#### Repeating Sub-Sequence
Given a string A, find length of the longest repeating sub-sequence such that the two subsequence don’t have same string character at same position,

i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

NOTE: Sub-sequence length should be greater than or equal to 2.

Example Input
```
Input 1:

 A = "aabebcdd"

Example Output
Output 1:

 2 (abd abd)
```
#### Word Ladder I

Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

You must change exactly one character in every transformation.
Each intermediate word must exist in the dictionary.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

Example :
```
Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log"]

Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
```
#### Integer to English Words
Convert a non-negative integer num to its English words representation.

Example 1:
```
Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```
#### 473. Matchsticks to Square
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:

```
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
```	
### Greedy Algorithm
#### Gas Station
Given two integer arrays A and B of size N.

There are N gas stations along a circular route, where the amount of gas at station i is A[i].

You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i 

to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, … n-1, 0, 1, 2.. Completing the circuit means starting at i and 

ending up at i again.

Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.

For Example

```
Input 1:
    A =  [1, 2]
    B =  [2, 1]
Output 1:
    1
    Explanation 1:
        If you start from index 0, you can fill in A[0] = 1 amount of gas. Now your tank has 1 unit of gas. But you need B[0] = 2 gas to travel to station 1. 
        If you start from index 1, you can fill in A[1] = 2 amount of gas. Now your tank has 2 units of gas. You need B[1] = 1 gas to get to station 0. So, you travel to station 0 and still have 1 unit of gas left over. You fill in A[0] = 1 unit of additional gas, making your current gas = 2. It costs you B[0] = 2 to get to station 1, which you do and complete the circuit. 

```
#### Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :
```
Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
```
#### Disjoint Intervals

Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.

Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.

Return a integer denoting the length of maximal set of mutually disjoint intervals.



```
Example Input
Input 1:

 A = [
       [1, 4]
       [2, 3]
       [4, 6]
       [8, 9]
     ]
Input 2:

 A = [
       [1, 9]
       [2, 3]
       [5, 7]
     ]


Example Output
Output 1:

 3
Output 2:

 2


Example Explanation
Explanation 1:

 Intervals: [ [1, 4], [2, 3], [4, 6], [8, 9] ]
 Intervals [2, 3] and [1, 4] overlap.
 We must include [2, 3] because if [1, 4] is included thenwe cannot include [4, 6].
 We can include at max three disjoint intervals: [[2, 3], [4, 6], [8, 9]]
Explanation 2:

 Intervals: [ [1, 9], [2, 3], [5, 7] ]
 We can include at max two disjoint intervals: [[2, 3], [5, 7]]
```
### Graph
#### Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

A height balanced BST : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example :
```
Given A : 1 -> 2 -> 3
A height balanced BST  :

      2
    /   \
   1     3
```
#### Capture Regions on Board

Given a 2D character matrix A of size N x M, containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

```
Example Input
Input 1:

 A = [  [X, X, X, X],
        [X, O, O, X],
        [X, X, O, X],
        [X, O, X, X]
     ]


Example Output
Output 1:

 A = [  [X, X, X, X],
        [X, X, X, X],
        [X, X, X, X],
        [X, O, X, X]
     ]


Example Explanation
Explanation 1:

 'O' in (4,2) is not surrounded by X from below.
``` 
### Complexity
#### Validate IP Address
Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.

For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" are valid IP addresses, while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.

Require constant complexity.

Examples:
```
ip = '192.168.0.1'
output: true

ip = '0.0.0.0'
output: true

ip = '123.24.59.99'
output: true

ip = '192.168.123.456'
output: false
```

### Puzzles
#### Cross the Bridge

Four people are on this side of the bridge. Everyone has to get across. 

Problem is that it’s dark and so you can’t cross the bridge without a flashlight and they only have one flashlight. 

Plus the bridge is only big enough for two people to cross at once. 

The four people walk at different speeds:
```
one fella is so fast it only takes him 1 minute to cross the bridge,
another 2 minutes,
a third 5 minutes,
the last it takes 10 minutes to cross the bridge.
When two people cross the bridge together (sharing the flashlight), they both walk at the slower person’s pace. What is the minimum time required for all 4 to cross the bridge.
```
#### Eggs and Building

There is a building of 100 floors

If an egg drops from the Nth floor or above it will break. If it’s dropped from any floor below, it will not break. You’re given 2 eggs. Find N, while minimizing the number of drops for the worst case.

These are very strong eggs, because they can be dropped multiple times without breaking as long as they are dropped from floors below their “threshold” floor, floor N. But once an egg is dropped from a floor above it’s threshold floor, it will break.

Output the minimum number of drops required to figure out N.

#### Ratio of Boys and Girls

In a country where everyone wants a kid with a specific gender (assuming only 2 genders), each family continues having babies till they have a kid with the expected gender. After some time, what is the proportion of boys to girls in the country? (Assuming probability of having a boy or a girl is the same)

