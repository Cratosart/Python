class Road:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        s = 25
        t = 5
        itog = (lenght * width * s * t)/1000
        print(f"Масса асфальта для покрытия дороги {int(itog)} тонн")


a = Road(5, 400)