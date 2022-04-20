import tkinter
from tkinter import *
from tkinter import ttk


# 互蕴含
def mutual_implication(s):
    s = s.replace("<->", "==")
    i = -1
    while i < len(s) - 2:
        i += 1
        if s[i] == '=' and s[i + 1] == '=':
            j = i - 1
            cnt = 0
            while j >= 0:
                if s[j] == ")":
                    cnt += 1
                if s[j] == "(":
                    cnt -= 1
                if (s[j] == '=' and s[j + 1] == '=' and cnt == 0) or cnt == -1:
                    break
                j -= 1
            cnt = 0
            k = i + 2
            while k < len(s) - 2:
                if s[k] == "(":
                    cnt += 1
                if s[k] == ")":
                    cnt -= 1
                if (s[k] == '=' and s[k + 1] == '=' and cnt == 0) or cnt == -1:
                    break
                k += 1
            l = list(s)
            if k == len(s) - 2:
                k += 1
            l.insert(k + 1, ")")
            l.insert(i + 2, "(")
            l.insert(i, ")")
            l.insert(j + 1, "(")
            s = "".join(l)
            i += 2
    return s


# 蕴含
def implication(s):
    s = s.replace("->", "<=")
    return s


# not
def not_del(s):
    s = s.replace("-", " not ")
    i = -1
    while i < len(s) - 3:
        i += 1
        if s[i] == 'n' and s[i + 1] == 'o' and s[i + 2] == 't':
            b, b2 = False, False
            j = i + 3
            while j < len(s):
                if s[j] == "(":
                    b = True
                    break
                if s[j] != " ":
                    break
                j += 1
            if b:
                k = j
                cnt = 1
                while k < len(s):
                    if s[k] == "(":
                        cnt += 1
                    if s[k] == ")":
                        cnt -= 1
                    if cnt == 1:
                        break
                    k += 1
                l = list(s)
                l.insert(k + 1, ")")
                l.insert(i - 1, "(")
                s = "".join(l)
                i += 1
                continue
            j = i - 1
            while j >= 0:
                if s[j] == '(':
                    b = True
                    break
                if s[j] != ' ' and s[j] != '(':
                    b = False
                    break
                j -= 1
            k = i + 3
            b3 = False
            while k < len(s):
                if s[k] != ' ':
                    b3 = True
                if b3 and (not (('Z' >= s[k] >= 'A') or ('z' >= s[k] >= 'a'))):
                    break
                k += 1
            j = k
            while j < len(s):
                if s[j] == ')':
                    b2 = True
                    break
                if s[j] != ' ' and s[j] != ')':
                    b2 = False
                    break
                j += 1
            if not (b and b2):
                l = list(s)
                l.insert(i - 1, "(")
                l.insert(k + 1, ")")
                s = "".join(l)
                i += 1
    return s


# 化简
def simplify(s):
    s.join("    ")
    s = mutual_implication(s)
    s = implication(s)
    s = not_del(s)
    return s


