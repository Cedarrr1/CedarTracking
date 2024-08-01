#导入turtle包的所有内容
from turtle import *
#设置色彩模式是RGB
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

#初始化RGB颜色
r = 0
g = 0
b = 0
pencolor(r,g,b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r,g, b
    w = width()

    width(2 * 3.0 / 4.0)
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 *l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level+1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level +1)
    bk(l)
    lt(s)

    width(w)

speed('fastest')

draw_tree(l, 4)

done()