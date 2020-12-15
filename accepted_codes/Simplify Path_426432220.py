class Solution:
    def simplifyPath(self, path: str) -> str:
        path1=path.split("/")
        stack=[]
        for s in path1:
            if(s=="" or s=="."):
                continue
            elif(s==".."):
                if(len(stack)!=0):
                    stack.pop()
                else:
                    continue
            else:
                stack.append(s)
        return "/"+'/'.join(stack)
