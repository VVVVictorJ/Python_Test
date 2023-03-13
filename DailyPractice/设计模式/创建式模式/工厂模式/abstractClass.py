from abc import ABCMeta, abstractclassmethod


#抽象类一定会提供至少一个被@abstractmethod装饰的方法。抽象类的特点是不能被实例化。
class Test(metaclass=ABCMeta):

    @abstractclassmethod
    def xxx():
        ...


class Payment(metaclass=ABCMeta):
    '''接口类，抽象基类'''

    @abstractclassmethod
    def pay(self, money):
        pass


class WeiChatPay(Payment):
    '''子类'''

    def pay(self, money):
        print('微信支付{}元'.format(money))


class Alipay(Payment):
    '''子类'''

    def paying(self, money):
        print('支付宝支付{}元'.format(money))


def pay(pay_obj, money):
    pay_obj.pay(money)

# WeichatPay 是正常使用的，因为它提供了pay方法
p = WeiChatPay()
pay(p, 123)

#Alipay 类实例化的时候就会报错
#TypeError: Can't instantiate abstract class Alipay with abstract method pay
p = Alipay()
pay(p, 123)