if __name__ == '__main__':
    root = Tk()
    root.title("离散数学计算器")
    ttk.Label(root, text="                         离散数学计算器").grid(column=0, row=0, sticky='W', columnspan=4)
    tab = ttk.Notebook(root)
    tab1 = ttk.Frame(tab)
    tab.add(tab1, text="求值")
    tab2 = ttk.Frame(tab)
    tab.add(tab2, text="替换")
    tab3 = ttk.Frame(tab)
    tab.add(tab3, text="对偶")
    tab4 = ttk.Frame(tab)
    tab.add(tab4, text="等价")
    tab5 = ttk.Frame(tab)
    tab.add(tab5, text="真值表")
    tab6 = ttk.Frame(tab)
    tab.add(tab6, text="范式")
    tab.grid(column=0, row=100, sticky='W', columnspan=5)
    # ----------命题变元---------- #
    ttk.Label(root, text=" 命题变元").grid(column=0, row=1, sticky='W')
    ttk.Label(root, text="  值").grid(column=1, row=1, sticky='W')
    e = []
    e2 = []
    entry = tkinter.Entry(root, width=10)
    entry.grid(column=0, row=3, sticky='W')
    entry2 = tkinter.Entry(root, width=10)
    entry2.grid(column=1, row=3, sticky='W', padx=10, pady=3)
    e.append(entry)
    e2.append(entry2)

    ttk.Label(root, text="命题变元个数").grid(column=0, row=1, sticky='W')
    ttk.Label(root, text="   命题变元").grid(column=0, row=2, sticky='W')
    ttk.Label(root, text="          值").grid(column=1, row=2, sticky='W')
    num = tkinter.StringVar()
    num.set("1")
    ttk.Label(root, textvariable=num).grid(column=2, row=1, sticky='W')

    def plus():
        number = int(num.get()) + 1
        if number == 11:
            number = 10
        else:
            en = tkinter.Entry(root, width=10)
            en.grid(column=0, row=number + 2, sticky='W')
            en2 = tkinter.Entry(root, width=10)
            en2.grid(column=1, row=number + 2, sticky='W', padx=10, pady=3)
            e.append(en)
            e2.append(en2)
        num.set(str(number))

    def minus():
        number = int(num.get()) - 1
        if number == 0:
            number = 1
        else:
            en = e.pop()
            en.destroy()
            en2 = e2.pop()
            en2.destroy()
        num.set(str(number))

    ttk.Button(root, text="+", command=plus).grid(column=1, row=1, sticky='W')
    ttk.Button(root, text="-", command=minus).grid(column=3, row=1, sticky='W')
    # ----------Tab1(求值)---------- #
    ttk.Label(tab1, text="公式:").grid(column=0, row=0, sticky='W')
    t1 = tkinter.Entry(tab1, width=40)
    t1.grid(column=0, row=1, sticky='W', columnspan=3)
    val1 = tkinter.StringVar()

    def evaluate():
        name_input = [i.get() for i in e]
        val_input = [int(i.get()) for i in e2]
        formula = t1.get()
        n = int(num.get())
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(name_input[i]) < len(name_input[j]):
                    name_input[i], name_input[j] = name_input[j], name_input[i]
                    val_input[i], val_input[j] = val_input[j], val_input[i]
        formula = simplify(formula)
        for i in range(n):
            formula = formula.replace(name_input[i], "val_input[{}]".format(i))
        val1.set(str(int(eval(formula))))

    ttk.Button(tab1, text="求值", command=evaluate).grid(column=0, row=2, sticky='W')
    ttk.Label(tab1, text="值为:").grid(column=1, row=2, sticky='W')
    ttk.Label(tab1, textvariable=val1).grid(column=2, row=2, sticky='W')
    # ----------Tab2(替换)---------- #
    ttk.Label(tab2, text="原公式:", width=50).grid(column=0, row=0, columnspan=2)
    ttk.Label(tab2, text="替换式:", width=25).grid(column=0, row=2)
    ttk.Label(tab2, text="目标式:", width=25).grid(column=1, row=2)
    t21 = tkinter.Entry(tab2, width=40)
    t21.grid(column=0, row=1, sticky='W', columnspan=2)
    t22 = tkinter.Entry(tab2, width=15)
    t22.grid(column=0, row=3, sticky='W')
    t23 = tkinter.Entry(tab2, width=15)
    t23.grid(column=1, row=3, sticky='W')
    val2 = tkinter.StringVar()

    def substitute():
        val2.set("替换式为:" + t21.get().replace(t22.get(), t23.get()))

    ttk.Button(tab2, text="求替换式", command=substitute).grid(column=0, row=4, sticky='W')
    ttk.Label(tab2, textvariable=val2).grid(column=1, row=4, sticky='W')
    # ----------Tab3(对偶)---------- #
    ttk.Label(tab3, text="公式:", width=50).grid(column=0, row=0, columnspan=3)
    t3 = tkinter.Entry(tab3, width=40)
    t3.grid(column=0, row=1, sticky='W', columnspan=3)
    val3 = tkinter.StringVar()

    def antithesis():
        s = t3.get()
        s = s.replace("1", "$")
        s = s.replace("0", "1")
        s = s.replace("$", "0")
        s = s.replace("|", "$")
        s = s.replace("&", "|")
        s = s.replace("$", "&")
        val3.set(s)

    ttk.Button(tab3, text="求对偶式", command=antithesis).grid(column=0, row=2, sticky='W')
    ttk.Label(tab3, text="对偶式为:").grid(column=1, row=2, sticky='W')
    ttk.Label(tab3, textvariable=val3).grid(column=2, row=2, sticky='W')
    # ----------Tab4(等价)---------- #
    ttk.Label(tab4, text="公式1:", width=50).grid(column=0, row=0, columnspan=3)
    ttk.Label(tab4, text="公式2:", width=50).grid(column=0, row=2, columnspan=3)
    t41 = tkinter.Entry(tab4, width=40)
    t41.grid(column=0, row=1, sticky='W', columnspan=3)
    t42 = tkinter.Entry(tab4, width=40)
    t42.grid(column=0, row=3, sticky='W', columnspan=3)
    val4 = tkinter.StringVar()

    def equal():
        n = int(num.get())
        s = [i.get() for i in e]
        val = [0 for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(s[i]) < len(s[j]):
                    s[i], s[j] = s[j], s[i]
        s1 = simplify(t41.get())
        s2 = simplify(t42.get())
        for i in range(n):
            if (s[i] in s1) and (s[i] in s2):
                s1 = s1.replace(s[i], "val[{}]".format(i))
                s2 = s2.replace(s[i], "val[{}]".format(i))
            else:
                val4.set("包含的变元种类不一样")
                return
        for i in range(1 << n):
            m = i
            for j in range(n):
                val[j] = m % 2
                m = int(m / 2)
            if eval(s1) != eval(s2):
                val4.set("不等价")
                return
        val4.set("等价")

    ttk.Button(tab4, text="比较", command=equal).grid(column=0, row=4, sticky='W')
    ttk.Label(tab4, text="结果为:").grid(column=1, row=4, sticky='W')
    ttk.Label(tab4, textvariable=val4).grid(column=2, row=4, sticky='W')
    # ----------Tab5(真值表)---------- #
    ttk.Label(tab5, text="公式:", width=50).grid(column=0, row=0, columnspan=3)
    t5 = tkinter.Entry(tab5, width=40)
    t5.grid(column=0, row=1, sticky='W', columnspan=3)
    val5 = tkinter.StringVar()

    def table():
        n = int(num.get())
        s = [i.get() for i in e]
        val = [0 for _ in range(n)]
        ans = ""
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(s[i]) < len(s[j]):
                    s[i], s[j] = s[j], s[i]
        s1 = t5.get()
        for i in range(n):
            ans += s[i] + " "
        ans += s1 + "\n"
        s1 = simplify(s1)
        for i in range(n):
            s1 = s1.replace(s[i], "val[{}]".format(i))
        t, f = True, True
        for i in range(1 << n):
            m = i
            for j in range(n):
                val[-1 - j] = m % 2
                m = int(m / 2)
            for j in range(n):
                ans += str(val[j]) + " "
            res = int(eval(s1))
            if res == 1:
                f = False
            if res == 0:
                t = False
            ans += str(res) + "\n"
        if f:
            ans += "永假式" + "\n"
        if t:
            ans += "永真式" + "\n"
        if (not f) and (not t):
            ans += "可满足式" + "\n"
        val5.set(ans)

    ttk.Button(tab5, text="求真值表", command=table).grid(column=0, row=3, sticky='W')
    ttk.Label(tab5, text="结果为:").grid(column=0, row=4, sticky='W')
    ttk.Label(tab5, textvariable=val5).grid(column=0, row=5, sticky='W')
    # ----------Tab6(范式)---------- #
    ttk.Label(tab6, text="公式:", width=50).grid(column=0, row=0, columnspan=3)
    t6 = tkinter.Entry(tab6, width=40)
    t6.grid(column=0, row=1, sticky='W', columnspan=3)
    val6 = tkinter.StringVar()

    def xi():
        normal_form(1)

    def he():
        normal_form(0)

    def normal_form(op):
        n = int(num.get())
        s = [i.get() for i in e]
        val = [0 for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(s[i]) < len(s[j]):
                    s[i], s[j] = s[j], s[i]
        s1 = simplify(t6.get())
        for i in range(n):
            s1 = s1.replace(s[i], "val[{}]".format(i))
        result = ""
        b = False
        if op == 0:
            for i in range(1 << n):
                m = i
                b2 = False
                for j in range(n):
                    val[-1 - j] = m % 2
                    m = int(m / 2)
                if int(eval(s1)) == 0:
                    if b:
                        result = result + "&"
                    b = True
                    result = result + "("
                    for k in range(n):
                        if b2:
                            result = result + "|"
                        b2 = True
                        if val[k] == 0:
                            result = result + s[k]
                        else:
                            result = result + "-" + s[k]
                    result = result + ")"
        else:
            for i in range(1 << n):
                m = i
                b2 = False
                for j in range(n):
                    val[-1 - j] = m % 2
                    m = int(m / 2)
                if int(eval(s1)) == 1:
                    if b:
                        result = result + "|"
                    b = True
                    result = result + "("
                    for k in range(n):
                        if b2:
                            result = result + "&"
                        b2 = True
                        if val[k] == 1:
                            result = result + s[k]
                        else:
                            result = result + "-" + s[k]
                    result = result + ")"
        val6.set(result)

    ttk.Button(tab6, text="求合取范式", command=he).grid(column=0, row=3, sticky='W')
    ttk.Button(tab6, text="求析取范式", command=xi).grid(column=1, row=3, sticky='W')
    ttk.Label(tab6, text="结果为:").grid(column=0, row=4, sticky='W')
    ttk.Label(tab6, textvariable=val6).grid(column=0, row=5, sticky='W')
    # ----------结束---------- #
    root.mainloop()
