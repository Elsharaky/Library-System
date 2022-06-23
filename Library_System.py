class Book:
    def __init__(self,id,name,quantity) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity
class User:
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name
class BackEnd:
    def __init__(self) -> None:
        self.data_base = {}
        self.query = {}
        self.users = {}
    def add_book(self,book):
        self.data_base.setdefault(book.name,[book.id,0,[]])
        self.data_base[book.name][1] += book.quantity

        pre = ''
        for i in book.name:
            pre += i
            self.query.setdefault(pre,[])
            self.query[pre].append(book.name)
    def search(self,pref):
        if len(self.query[pref]):
            for i in self.query[pref]:
                print(f'\tBook: {i}\tid: {self.data_base[i][0]}\tcopies: {self.data_base[i][1]}\ttotal borrowed: {len(self.data_base[i][2])}')
        else:
            print('There is no book begins with this prefix!')
    def print_books(self):
        if len(self.data_base):
            for i in self.data_base:
                print(f'\tBook: {i}\tid: {self.data_base[i][0]}\tcopies: {self.data_base[i][1]}\ttotal borrowed: {len(self.data_base[i][2])}')
        else:
            print("There is no books at the moment!")
    def add_user(self,user):
        self.users.setdefault(user.name,[user.id,[]])
    def borrow_book(self,user_name,book_name):
        self.users[user_name][1].append(book_name)
        self.data_base[book_name][2].append(user_name)
    def return_book(self,user_name,book_name):
        self.users[user_name][1].remove(book_name)
        self.data_base[book_name][2].remove(user_name)
    def print_users(self):
        if len(self.users):
            for i in self.users:
                print(f'User: {i}\tid: {self.users[i][0]}')
                if self.users[i][1]:
                    print("Borrowed Books:")
                    for j in self.users[i][1]:
                        print(f'\tBook: {j}\tid: {self.data_base[j][0]}\tcopies: {self.data_base[j][1]}\ttotal borrowed: {len(self.data_base[j][2])}')
        else:
            print("There are no users at the moment!")
class FrontEnd:
    def __init__(self) -> None:
        pass
    def show_menu(self):
        func = BackEnd()
        self.choices = ["Add book","Print all books","Search for a book","Add user","Borrow book","Return book","Print all users borrowed a book","print all users","Exit from the program"]
        while 1:
            print("Welcome to our library system!")
            for i , v  in enumerate(self.choices):
                print(f'{i+1} {v}')
            main_choice = input('Enter your choice: ')
            if main_choice == '1':
                id = input('Enter book ID: ')
                name = input('Enter book Name: ')
                quantity = int(input('Enter Number of copies: '))
                book = Book(id,name,quantity)
                func.add_book(book)
            elif main_choice == '2':
                func.print_books()
            elif main_choice == '3':
                pref = input("Enter name of the book or it's prefix: ")
                func.search(pref)
            elif main_choice == '4':
                id = input('Enter user id: ')
                name = input('Enter user name: ')
                user = User(id,name)
                func.add_user(user)
            elif main_choice == '5':
                user_name = input("Enter user name: ")
                book_name = input("Enter book name: ")
                if user_name not in func.users:
                    print("Invalid user!")
                    continue
                if book_name not in func.data_base:
                    print("Invalid book!")
                    continue
                if len(func.data_base[book_name][2]) < func.data_base[book_name][1]:
                    func.borrow_book(user_name,book_name)
                else:
                    print("Invalid borrow!")
            elif main_choice == '6':
                user_name = input("Enter user name: ")
                book_name = input("Enter book name: ")
                if book_name in func.users.get(user_name)[1]:
                    func.return_book(user_name,book_name)
                else:
                    print("Invalid Returning!")
            elif main_choice == '7':
                book_name = input("Enter book name: ")
                print(*func.data_base[book_name][2])
            elif main_choice == '8':
                func.print_users()
            elif main_choice == '9':
                break
            else:
                print("Invalid choice!")

fe = FrontEnd()
fe.show_menu()