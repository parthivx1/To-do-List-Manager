def notice(title):
    print()
    print('------> '+title+' <------')
    print()
def printbox(title):
    print('+'+'-'*(len(title)+2)+'+')
    print('|'+' '+title+' '+'|')
    print('+'+'-'*(len(title)+2)+'+')


def login():
    import pickle
    f=open('uridpwd.dat','rb')
    details={}
    try:
        while True:
            det=pickle.load(f)
            for i in det:
                k=i   
                v=det[i]
                details[k]=v  
    except EOFError:
        f.close()
    print('enter user id')
    u=input('->')
    if u in details:
        print('Enter password')
        pwd=input('->')
        if details[u][0]==pwd:
            notice('login successful!!!')
            manage_todo()
        else:
            notice('invalid password entered!!!')
            ch=input('do you want to change password<y/n>: ')
            if ch=='y':
                print('enter',details[u][1])
                a=input('->')
                if a==details[u][2]:
                    notice('security check passed')
                    npwd=input('enter new password: ')
                    import pickle
                    f=open('uridpwd.dat','wb')
                    details[u][0]=npwd
                    pickle.dump(details,f)
                    notice('PASSWORD SUCCESSFULLY UPDATED!!!')
                    f.close()
                else:
                    notice('you failed security check')
                    main()
                main()  
            else:
                main()
    else:
        notice('user id does not exist!!!') 
        main()
def newuser():
    import pickle
    f=open('uridpwd.dat','ab+')
    id =input('enter user id: ')
    pwd=input('enter password: ')
    print()
    print('1 what is your favourate colour')
    print('2 what is your favourate sport')
    print('3 what is your school name')
    print()
    ch=int(input('choose any of the security question[1/2/3]: '))
    print()
    if ch==1:
        ch ='what is your favourate colour'
    elif ch==2:
        ch ='what is your favourate sport'
    elif ch==3:
        ch ='what is your school name'
    else:
        notice('please enter valid security choise')
        notice('restart creataion of account')
        main()    
    a=input('enter answer for the security question: ')
    pickle.dump({id:[pwd,ch,a]},f)
    notice('Account succesfully created!!!')
    del id , pwd , ch , a   
    f.close()
    main()
def main():
    import pickle
    printbox('welcome')
    printbox('1 New Account')
    printbox('2 Login')
    printbox('3 Exit')
    print()
    try:
        ch=int(input('What do you like to start with?  ->'))
    except:
        notice('there was an attempt to enter non interger value!!!')   
    if(ch==1):
        newuser()
    elif(ch==2):
        login()
    elif(ch==3):
        printbox('exiting...')
    else:
        print()
        notice('Invalid choise made!!!') 
  

def manage_todo():
    todo_list = []
    import pickle
    try:
        with open("todo.dat", "rb") as f:
            todo_list = pickle.load(f)
    except FileNotFoundError:
        pass

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter priority (Low, Medium, High): ").capitalize()
            task = {
                "task": task_name,
                "priority": priority,
                "completed": False
            }
            todo_list.append(task)
            print("Task added successfully.")
        
        elif choice == "2":
            if not todo_list:
                print("No tasks in the to-do list.")
                continue
            print("\nTo-Do List:")
            for i in range(len(todo_list)):
                task = todo_list[i]
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"


                print(i + 1, ".", task["task"], "| Priority:", task["priority"], "| Status:", status)
        
        elif choice == "3":
            if not todo_list:
                print("No tasks to delete.")
                continue
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(todo_list):
                deleted_task = todo_list.pop(task_num - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")
        
        elif choice == "4":
            if not todo_list:
                print("No tasks to mark as completed.")
                continue
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]["completed"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        
        elif choice == "5":
            with open("todo.dat", "wb") as f:
                pickle.dump(todo_list, f)
            printbox("To-do list saved. Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


main()