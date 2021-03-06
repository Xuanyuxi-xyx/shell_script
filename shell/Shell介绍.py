# -*- coding: utf-8 -*-
# @Time    : 1/18/2022 4:28 PM
# @Author  : xuanyuxi
# @Email   : xuanyuxi@360.cn
# @File    : Shell介绍.py
# @Software: PyCharm

"""
Shell 是一个用C语言编写的程序，是用户和Linux的桥梁，如何理解 ‘桥梁’？
    对于图形界面，用户点击某个图标就能启动某个应用程序；对于命令行，用户输入某个程序的名字，就可以启动某个应用程序，
    两者的基本过程是类似的，都需要查找程序在硬盘上的安装位置，然后将他们加载到内存中运行。

    通俗的说：图形化界面和命令行的目的是一样的，都是让用户控制计算机，然而真正控制计算机硬件(CPU、硬盘)的只有操作系统内核，
    图形化界面和命令行就是用户和内核之间的一个桥梁。

    但由于考虑到操作系统安全、复杂等因素，不允许用户直接操作内核，需要再开发一个程序，让用户使用这个程序来达到控制计算机的目的。
    该程序的作用就是：接收用户的操作，进行一些处理，然后传递给内核。

    用户界面和命令行就是这个另外开发的程序，在Linux下，这个命令行程序叫做Shell

    因此，Shell的本质为：一个应用程序，连接了用户和Linux内核，让用户更安全、高效的使用Linux内核

Shell如何连接用户和内核？
    通过调用内核提供的函数

Shell支持编程
    Shell也是一种编程语言，它的编译器（解释器）就是Shell这个程序

Shell是一种脚本语言
    编写完源码后不用编译，直接运行即可

"""