#file to store something permanently 
try: 
    f = open("file.txt", "r")
    content = f.read()
    print(content)
    f.close()

except Exception as e:
        print(e)


#write to a file 

f = open("Nadia.txt", "w")
str = '''
Hey!! I'm Nadia. I am learning python and its very easy and interesting language
'''
f.write(str)
f.close()

#append to a file 

f = open("Nadia.txt", "a")
str = '''
i am preparing notes along with learning. It will be helpful for anyone wants to get started with python
'''
f.write(str)
f.close()
