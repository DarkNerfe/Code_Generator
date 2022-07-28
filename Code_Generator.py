#testing...


# author: Nerfe Onug
# ~/Code_Generator.py
# version: 1.0

#import goes here
import os                                       # to use command line cli
import random
import sys

# public varibales


code_list_datatype=[]                           # initializing a list that where datatypes are stored in every index of the list


def Banner():
    print("\t\t\tCode Generator\n\n")           # print string in the center

def Update_Code_List_Datatype(code_list_datatype):
    print("\t\tCode Data Type:",code_list_datatype,"\n\n") # it prints the recent value of each index of the list

def Code_Generator_Get_Details():                           #  main function
    
    Banner()                                    # Calling a function which display Progran Name or called banner
  
    global index_Range                          # variable declaration which can be used/access globally

    index_Range=int(input("Input Code Range: "))# ask a user for the range index of code to be generated 
    
    i=0                                         # initialize the i for the increment in the loop
    

    # start of loop 
    while(i != index_Range):                    # starting of the loop which specified by range function that has start and end of th increment
        
        os.system('cls')                        # a built in function that could clear screen by using os. in window uses "clear" but in linux uses "cls"
        
        Banner()                                # Calling a function which display Progran Name or called banner
        
        Update_Code_List_Datatype(code_list_datatype)
        print("Data Types: \n\n\t1.Integer\n\t2.UpperCase Character\n\t3.LowerCase Character\n\t4.Static\n\tQ or q to Quit\n") # it prints the choices for the user to use  

        choices=input("Input Choices at Index {0}: ".format(i+1)) # "input" where value is stored in variable "choice" from the user input and display input message and its index number of list 

        if(choices=='1'):                       # it determines the user input that matches the  if condtion
        
            code_list_datatype.append("Int")    # if the condition is true, then it add the string  "int" to the current index of list
            
            i+=1                                #increment
        
        elif(choices=='2'):                     # it determines the user input that matches the  else if condtion
            
            code_list_datatype.append("CHAR")   # else if the condition is true, then it add the string  "CHAR" to the current index of list
            
            i+=1                                #increment
        
        elif(choices=='3'):                     # it determines the user input that matches the  else if condtion
            
            code_list_datatype.append("Char")   # else if the condition is true then it add the string  "Char" to the current index of list

            i+=1                                #increment

        elif(choices=='4'):                     # it determines the user input that matches the  else if condtion
            
            Input=input("Input Value: ")        # "input" where value is stored in variable "Input" from the user input with display input message

            code_list_datatype.append(Input[0])# else if the condition is true then it add the unchangeble  Character of the code index  from user input to the current index of list
            
            i+=1                                #increment
                                                    
        elif(choices.lower()=='q'):             # it determines the user input that matches the  else if condtion and convert the input into lower case to avoid error
            
            print("\n\n\tProgram Termanated...")# print the message that tells that the program is end

            sys.exit()
            
            
            
        else:                                   # the else condition it determines that the all recent condtion is doesn't match the user input
            print("Invalid input!!\n\tPlease Try Again!") # prints the string message
    # End of the loop
 
    os.system('cls')                            # a built in function that could clear screen by using os. in window uses "clear" but in linux uses "cls"
 
    Banner()                                    # Calling a function which display Progran Name or called banner
  
    Update_Code_List_Datatype(code_list_datatype)# calling the function with a value of its parameter/ it update the value of list 

def Generate():
    
    all_list            
    for j in range(total_Range()):

        code_list=[]


        for i in range(index_Range):

            if(code_list_datatype[i]=='Int'):
                rand=random.randint(0,9)
                code_list.append(rand)
    
            elif(code_list_datatype[i]=='CHAR'):
                rand=chr(random.randint(65,90))
                code_list.append(rand)
    
            elif(code_list_datatype[i]=='Char'):
                rand=chr(random.randint(97,122))
                code_list.append(rand)
    
            else:
                code_list.append(code_list_datatype[i])


    


def total_Range():
    r_Int=10
    r_CHAR=90-65+1
    r_Char=122-97+1
    r_code=[]
    total=1
    for j in range(0,index_Range):

        if(code_list_datatype[j]=='Int'):
            r_code.append(r_Int)
        elif(code_list_datatype[j]=='CHAR'):
            r_code.append(r_CHAR)
        elif(code_list_datatype[j]=='Char'):
            r_code.append(r_Char)
        else:
            r_code.append(1)

        total=total*r_code[j]

        j=j+1
    return total




# next task is to add anoher function that generate the code by index       
# undone task:   make the range variable into public


  #  SaveToFile()

    print("\n\nPenetration goes here but for now is undergoing...\n\t\t\tPlease stay tunned!\n\n\n")# Notice message for updates are incomming







################################################################################################################################




if __name__=="__main__":                        # a condtion where the program starts to excuted

    Code_Generator_Get_Details()                            # calling the function
    print(Generate())    
       



