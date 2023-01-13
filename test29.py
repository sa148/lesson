# output #
class HumanClass:
    def __init__(self):
      print('HumanClassのinit')
      self.hp = 100

class WizardClass(HumanClass):
    def __init__(self):
      super().__init__()
      self.mp = 50

    def output_info(self):
        print(f'現在のHPは{self.hp}で、'
              f'MPは{self.mp}です。')

Wizard = WizardClass()
Wizard.output_info()
