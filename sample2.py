# クラス #
class BodyCondiction:
    def bmi_calc(self):
      print('体重')

# インスタンス代入 #
bc = BodyCondiction()
bc.bmi_calc()

# イニシャライザ実行確認 #
class BodyCondiction:
    def __init__(self):
        print('初期化')

    def bmi_calc(self):

bc = BodyCondiction()