class student:
    #constructor
    def __init__(self, uid, name, branch):
        self.uid = uid
        self.name = name
        self.branch = branch
    #function to create & append new student
    def accept(self, newuid, newname, newbranch):
        ob = student(newuid, newname, newbranch)
        ls.append(ob)
    #function to display student details
    def display(self, ob):
        print("uid: ", ob.uid)
        print("name: ", ob.name)
        print("branch: ", ob.branch)
        print("\n")
    #function to search for the student details
    def search(self, rn):
        #print(len(ls))
        for i in range(len(ls)):
            #print(ls[i].uid)
            if(ls[i].uid == rn):
                #print(ls[i].uid)
                return i
    #function to delete the student deatils
    def delete (self, rn):
        i = obj.search(rn)
        del ls[i]
    #function to update the student details
    def update(self, rn, no):
        i = obj.search(rn)
        roll = no
        ls[i].uid = roll
#create list to add students
ls = []
#an object of student class
obj = student(' ',' ',' ')
#obj=student()

print("\n operations used: ")
print("\n 1. accept student details \n 2. display student details \n 3. search details of a student \n 4. delete details of a student \n 5. update student details \n 6. exit")
while True:
    ch = int(input("enter your choice: "))
    if(ch == 1):
        obj.accept("20mca1005", "vaishnavi", "mca")
        obj.accept("20mca1063", "himani", "mca")
        obj.accept("20mca1014", "sakshi", "mca")
        obj.accept("20mca1078", "anwesha", "mca")
        obj.accept("20mca1054", "suman", "mca")

    elif(ch == 2):
        print("\n")
        print("\n list of students: \n")
        for i in range(len(ls)):
            obj.display(ls[i])

    elif(ch == 3):
        print("\n student found!")
        s = obj.search("20mca1063")
        print(s)
        obj.display(ls[s])

    elif(ch == 4):
        obj.delete("20mca1054")
        print(len(ls))
        print("list after deletion: ")
        for i in range(len(ls)):
            obj.display(ls[i])

    elif(ch == 5):
        obj.update("20mca1014", "20mca1000")
        print(len(ls))
        print("list after updation: ")
        for i in range(len(ls)):
            obj.display(ls[i])

    else:
        print("thank you!")