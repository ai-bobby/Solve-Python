class Files:
    def __init__(self,file_nsme,file_mode):
        self.file_name = file_nsme
        self.file_mode = file_mode
        self.file_content = None

    def __enter__(self):
        self.file_content = open(self.file_name, self.file_mode)
        return self.file_content
    
    def __exit__(self,*exc_value):
        if self.file_content :
            self.file_content.close()


# -------------------------------------------------------------

def writeLineToFile(file_name,line):
    with open(file_name, 'a') as file:
        file.write(line)
try:
    pass
    flag1 ,flag2 =False,False
    with Files('File\courses_program.txt','r') as file:
        while file:
            line = file.readline()

            if line == 'Python Basic for Beginners\n':
                flag1 = True
            
            elif line == 'Python for Engineers and Scientists\n':
                flag2 = True

            if line == '\n':
                flag1 ,flag2 = False,False
            
            if flag1 == True:
                writeLineToFile('File/file1.txt',line)
            
            elif flag2 ==True:
                writeLineToFile('File/file2.txt',line)

            if line =='':
                break
            
            print(line,end='')

except Exception as error:
    print('Error: %s' % error)