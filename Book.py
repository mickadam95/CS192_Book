class Books:

    def _init_(self):
        self.pageNum = 0
        self.hardcoverStr = "no"
        self.author = " "
        self.title = " "

    def Publish(self):
        self.pageNum = input("How many pages is the book (Including covers):")
        self.hardcoverStr = input("Is the book hardcover?" )
        if self.hardcoverStr.lower() == "yes" or self.hardcoverStr.lower() == "y":
            self.hardcover = true
        self.author = input("Please enter the author name: ")
        self.title = input("Please enter the book title: ")

    def SetTitle(self):
        self.title = input("Please enter the book title: ")
    def SetCoverType(self):
            self.hardcoverStr = input("Is the book hardcover?" )
            if self.hardcoverStr.lower() == "yes" or self.hardcoverStr.lower() == "y":
                self.hardcover = true
    def SetPageCount(self):
        self.pageNum = input("How many pages is the book (Including covers):")
    def SetAuthor(self):
        self.author = input("Please enter the author name: ")


    def GetTitle(self):
        print("The book's title is: ", self.title)
    def GetAuthor(self):
        print("The book's author is: ", self.author)
    def GetPageCount(self):
        print("The page count is: ", self.pageNum)

Books()

def main():

    library = [Books() for i in range(5)]
    for i in range(5):
        library[i].Publish()

    titleS = input("What book are you looking for?")
    for i in range(5):
        if library[i].title == titleS:
            library[i].GetTitle()
            library[i].GetAuthor()
            library[i].GetPageCount()
        if i == 4 and library[i].title != titleS:
            print("We do not have your book")
    
main()
