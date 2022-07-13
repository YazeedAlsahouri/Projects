class Rectangle:
    all = []
    def __init__(self,width:float,height:float):
        assert width > 0 ,"Width is not greater than zero"
        assert height > 0 ,"Height is not greater than zero"
        self.width=width
        self.height=height
        Rectangle.all.append(self)
    def set_width(self,new_width):
        if new_width < 0 :
            raise Exception("The New Width is less than zero")
        else:
            self.width=new_width
    def set_height(self,new_height):
        if new_height < 0 :
            raise Exception("The New Height is less than zero")
        else:
            self.height=new_height
    def get_area(self):
        return f"Area={self.width*self.height}"
    def get_perimeter(self):
        return f"Perimeter={2 * self.width + 2 * self.height}"
    def get_diagonal(self):
        return f"Diagonal={(self.width ** 2 + self.height ** 2) **5}"
    def get_picture(self):
        for i in range(self.height):
            for j in range(self.width):
                print("*",end="")
            print()
    def __repr__(self):
        return f"{self.__class__.__name__}({self.width},{self.height})"
class Square:
    all = []
    def __init__(self,side:float):
        assert side > 0 ,"Side is not greater than zero"
        self.side=side
        Square.all.append(self)
    def set_side(self,new_side):
        if new_side < 0:
            raise Exception("The New Side is less than zero")
        else:
            self.side=new_side
    def get_area(self):
        return f"Area={self.side**2}"
    def get_perimeter(self):
        return f"Perimeter={2 * self.side + 2 * self.side}"
    def get_diagonal(self):
        return f"Diagonal={(self.side ** 2 + self.side ** 2) **5}"
    def get_picture(self):
        for i in range(self.side):
            for j in range(self.side):
                print("*",end="")
            print()  
    def __repr__(self):
        return f"{self.__class__.__name__}({self.side})"
