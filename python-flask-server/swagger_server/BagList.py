

class BagList:
    def __init__(self):
        self.count  = 0
        self.data = {}
        self.locations = ["Mid_3", "Front_1", "Rear_2","Front_4","Rear_1"]

    def add(self,bagId, weight):
        location = "Mid_303"
        bag = {'color':bagId, 'location':self.locations[self.count]}
        self.count +=1
        self.data[bagId]  = bag
    
    def remove(self,bagId):
        if self.data.get(bagId) : del self.data[bagId]

    def get(self,bagId):
        if self.data.get(bagId):
            bag  = self.data[bagId]
            print (bag)
            return bag
        else:
            return {}

