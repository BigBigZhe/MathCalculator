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


# not加括号
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
    s = mutual_implication(s)
    s = implication(s)
    s = not_del(s)
    return s


# 求值
def evaluate():
    num = int(input("请输入命题变元个数:"))
    print("输入{0}行，每行的格式为:命题变元/值".format(num))
    name_input = []
    val_input = []
    for i in range(num):
        a, b = input("{}:".format(i + 1)).split("/")
        name_input.append(a)
        val_input.append(int(b))
    for i in range(num - 1):
        for j in range(i + 1, num):
            if len(name_input[i]) < len(name_input[j]):
                name_input[i], name_input[j] = name_input[j], name_input[i]
                val_input[i], val_input[j] = val_input[j], val_input[i]
    formula = input()
    formula.join("    ")
    formula = simplify(formula)
    for i in range(num):
        formula = formula.replace(name_input[i], "val_input[{}]".format(i))
    print("所求值为:")
    print(eval(formula))
    print("")


# 替换
def substitute():
    s, s2 = input("请输入原式子:").split("[")
    s2, s3 = s2.split("/")
    l1 = list(s2)
    l2 = list(s3)
    l2.pop()
    s2 = "".join(l1)
    s3 = "".join(l2)
    print(s.replace(s2, s3))


# 对偶
def antithesis():
    s = input("请输入原式子:")
    s = s.replace("1", "$")
    s = s.replace("0", "1")
    s = s.replace("$", "0")
    s = s.replace("|", "$")
    s = s.replace("&", "|")
    s = s.replace("$", "&")
    print("其对偶式为:")
    print(s)


# 等价式
def equal():
    num = int(input("输入变元个数:"))
    print("请输入{}个变元名，用;隔开".format(num))
    s = input().split(";")
    val = [0 for _ in range(num)]
    for i in range(num - 1):
        for j in range(i + 1, num):
            if len(s[i]) < len(s[j]):
                s[i], s[j] = s[j], s[i]
    print("请输入两行，一行一个式子，判断他们是否等价")
    s1 = input()
    s2 = input()
    s1 = simplify(s1)
    s2 = simplify(s2)
    for i in range(num):
        if (s[i] in s1) and (s[i] in s2):
            s1 = s1.replace(s[i], "val[{}]".format(i))
            s2 = s2.replace(s[i], "val[{}]".format(i))
        else:
            print("包含的变元种类不一样")
            return
    for i in range(1 << num):
        m = i
        for j in range(num):
            val[j] = m % 2
            m = int(m / 2)
        if eval(s1) != eval(s2):
            print("不等价")
            return
    print("等价")


# 真值表
def table():
    num = int(input("输入变元个数:"))
    print("请输入{}个变元名，用;隔开".format(num))
    s = input().split(";")
    val = [0 for _ in range(num)]
    for i in range(num - 1):
        for j in range(i + 1, num):
            if len(s[i]) < len(s[j]):
                s[i], s[j] = s[j], s[i]
    print("请输入一行一个式子，输出他的真值表")
    s1 = input()
    for i in range(num):
        print(s[i], end=" ")
    print(s1)
    s1 = simplify(s1)
    for i in range(num):
        s1 = s1.replace(s[i], "val[{}]".format(i))
    for i in range(1 << num):
        m = i
        for j in range(num):
            val[-1 - j] = m % 2
            m = int(m / 2)
        for j in range(num):
            print(val[j], end=" ")
        print(int(eval(s1)))


# 求范式
def normal_form():
    op = int(input("选择模式：0、主合取范式；1、主析取范式\n"))
    num = int(input("输入变元个数:"))
    print("请输入{}个变元名，用;隔开".format(num))
    s = input().split(";")
    val = [0 for _ in range(num)]
    for i in range(num - 1):
        for j in range(i + 1, num):
            if len(s[i]) < len(s[j]):
                s[i], s[j] = s[j], s[i]
    text = ["主合取范式", "主析取范式"]
    print("请输入一行一个式子，输出他的{}".format(text[op]))
    s1 = input()
    s1 = simplify(s1)
    for i in range(num):
        s1 = s1.replace(s[i], "val[{}]".format(i))
    result = ""
    b = False
    if op == 0:
        for i in range(1 << num):
            m = i
            b2 = False
            for j in range(num):
                val[-1 - j] = m % 2
                m = int(m / 2)
            if int(eval(s1)) == 0:
                if b:
                    result = result + "&"
                b = True
                result = result + "("
                for k in range(num):
                    if b2:
                        result = result + "|"
                    b2 = True
                    if val[k] == 0:
                        result = result + s[k]
                    else:
                        result = result + "-" + s[k]
                result = result + ")"
    else:
        for i in range(1 << num):
            m = i
            b2 = False
            for j in range(num):
                val[-1 - j] = m % 2
                m = int(m / 2)
            if int(eval(s1)) == 1:
                if b:
                    result = result + "|"
                b = True
                result = result + "("
                for k in range(num):
                    if b2:
                        result = result + "&"
                    b2 = True
                    if val[k] == 1:
                        result = result + s[k]
                    else:
                        result = result + "-" + s[k]
                result = result + ")"

    print(result)


if __name__ == '__main__':
    while True:
        op = int(input("离散数学计算器\n1.求值\n2.替换式\n3.对偶式\n4.等价式\n5.真值表\n6.求范式\n7.退出\n选择数字:"))
        if op == 1:
            evaluate()
        elif op == 2:
            substitute()
        elif op == 3:
            antithesis()
        elif op == 4:
            equal()
        elif op == 5:
            table()
        elif op == 6:
            normal_form()
        elif op == 7:
            break
