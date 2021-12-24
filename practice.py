class Cafe :
    def __init__(self) :
        self.name = input("어떤 음료를 주문하시겠습니까?")
        self.pearl = input("펄을 추가하시겠습니까? (네/아니오로만 답변이 가능합니다.)")
        self.sweet = input("당도는 어떻게 하시겠습니까?")
        self.ice = input("얼음은 얼마나 넣어드릴까요?")
    
    def pearl_order(self):
        if self.pearl == "네" :
            print("펄을 추가하셨습니다.")
        
        
        else :
            print("펄은 추가하지 않습니다.")

    def lastorder(self):
        print("{0}음료를 주문하셨습니다.당도는 {1}%입니다. 얼음은 {2} 넣어드리겠습니다.".format(self.name, self.sweet, self.ice))


firstorder = Cafe()
firstorder.lastorder()
firstorder.pearl_order()

print("송이는 천재다. ")
print ('안녕하세요 ')
print ('안녕하세요 ')
print ('안녕하세요 ')
print ('안녕하세요 ')
print ('안녕하세요 ')
print ('안녕하세요 ')
print ('안녕하세요 ')
print ('안녕하세요 ')
