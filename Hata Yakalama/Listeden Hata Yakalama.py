liste = ["345","sadas","324a","14","kemal"]

"""
for i in liste:
    try:
        i==int(i)
        print(i)
    except:
        pass
"""

for i in liste:
    try:
        if i!=int(i):
         print(i)
    except:
        pass
