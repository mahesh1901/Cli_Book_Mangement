import json
list_data="list_data.json"
print("Welocome To The Library of Nimap..... ")
ch=int(input("Enter The Choice: \n1. Login \tt2.Exist..  :- "))
for i in range(3):
    
    if ch==1:
        Uname=input("Enter the Username: ") 
        passe=input("Enter the Password: ")
        #if Uname=='abc' and passe=='abc@123':
        if True:

            while True:
                
                choice=int(input("Enter the Choice:\n1.Add_Books \t2. Show_list \n3. Update Books \t4. Delete_Books \n5. Exist.. :- "))
                #try:
                if choice==1:
                    print("Adding Books")
                    book_id=int(input("Enter The Id of Book : "))
                    book_Name=input("Enter the Book Name : ")
                    Author=input("Enter the Name of Book Author : ")
                    price=int(input("Enter the Price of Book : "))
                    #Add_Data=[{'Book_id':book_id},{'Book_Name':book_Name},{'Author':Author},{'Price':price}]
                    Add_Data={'Book_id':book_id,'Book_Name':book_Name,'Author':Author,'Price':price}

                    with open(list_data,"r") as read_it:
                        try:
                            data=json.load(read_it)
                        except json.decoder.JSONDecodeError as emptyfile:
                            print(emptyfile)
                            data = {}
                            
                    #print("\n\ndata from json=",data, "\ntype of data=", type(data))
                    data[str(book_id)]=Add_Data
                            
                    #print("\ndata to be added in json=",data, "\ntype of data=", type(data))
                    
                    with open(list_data, "w") as outfile:
                        json.dump(data,outfile)

                   
                elif choice==2:
                    print("Showing The List Of Books")
                
                    with open(list_data,"r") as read_it:
                        try:
                            data=json.load(read_it)
                        
                            count=0
                            for k in data:
                                print(k,data[k])
                                count+=1
                                if count%10==0:
                                    ch=input("Do u want to see next 10 records(Y/N)?")
                                    if ch=='Y' or ch=='y':
                                        continue
                                    else:
                                        break
                            print("data printed")
                        except json.decoder.JSONDecodeError as emptyfile:
                            print("\n\nFile was empty\n",emptyfile)

                        
                    
                elif choice==3:
                    print("Update Books")
                    Book_id=int(input("Enter the Book_id To Update: "))
                    Update_Price=int(input("Enter the Updating Price :  "))

                    with open(list_data,'r')as read :
                        update_book = json.load(read)

                    update_book[str(Book_id)]["price"]=Update_Price

                    print("Books Update Sucessfully ")

                    with open(list_data, 'w')as update_file:
                        json.dump(update_book,update_file)

                    print("Data Added Succesfully ")
                    
                    



                elif choice==4:
                    print("Delete Books")

                elif choice==5:
                    print("Existing from Programe...")
                    break
                

                else:
                    print("Invalid Input")
                #except:
                 #   print("Something gone Wrong....")
        else:
            print("Please Provide Valid Username and Password")
            
    elif ch==2:
        print("Thanks for Visiting")
        break

    else:
        print("Invalid Input From User:")
    break        

else:
    print("To Many Unsuccessful Atempt")



