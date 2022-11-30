from pickle import TRUE
import datetime

#namespace Christmas_Songs:

class heart:
    heart = {"tears": True}

class Last_Christmas:

    def __init__(self, fst_time = True, this_year = datetime.date.today(), last_year = datetime.date((datetime.date.today().year - 1), datetime.date.today().month, datetime.date.today().day)):
        self.this_year = this_year
        self.last_year = last_year
        print(f"\nLast Christmas: {last_year}")
        self.fst_time = fst_time
        self.song = {"makes money": True}
        self.my_heart = heart()
        if self.last_year.month == 12 and self.last_year.day == 25:            
            self.Give_Heart("you")
        if self.this_year:
            print(f"\nThis Year: {self.this_year}")
            if self.fst_time == True:
                self.Give_Heart("someone special")
            elif self.fst_time == False:
                lucrative = input(f"\nDoes the song still make money?\n> ")
                if 'y' in lucrative.lower():
                    self.song["makes money"] = True
                    return print("\n\n*****************************\nLet's do it again!\n")
                else:
                    self.song["makes money"] = False
                    return print("It's not making money anymore?\nPerhaps it is now time to stop playing it at Christmas time...")
                    
    
    def Give_Heart(self,recipient):        
        pst_ftr = " gave"
        if recipient.lower() == "you":
            while self.last_year.day != 26 or self.last_year.month != 12:
                ''
                self.last_year = datetime.date(self.last_year.year, 12, 26)
                #simulate the passing of 1 day
            if self.fst_time == True:
                print(f"\nI{pst_ftr} {recipient} {self.my_heart}")
                print(f"\nBut: {self.last_year}\n")
            if self.fst_time == False:
                pst_ftr = "'ll give"
                print(f"\nI{pst_ftr} {recipient} {self.my_heart}")
                print(f"\nAnd: {self.last_year}\n")
            self.Give_Away(pst_ftr)

        if recipient.lower() == "someone special":
            pst_ftr = "'ll give"
            print(f"\nI{pst_ftr} it to {recipient}")
            self.my_heart.heart['tears'] = False
            print(f"Status of heart: {self.my_heart.heart}")
            print(f"\nThat's how the song goes... but in reality:\n")
            lucrative = input(f"\nDoes the song still make money?\n> ")
            if 'y' in lucrative.lower():
                self.song["makes money"] = True
                return print("\n\n*****************************\nLet's do it again!\n")
            else:
                return print("\n\nIt's not making money anymore?\nPerhaps it is now time to stop playing it at Christmas time...\n\n")


    def Give_Away(self, pst_ftr = " gave"):
        self.my_heart.heart['tears'] = True
        print(f"You{pst_ftr} it away\nStatus of heart: {self.my_heart.heart}")

if __name__ == "__main__":
    print("This printed within Funny_Christmas_Songs.py")
    this_year = datetime.date(datetime.date.today().year, 12, 25)
    last_year = datetime.date(datetime.date.today().year -1, 12, 25)
    Wham = Last_Christmas(True, this_year, last_year)
    while Wham.song['makes money'] == True:
        last_year = (this_year)
        this_year = datetime.date(this_year.year + 1, 12, 25)
        Wham = Last_Christmas(False, this_year, last_year)