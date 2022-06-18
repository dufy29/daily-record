# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/6/18 19:16
File : logic_gate_demo.py

通过逻辑门模拟数字电路的程序
逻辑门 继承关系:
                    Logic Gate
                      /  \
                     /    \
          Binary Gate      UnaryGate
             / \               |
            /   \              |
          AND    OR           NOT
          2输入 +1输出        1输入+1输出

==============================================================================
"""


class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        """"
        注意， performGateLogic() 函数，我们并不会执行，
        具体实现将被包含在每一个被加入到继承体系中的 gate
        """
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):  # 继承
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def setNextPin(self, source):  # 设定端口为连接
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

    def getPinA(self):  # 两种获得方式，一种直接输入，另一种其它接入
        if self.pinA==None:
            return int(input("Enter Pin A input for gate" + self.getLabel() + "-->"))
        else:
            return self.pinA.getOutput()

    def getPinB(self):
        if self.pinB ==None:
            return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))
        else:
            return self.pinB.getOutput()


class UnaryGate(LogicGate):  # 继承
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

    def getPin(self):
        if self.pin ==None:
            return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))
        else:
            return self.pin.getOutput()


class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPin()
        if a==1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(fgate)  # 设定输入来自于fgate



if __name__ == "__main__":
    g1 =AndGate("g1")
    g2 =AndGate("g2")

    g3 = OrGate("g3")
    g4 = NotGate("g4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())
