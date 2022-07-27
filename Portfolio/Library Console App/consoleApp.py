import time
import booksSDK
#Tools required to run the app properly

print("\nHi!")
print("What books do you like?")
answer=input("\nYour answer:")
books=[]
#The main menu(essential)

while True:
    #The infinite loop(essential)

    if str.lower(answer)=='q':
        #In case the user wants to quit, he types 'Q'

        if len(books)==0:
            print("\nYou haven't entered any books. Are you sure?")
            zz=input()
            if str.lower(zz)=='yes':
                print("Quitting")
                time.sleep(1.5)
                break
                #In case the user wants to quit, but didn't enter any books, this will ask him if he's sure about his decision
            
            elif str.lower(zz)=='no':
                print("Alright. What books do you like?")
                answer=input()
                #If the user doesn't want to quit, this will allow him to continue 
            
            else:
                print("Invalid input. Please type only 'yes' or 'no' .")
                zz=input()
                #If the user types something wrong, this will remind him of the available options

        else:
            if len(books)==1:
                print(f"\nYour favourite book is {books[0][0]} ({books[0][1]} pages long)")
                #This will help with formatting the output in which the user typed only one book
                
                print("Do you want to add this book to your virtual collection?")
                sz=input()
                if str.lower(sz)=='yes':
                    booksSDK.add(books[0][0], books[0][1])
                    print("\nBook successfully saved")
                    print("Quitting")
                    time.sleep(1.5)
                    break
                    #This will allow the user to save his book to the database
                    
                else:
                    print("Ok. Quitting")
                    time.sleep(1.5)
                    break
                #In case the user doesn't want to save his book

            else:
                print("\nYour books:")
                for item in books:
                    print(f"{books.index(item)+1}){item[0]} ({item[1]} pages long)") #Helps with formatting the answer
                print("\nDo you want to add your books to your virtual collection?")
                sz=input()
                if str.lower(sz)=='yes':
                    for item in books:
                        booksSDK.add(item[0], item[1])
                    print("\nBooks successfully saved")
                    print("Quitting")
                    time.sleep(1.5)
                    quit()
                #This will allow the user to save his books to the database
                
                else:
                    print("Ok. Quitting")
                    time.sleep(1.5)
                    break
                #If the user typed more books and wants to quit without saving to the DB, this will do just that

    elif str.lower(answer)=="r":
        if len(books)==0:
            print("You can't remove a book because you don't have any. You can add books by typing them or you can quit by typing 'Q'.")
            answer=input()
            #If the user didn't add any books, this will remind him of that. It will also give him the chance to either add them or quit

        else:
            print("\n")
            for item in books:
                print(f"{item[0]} ({item[1]} pages long) - {books.index(item)}")
            print("What book would you like to remove?(Type the number next to the book)")
            #The lines above the 'print' statement will print the books the user added, while the above line will inform him about what he can do to remove them
 
            de=input()
            try:
                e=books.pop(int(de))
            except IndexError:
                print("Invalid input. Please type only the number next to the book you want to remove")
            except ValueError:
                print("Invalid input. Please type only the number next to the book you want to remove")
            #If the user enters the wrong number or something other than that, this will inform him about his mistake and will give him the chance to choose again

            else:
                print(f"Removed: {e[0]} ({e[1]} pages long)")
                #This will inform the user about the book removed

                if len(books)==0:
                    print('\nYou have removed all the books. If you want to add any, type them, but if you want to quit, type "Q"')
                    answer=input()
                #If the user removed all the books, this will inform him about it and will give him the chance to either quit or add other ones
    
    elif str.lower(answer)=='m':
        if len(books)==0:
            print("You can't modify a book because you don't have any. You can add books by typing them or you can quit by typing 'Q'.")
            answer=input()
            #If the user didn't add any books, this will remind him of that. It will also give him the chance to either add them or quit

        else:
            print('\n')
            for item in books:
                print(f"{item[0]} ({item[1]} pages long) - {books.index(item)}")
            print("What book would you like to modify?(Type the number next to the book)")
            zs=input()
            if str.lower(zs)=="q": #If the user wants to stop modifying any books, this will give him the chance to do so
                print("Good. You can add books by typing them, remove them by typing 'R' or quit by typing 'Q' .")
                answer=input()
            else:
                try:
                    zs=int(zs)
                except ValueError:
                    print("Invalid input. Please type only the number next to the book you want to remove")
                    #In case the user types something else than the number

                else:
                    if zs in range(len(books)): #Verifies whether the the number typed does indicate a book
                        print("Please enter a new title(if you want to keep the old title, press Enter)")
                        title=input()
                        if title=="":
                            title=books[zs][0]
                            print(f"The book will keep the old title({title})")
                        print('\nEnter a new page number(if you want to keep the old number of pages, press Enter.')
                        pages=input()
                        while True:
                            if pages=="": 
                                pages=books[zs][1]
                                print(f"The book will keep the old number of pages({pages})")
                                break
                            else:
                                try:
                                    pages=int(pages)
                                    break
                                except ValueError:
                                    print("Wrong input. Pages always represent a number")
                                    pages=input()
                                #The above code will ask the user for a new title and number of pages. Should the user want to not modify an aspect, the code will revert to the old one

                        i=[]
                        i.append(title)
                        i.append(pages)
                        books.insert(zs, i)
                        print(f'\nModification complete. If you want to quit, type "Q". ')
                        del books[zs+1]
                        #This implements the changes

    elif str.lower(answer)=='d':
        print("\nWelcome to the collections' menu")
        data=booksSDK.read()
        if len(data)==0:
            print("You have no books to your collections. You can add your entered books to the database when you quit the app")
            print("Try adding some")
            answer=input()
            #In case there are no books in the database, this will display that and will allow the user to continue using the application

        elif len(data)==1:
            print(f"Your book: {data[0][0]} ({data[0][1]} pages long)")
            print("\nIf you want to remove this book, type 'D'. If you want to modify it, type 'R'. ")
            print("If you want to go back to the main menu, type 'Q'.")
            db=input()
            #If there is only a book in the database, this will display it and will also display the options available

        else:
            d=booksSDK.readNEW()
            print(f"Your books:{d}")
            print("\nIf you want to remove a book, type 'R'. If you want to modify one, type 'U'. ")
            print("If you want to go back to the main menu, type 'Q'.")
            db=input()
            #If there are more than 1 books in the database, this will display them and will also display the available options

        if str.lower(db)=="q":
            print("Fine. You can add books by typing them or quit by typing 'Q' .")
            answer=input()
            #If the user wants to quit the collections' menu, this will give him the opportunity to do just that and will allow him to continue using the app

        elif str.lower(db)=='r':
            dd=booksSDK.readingROWID()
            print(' ')
            for i in dd:
                print(i)
            print("What book would you like to delete (type only the number)")
            dele=input()
            try:
                dele=int(dele)
                booksSDK.read2(dele)
            except ValueError:
                print('Please type only the number after which the book is ordered')
            except TypeError:
                print("\nPlease type only the number after which the book you want to delete is ordered")
                #If the user's input represents anything else than what's required

            else:
                print("Removing", booksSDK.read2(dele))
                booksSDK.delete(dele)
                print("If you're done removing, you can quit by typing 'Q' . If you want to remove another book, type again 'D'. ")
                db=input()
                #This represents the end of the removing process.

        elif str.lower(db)=='u':
            ed=booksSDK.readingROWID()
            print(' ')
            for i in ed:
                print(i)
            print("What book would you like to modify (type only the number)")
            up=input()
            try:
                up=int(up)
                booksSDK.read2(up)
            except ValueError:
                print("\nPlease type only the number after which the book is ordered")
            except TypeError:
                print("\nPlease type only the number after which the book you want to modify is ordered")
                #In case the number entered by the user doesn't corespond with the ones that can access the book, this will remind him about the right choice

            else:
                print("\nEnter a new title. If you want to keep the old title, press Enter.")
                newTitle=input()
                if newTitle=="":
                    newTitle=booksSDK.read2(up)[0]
                    print(f"The book will keep it's title ({newTitle})")
                #Will ask the user about the new title. If the user doesn't want to change the title, he can freely keep it.
                
                print("Enter a new number of pages. If you want to keep the old number of pages, press Enter")
                while True:
                    newPages=input()
                    if newPages=="":
                        dz=booksSDK.read2(up)
                        newPages=int(dz[dz.index('(')+1:dz.index('p')-1])
                        print(f"The book will keep it's old number of pages ({newPages})")
                        booksSDK.update(newTitle, newPages, up)
                        break
                        #Same goes with the number of pages

                    else:
                        try:
                            newPages=int(newPages)
                        except ValueError:
                            print("Please enter a number, as the number of pages represent a number.")
                        else:
                            booksSDK.update(newTitle, newPages, up)
                            break
                    #In case he types something else than an integer that will represent the number of pages

    else:
        print("\nHow many pages does your book have?")
        try:
            pages=int(input())
        except ValueError:
            print("\nPages represent a number.")
            #The number of pages of a book represents a number. In case the user types something else than that, this will remind him of this 

        else:
            finalAnswer=[]
            finalAnswer.append(answer)
            finalAnswer.append(pages)
            books.append(finalAnswer)
            print(f"\nAdded book: {answer}")
            #Will save the books the user types

            if len(books) %2 ==0:
                print("Notice: If you want remove a book, type 'R'. If you want to modify it, type 'M'. If you want to see your collection of saved books, type 'D' .")
                #Will inform the user that he can remove a book(but not every time so that it doesn't become irritating)

            print('\nAnything else?')
            if len(books) % 2!=0:
                print("If not, type 'Q' to quit.")
                #Will inform the user about what he should do, should he want to quit.

            answer=input()
            #Will give the user the opportunity to add more books