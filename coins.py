import random

class Coin:
    def __init__(self, rare=False, heads=True, clean=True, **kwargs): #**kwargs will pack down all the unpacked keyword arguments below into a dictionary called kwargs
        for key,value in kwargs.items():
            setattr(self,key,value) #this loops over the kwargs, and stores the keys and values of the dcitionary
                                    #setattr does all the self.original_value=1 etc. 
    
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads 

        if self.is_rare:
            self.value=self.original_value *1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
    def rust(self): #making a coin rust 
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self): #coin flip
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    
    def __del__(self): #del is the deconstructor; this is for the function of spending the coin
        print("Coin spent") #coin1 or whatever will no longer be defined after this function
    def __str__(self): #to format the name of the coin when printed out below 
        if self.original_value>=1:
            return "{} coin".format(int(self.original_value))
        else:
            return "{}p coin".format(int(self.original_value*100))

class one_pence(Coin): 
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass":3.56 }
        super().__init__(**data)
class two_pence(Coin): 
    def __init__(self):
        data = {
            "original_value": 0.02,
            "clean_colour": "silver",
            "rusty_colour": None, #must override the rust behaviour from parent class since silver doesn't rust
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass":3.56 }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour #polymorphism example since same function name has different forms
        def clean(self):
            self.colour =self.clean_colour 

class Pound(Coin): #Pound  class will inherit from its parent class
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass":7.12 }
        super().__init__(**data)
        #unpacking the data into keyword arguments; will pack this down in the parent  
            
coins = [one_pence(), two_pence(), Pound()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    string = "{} - Colour: {}, Value: {}, Diameter {}, Thickness: {}, Edges: {}, Mass: {}".format(*arguments)
    #inputting *arguments in format() rather than individual arguments will do the same thing
    print(string)
   

