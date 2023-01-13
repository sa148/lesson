# 継承 #
# 基底クラス #
class HumanClass:
    def defebd(self):
      print('防御しました')

# 派生クラス #
class WizardClass(HumanClass):
    pass

wizard = WizardClass()
wizard.defebd()

# イニシャライザあり #
class HumanClass:
    def __init__(self):
        print('HumanClassのinit')
        self.hp = 100

class WizardClass(HumanClass):
    pass

wizard = WizardClass()
print(wizard.hp)
