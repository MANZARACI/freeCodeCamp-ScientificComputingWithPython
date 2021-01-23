class Category:
    def __init__(self, name):
        self.ledger=list()
        self.name=name
        self.balance=0
        self.spent=0

    def __str__(self):
        x=(30-len(self.name))//2
        write=x*"*"+self.name+x*"*"+"\n"

        for i in self.ledger:
            i["amount"]="{:.2f}".format(i["amount"])
            length1=len(i["description"][:23])
            length2=len(i["amount"])
            m=30 - (length1+length2)
            write+=i["description"][:23]+m*" "+i["amount"]+"\n"
        
        write+="Total: "+"{:.2f}".format(self.balance)

        return write

    def deposit(self, amount, description=""):
        self.balance+=amount
        a = {"amount":amount, "description":description}
        self.ledger.append(a)
    
    def withdraw(self,amount,description=""):
        if(self.check_funds(amount)):
            self.balance-=amount
            self.spent+=amount
            a = {"amount":-amount, "description":description}
            self.ledger.append(a)
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, another):
        if(self.check_funds(amount)):
            self.withdraw(amount,f"Transfer to {another.name}")
            another.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if(amount>self.balance):
            return False
        else:
            return True

def create_spend_chart(loc):
    total=0
    perOfCat = list()
    maxLen = len(loc[0].name)

    for i in loc:
        total+=i.spent
        if len(i.name)>maxLen:
            maxLen = len(i.name)

    for i in loc:
        per=(i.spent*100)/total
        per-=per%10
        perOfCat.append(per)
    
    write=""
    write+="Percentage spent by category\n"

    for i in range(100,-1,-10):
        write+=(3-len(str(i)))*" "+"{}|".format(i)
        for a in range(len(perOfCat)):
            if perOfCat[a]>=i:
                write+=" o "
            else:
                write+=3*" "
        write+=" \n"
    
    write+=4*" "+(3*len(perOfCat)+1)*"-"+"\n"

    for i in range(maxLen):
        write+=4*" "
        for a in range(len(perOfCat)):
            if i<len(loc[a].name):
                write+=" "+loc[a].name[i]+" "
            else:
                write+=3*" "
        if i!=maxLen-1:
            write+=" \n"
        else:
            write+=" "

    return write