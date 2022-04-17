# https://leetcode.com/problems/simplify-path/submissions/
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        terms = path.split('/')
        result = []
        for term in terms:
            if term:
                if term != '.':
                    if term == '..':
                        if result:
                            result = result[0:len(result)-1]
                    else:
                        result.append(term)
        return '/' + '/'.join(result)