class Fan:
    #attribute(properties) and behaviour(functionality)
    #class vaiable
    cname = 'bajaj'

    # price and color are instance variable
    def __init__(self,p,c):
        self.price = p
        self.color = c

    #self represents current object
    def fanInfo(self):
        print("My properties are ",self.price,self.cname,self.color)

    def getOn(self):
        print("Fan is switched on.")

#a = 10
MyFan1 = Fan(500,'black')
MyFan2 = Fan(2000,'white')
MyFan1.fanInfo()
MyFan2.fanInfo()


