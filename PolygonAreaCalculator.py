class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if (self.width>50) or (self.height>50):
            return "Too big for picture."
        else:
            self.picture=""
            for a in range(self.height):
                self.picture+=self.width*"*"+"\n"
            return self.picture
    
    def get_amount_inside(self,shape):
        return (self.width//shape.width)*(self.height//shape.height)
    
    def set_width(self,number):
        self.width=number
    
    def set_height(self,number):
        self.height=number
    
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)

    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self,number):
        self.width=number
        self.height=number
    
    def set_width(self,number):
        self.width=number
        self.height=number
    
    def set_height(self,number):
        self.width=number
        self.height=number