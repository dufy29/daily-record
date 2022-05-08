# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/10/14 10:14
Author : Dufy
File : Car.py
验证对象之间的交互
e.g.
汽车中巡航速度设定时候，要调用点火类的方法
...
==============================================================================      
"""
from engine import Engine


class Car:
    Engine = Engine()


car = Car()
car.Engine.CruiseControl.set_cruise_speed(15)