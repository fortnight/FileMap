#Create a JSON object that has a name, a list of JSON objects called children, and a size that gets printed out if and only if that object has a filesize
#ls -l will give the approximate size of a file - size is 6th thing printed [element #5]
#json library to dump out into a json string
#os.path library to manipulate path variables.

def __JNOS__(self):
    self.name = ''
    self.children = []
    self.size = 0

def main():
    myFile = 'myfile.txt'
    f = open(myFile)
    path = f.readline()[:-1] + '/'
    for line in f:
        line = path + line[2:-1]
        #line = '"name": "' + line + '",'
        #print(line)

#split string into string array by / characters
#while index doesn't equal length of array minus one:
    #go down the jnos object, cur child, cur name, string[index]
#once on the deepest child, set string[index] to be a child of cur name
#rinse and repeat for each line

main()
