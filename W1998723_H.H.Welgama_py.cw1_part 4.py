#Student id: w1998723
#IIT student id: 20221109
#Name: H.H.Welgama
#Date: 05/04/2023
#SD1 part 4 of the coursework
#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
# Any code taken from other sources is referenced within my code solution.

#Main CODE

progress=0
trailer=0
retriver=0
exclude=0

count_stu=0
Menu_option='y'
menu=""
star="*"
list=[]
my_Dict={}
       
#function for printing histogram       
def output_histogram_at_the_end(progress, trailer, retriver, exclude,count_stu):
    print("\n"+"-"*80)
    
    print("Histogram")
    
    print( f"progress:{progress}\t: {star * progress}")
    print( f"Trailer-{trailer}\t: {star * trailer}")
    print( f"Retriver-{retriver}\t: {star * retriver}")
    print( f"Exclude-{exclude}\t: {star * exclude}")
    print("\n"+"-"*80)
    print("total output at the end:",count_stu)
    print("\n"+"-"*80)
    
#function of cheking validity of the inputs
def stu_credits(invalid_options):                   
    while True:
        try:
            stu_credits=int(input(f"could you please enter your credits at {invalid_options}"))
        except Exception as e:
            print("Integer required",e)
            continue
        if stu_credits not in [0,20,40,60,80,100,120]:
            print("Out of range")
            continue
        break
    return stu_credits

#menu to select
while True:
    try:                                                                        
        print("_"*20+"Welcome to the University of Westminster!"+"_"*19)
        print("\n"+"Press *1* for student.\npress *2* for staff.")
        Main_menu=int(input("Enter :" ))
        print("\n"+"-"*80)
    except Exception as e:
        print("Invalid. press again *1* or *2*.",e)
        continue
    if Main_menu not in [1,2]:
        print("Invalid. press again *1* or *2*")
        continue
    while True:                                                     
        stu_id = input("\n"+"Please enter your student UoW student id:")  #checking validity of Student ID
        print("\n"+"-"*80)
        if len(stu_id)!=8 or stu_id[0]!="w":
            print("Invalid UoW id, Re-enter your UoW id:")
            continue
        if not (stu_id[1:].isdigit()):
            print("Invalid UoW id, Re-enter your UoW id:")
            continue
        else:
            break
        
    while True:
        
         
        pass_c= stu_credits("Pass:")
        defer_c= stu_credits("Defer:")
        fail_c= stu_credits("Fail:")
        tot=pass_c+defer_c+fail_c   #Total checking      
        if tot!=120:
            print("Total credits incorrect")
        else:
            count_stu=count_stu+1
            if pass_c==120:                                         
                print("Progress")
                progress=progress+1
                extension="Progress - "+str(pass_c)+","+str(defer_c)+","+str(fail_c)   #Adding to dictionary      
            elif pass_c==100:
                print("Progress (module trailer)")
                trailer=trailer+1
                extension="Progress (module trailer) - "+str(pass_c)+","+str(defer_c)+","+str(fail_c)
            elif fail_c>60:
                print("Exclude")
                exclude=exclude+1
                extension="Exclude - "+str(pass_c)+","+str(defer_c)+","+str(fail_c)
            else:
                print("Module retriever ")
                retriver=retriver+1
                extension="module retriever - "+str(pass_c)+","+str(defer_c)+","+str(fail_c)
            if Main_menu ==1:
                break
            if Main_menu ==2:
                my_Dict.update({stu_id:extension})   
                while True:
                    Menu_option=str(input("\n"+"Do you want to input another set of information? \nEnter 'y' for yes or Quit and view results by pressing 'q' :"))
                    print("\n")
                    if Menu_option.lower() == "q":
                        output_histogram_at_the_end(progress, trailer, retriver, exclude,count_stu)
                        break
                    elif Menu_option.lower() =="y":
                        while True:
                            stu_id = input("Please enter your student UoW student id:")
                            if  len(stu_id) !=8 or stu_id[0]!="w":
                                print("Invalid UoW student ID, Re-enter your UoW student id:")
                                continue
                            if not(stu_id[1:].isdigit()):
                                print("Invalid UoW student id, Re-enter your UoW student id:")
                                continue
                            else:
                                
                                break
                            break
                    else:
                        print("\n"+"Invalid UoW student id,Re-enter your Uow id:")
                        continue
                    break
                if Menu_option.lower() == "q":
                    break
                elif Menu_option.lower() =="y":
                    continue
                break
            if Menu_option.lower() == "q":
                break
    my_Dict.update({stu_id:extension})     #updating Dictionary     
    if Main_menu ==1:
        break
    if Menu_option.lower() == "q":
        break                   
for stu_id,extension in my_Dict.items():#printing Dictionary
    print(stu_id,":",extension,end=" ")
print("\n"+""*80)   
print("_"*35+"Thank you!"+"_"*35)
               

    


















        

    














        

    
