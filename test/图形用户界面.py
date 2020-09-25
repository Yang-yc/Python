import easygui as g

while 1:
    g.msgbox("害，欢迎进入第一个界面小游戏")
    msg = "请问你希望学习到什么知识"
    title = "小游戏互动"
    choice = ["谈恋爱", "编程", "demo", "琴棋书画"]
    choice = g.choicebox(msg, title, choice)
    g.msgbox("你的选择是:" + str(choice), "结果")
    msg = "你希望重新开始小游戏吗"
    msg = "请选择"
    if g.ccbox(msg, title):
        pass
    else:
        exit(0)


