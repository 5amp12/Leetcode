class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        lower_dir = 0
        dir = ""

        while stack:
            if stack[-1] == '' or stack[-1] == '.':
                stack.pop()
                continue
            elif stack[-1] == '..':
                stack.pop()    #possible issue here
                lower_dir +=1
            else:
                if lower_dir > 0:
                    stack.pop()
                    lower_dir -=1
                else:
                    dir = "/" + stack.pop() + dir
        if dir is "":
            dir = "/"
        return dir
            