class Encyription:
    def __init__(self):
        self.message = input("What is your message?:")
        while True:
            self.key = input("Whick key do you want to use (int only)?:")
            if self.key.lstrip("-").isdigit() == False:
                print("Your key must be an integer. Please enter again.")
            else:
                self.key = int(self.key)
                self.working = list(self.message)
                break
        self.main()

    def main(self):
        self.cypher = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","q","r","s","ş",
                       "t","u","ü","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"," ",",",".","?",":","!",
                       "&","*","''","+"]
        for i in range(len(self.working)):
            self.index = self.cypher.index(self.working[i]) + self.key
            self.index = self.index % 52
            self.working[i] = self.cypher[self.index]
        self.encripted = "".join(self.working)
        print(self.encripted)
        input("Press enter to exit")
Encyription()