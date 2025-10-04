class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return '/'
        s_path = []
        path_split = path.split("/")

        for i,c in enumerate(path_split):
            if not c or c == '.':
                continue
            if c == '..':
                if s_path:
                    s_path.pop()
            else:
                s_path.append(c)
        
        return "/" + "/".join(s_path)