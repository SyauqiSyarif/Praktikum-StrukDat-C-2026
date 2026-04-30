stack = []

stack.append('tiktok.com')
stack.append('github.com')
stack.append('w3shool.com')
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

print("Size: ",len(stack))