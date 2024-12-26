# class 定義一個型別，具有特性和功能
# class 名稱
# __init__ 建構子

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = None

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_sex(self, sex):
        self.sex = sex

    def get_sex(self):
        return self.sex

a = Person("John", 36)
print(a.get_name())
print(a.get_age())
a.set_sex("male")
print(a.get_sex())

# 主要運用場景，多物件，具有同屬性
class Light:
    def __init__(self, color, brand, height, width):
        self.color = color
        self.brand = brand
        self.height = height
        self.width = width

    def get_info(self):
        return f"color: {self.color}, brand: {self.brand}, height: {self.height}, width: {self.width}"

a = Light("red", "Philips", 10, 10)
print(a.get_info())
b = Light("blue", "Philips", 10, 20)
print(b.get_info())

# 繼承
class Led(Light):
    def __init__(self, color, brand, height, width, watt):
        # Initialize the parent class with its attributes
        super().__init__(color, brand, height, width)
        self.watt = watt  # Add new attribute for Led class

    def get_info(self):
        # Extend the parent class's `get_info` method
        base_info = super().get_info()
        return f"{base_info}, watt: {self.watt}"

c = Led("red", "Philips", 10, 10, "1000W")
print(c.get_info())


