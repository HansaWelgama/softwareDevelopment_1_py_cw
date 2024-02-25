#Student id: w1998723
#IIT student id: 20221109
#Name: H.H.Welgama
#Date: 05/04/2023
#SD1 part 1, part 2 and part 3 of the coursework
#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
# Any code taken from other sources is referenced within my code solution.

#CODE
#input variables
progress=0 
trailer=0
retriver=0
exclude=0

tot=0
count_stu=0
Menu_option='y'
Main_menu=""
star="*"
list=[]

f = open("part3_text_file.txt", "w")         #file open in write mode
f.close()                                    #file close

#function for printing histogram      
def output_histogram_at_the_end(progress, trailer, retriver, exclude,count_stu):
    print("\n"+"="*80)
    
    print("Histogram")

    print( f"progress:{progress}\t: {star * progress}")
    print( f"Trailer-{trailer}\t: {star * trailer}")
    print( f"Retriver-{retriver}\t: {star * retriver}")
    print( f"Exclude-{exclude}\t: {star * exclude}")
    print("\n"+"-"*80)
    print("total output at the end:",count_stu)
    print("\n"+"="*80)

def stu_credits(invalid_options):            #function of cheking validity of the inputs
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
#user def fuctions for part 2
def print_list():
    print("\n"+"-"*80)
    print("\n")
    print('List')
    for extension in list:
        for h in extension:
            print(h, end=" ")
            print()
            print("\n"+"-"*80)


while True:
    try:                                                                        
        print('_'*20+"Welcome to the University of Westminster!"+"_"*19)
        print("\n"+"Press *1* for student.\npress *2* for staff.")            #Main menu to select(staff/student)

        Main_menu=int(input("Enter :" ))
        print("\n"+"-"*80)
    except Exception as e:
        print("Invalid. press again *1* or *2*.",e)
        continue
    if Main_menu not in [1,2]:
        print("Invalid. press again *1* or *2*")
        continue                                              
        
    while True:
        f=open("part3_text_file.txt","a")#open file to inputs
        pass_c= stu_credits("Pass:")
        defer_c= stu_credits("Defer:")
        fail_c= stu_credits("Fail:")
        tot=pass_c+defer_c+fail_c#total checking         
        if tot!=120:
            print("Total credits incorrect")
        else:
            count_stu=count_stu+1
            if pass_c==120:   #to output printing                                                    
                extension=[f"Progress - {pass_c},{defer_c},{fail_c}"]
                list.append(extension)#appending values for extension list
                print("Progress")
                f.write(str(f"{extension}\n"))  #file writing
                progress=progress+1
                
            elif pass_c==100:         
                extension=[f"Progress (module trailer) - {pass_c},{defer_c},{fail_c}"]
                list.append(extension)
                print("Progress (module trailer)")  
                f.write(str(f"{extension}\n"))
                trailer=trailer+1
            elif fail_c>60:
                extension=[f"Exclude - {pass_c},{defer_c},{fail_c}"]
                list.append(extension)
                print("Exclude")
                list.append(extension)
                f.write(str(f"{extension}\n"))
                exclude=exclude+1
            else:
                extension=[f"module retriever - {pass_c},{defer_c},{fail_c}"]
                list.append(extension)
                print("Module retriever ")
                f.write(str(f"{extension}\n"))
                retriver=retriver+1

                
            #part 3 opening a file
            if Main_menu ==1:
                print_list()
                f = open("part3_text_file.txt", "r")                     
                with open ('part3_text_file.txt','r') as part3_text_file:
                    f=part3_text_file.read()
                    f=f.replace('[','').replace(']','').replace("'",'').replace("'",'')
                with open ('part3_text_file.txt','w') as part3_text_file:
                    part3_text_file.write(f)
                    print('_'*35+"Thank you!"+"_"*35)
                break
             
            if Main_menu ==2:

                while True:
                    Menu_option=str(input("\n"+"Do you want to input another set of information? \nEnter 'y' for yes or Quit and view results by pressing 'q' :"))
                    print("\n")
                    if Menu_option.lower() == "q":
                        output_histogram_at_the_end(progress, trailer, retriver, exclude,count_stu)
                        break
                    elif Menu_option.lower()=="y":
                        break
                    else:
                        print("\n"+" invalid input, press again")
                        continue
                    break     
                if Menu_option.lower()  == "q":
                    break
                elif Menu_option.lower() =="y":
                    continue
                break
            if Menu_option.lower() == "q":
                break
        
    if Main_menu ==1:
        break
    if Menu_option.lower() == "q":
        break
#part 3 opening a file
#opening a file #https://stackoverflow.com/questions/3925614/how-do-you-read-a-file-into-a-list-in-python
#https://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python-with-newlines    
if Main_menu==2:
    print_list()
    f = open("part3_text_file.txt", "r")   #file writing                  
    with open ('part3_text_file.txt','r') as part3_file:     
        f=part3_file.read()
        f=f.replace('[','').replace(']','').replace("'",'').replace("'",'')

    with open ('part3_text_file.txt','w') as part3_file:
        part3_file.write(f)
        print("[Open 'part3_text_file.txt' for part 3]")
        print("_"*35+"Thank you!"+"_"*35)
        




    



