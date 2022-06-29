class triangle_area:
    def __init__(self, base, height, is_right):
        self.base = 0
        self.height = 0
        self.is_right = False
        

    def hypotenuse(self, base, height, is_right):
        if (self.is_right == True):
            hypo = ((self.base**2) + (self.height**2))
            return hypo
        else:
            print("The instance you are trying to use is not a right triangle.")
            
    def area(self, base, height):
        if(self.base > 0 and self.height > 0):
            area = ((0.5)*self.base*self.height)
            return area
        else:
            raise ValueError('You must enter a positive integer that is greater than zero.')
        
a = triangle_area(3,4, True)
b = triangle_area(4, 10, False)
        