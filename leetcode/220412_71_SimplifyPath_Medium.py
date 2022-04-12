# String, Stack

class Solution:
    def simplifyPath(self, path):
        st = []

        for file in path.split('/'):
            if st and file == '..':
                st.pop()
            elif file not in ['.', '', '..']:
                st.append(file)

        return '/' + '/'.join(st)
