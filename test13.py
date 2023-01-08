# 一番シンプルなクラス #
class BodyCondiction:
    def bmi_calc(self):
        print('あいうえお')

# インスタンス代入 #
bc = BodyCondiction()
bc.bmi_calc()

# イニシャライザ実行確認 #
class BodyCondiction:
    def __init__(self):
        print('初期化')

    def bmi_calc(self):
        print('あいうえお')

bc = BodyCondiction()

# イニシャライザ中に値を設定 # 
class BodyCondiction:
    def __init__(self, arg_weight, arg_height):
        self.weight = arg_weight
        self.height = arg_height
    
    def bmi_calc(self):
        m_height = self.height / 100
        bmi = self.weight / m_height / m_height
        print(bmi)

bc = BodyCondiction(55, 150)
bc.bmi_calc()
