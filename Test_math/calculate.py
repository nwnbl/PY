class Math: 
    def __init__(self, a, b):  # 初始化方法，a和b两个参数
        self.a = int(a)  # 强制转化成int型
        self.b = int(b)  # 强制转化成int型


    def add(self):  # 定义加法运算
        return self.a+self.b
