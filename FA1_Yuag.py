class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    @title.setter
    def title(self, new_title):
        self.set_title(new_title)

    @author.setter
    def author(self, new_author):
        self.set_author(new_author)

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


# Create the Book child class

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, new_number_of_pages):
        if new_number_of_pages > 0:
            self.__number_of_pages = new_number_of_pages
        else:
            print("The number of pages must be positive.")

    @number_of_pages.setter
    def number_of_pages(self, new_number_of_pages):
        self.set_number_of_pages(new_number_of_pages)

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    @property
    def issue_number(self):
        return self.__issue_number

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, new_issue_number):
        if new_issue_number > 0:
            self.__issue_number = new_issue_number
        else:
            print("The issue number must be positive.")

    @issue_number.setter
    def issue_number(self, new_issue_number):
        self.set_issue_number(new_issue_number)


# Create the objects

pub1 = Publication("Journal of Experimental Psychology",
                   "Ratchliff, R. & Van Dongen, H.")
pub2 = Publication("Science Today", "Dr. Maria Santos")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 350)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Various Authors", 150)


# Print the information

print("Publication Information:")
pub1.display_info()
print()
pub2.display_info()

print("\nBook Information:")
book1.display_info()
print()
book2.display_info()

print("\nMagazine Information:")
mag1.display_info()
print()
mag2.display_info() 

print("\nTesting Data Validation:")
book1.set_number_of_pages(-310)
mag1.set_issue_number(0)

print("Number of Pages:", book1.get_number_of_pages())
print("Issue Number:", mag1.get_issue_number())
