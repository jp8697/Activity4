"""
This code was written by Julian Pascher, Georgii Terzii and Yahya Kaddoura
for Activity 4. 
The code aims to fulfill the all necessary parts of the Activity.
"""
# ​‌​‌​‌​‌​
class Polygon:
    #St​ep 1​‌​‌​‌​‌​
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_sides(self):
        return self.sides
    def set_sides(self, sides):
        self.sides = sides

    #St​ep​‌​‌​‌​‌​ ​‌​‌​‌​‌​2
    def __eq__(self,other):
        return self.name == other.name and self.sides == other.sides
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    #Ste​p ​‌​‌​‌​‌​3
    def __str__(self):
        return f"{self.name} has sidelenghts of {self.sides}"
    
    #Step ​‌​‌​‌​‌​4
    def circumference(self):
        sides = self.sides
        ter = 0
        for zi in range(len(sides)):
            cir += sides[zi]
        return ter

def demo():
    #Demonstrates results of Step 1 - 4 
    #Step1 
    #Creating first instance of the class ​‌​‌​‌​‌​
    polygon1 = Polygon(name = "Square", sides = [3.5,3.5,3.5,3.5])

    #Printing the Output of the Accessor Functions
    print("Polygon 1 name using accessor function: ", polygon1.get_name())
    print("Polygon 1 sides using accessor function: ", polygon1.get_sides())

    #Modifiying the name and side attribute of the the instane using the Mutator function
    polygon1.set_name("Rectangle")  
    polygon1.set_sides([4.0, 4.0, 4.5, 4.5])  

    #Printing the new output
    print("Polygon 1 name using mutator function: ", polygon1.get_name())
    print("Polygon 1 sides using mutator function: ", polygon1.get_sides())

    #Step2
    #Second instance so that we can use it in the __eq__ and __ne__ fucntion
    polygon2 = Polygon(name = "Rectangle", sides = [4.0 ,4.0, 4.5, 4.5])
    print(polygon1 == polygon2)
    print(polygon1 != polygon2)

    #Step 3
    #Printing the output of the __str__ function
    print(polygon1)

    #Step 4
    #Printing the output of the circumference fucntion
    print("The circumference is: ", polygon1.circumference())

def main():
    #Step ​‌​‌​‌​‌​5
    #Creation ​‌​‌​‌​‌​of instances
    triangle = Polygon("triangle", [4.0, 3.0, 6.0])
    square = Polygon("square", [4.0, 4.0, 4.0, 4.0])
    hexagon = Polygon("hexagon", [5.0, 8.0, 5.0, 4.0, 2.0, 6.0])
    
    #Printing the __str__ function
    print("The", triangle, "and the", square, "and the", hexagon)

    #Printing the circumference
    print("The triangle circumference is: ", triangle.circumference())
    print("The square circumference is: ", square.circumference())
    print("The hexagon circumference is: ", hexagon.circumference())

if __name__ == "__main__":
    main()

    