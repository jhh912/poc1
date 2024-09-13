# 银行自主存款机
# 银行账户数据
Account = [
    {"账号": "13233054751", "密码": "123456", "姓名": "zhangsan", "余额": 100},
    {"账号": "13233054752", "密码": "654321", "姓名": "lisi", "余额": 20},
    {"账号": "13233054753", "密码": "456789", "姓名": "wangwu", "余额": 90}
]

# 界面1：系统进入界面
def xitongcaozuojiemian():
    "系统进入界面"
    print("=" * 40)
    print("{}{:^29}{}".format("=", "银行自助存取款系统", "="))
    print("=" * 40)
    print("{}{:^33}{}".format("=", "1、登录账号", "="))
    print("{}{:^33}{}".format("=", "2、退出系统", "="))
    print("=" * 40)
    cmd = int(input("请输入1或者2\n:"))
    while True:
        if cmd == 1:
            return 1
        elif cmd == 2:
            return 2
        else:
            print("输入无效，请重新输入！")

# 界面2：账号密码输入界面
def inputAccount():
    "账号输入界面"
    while True:
        print()
        account = input("========请输入11位数账号！========\n")
        if len(account) != 11:
            print("========输入账号位数错误！========\n")
        elif account.isdigit():
            for i in range(len(Account)):
                if account == Account[i]["账号"]:
                    if inputPassword(i) == 1:
                        return i
                    else:
                        print("========密码错误！========\n")
                        return -1
            print("========你输入的用户不存在========\n")
            return -1
        else:
            print("========请输入正确的格式========\n")

def inputPassword(member):
    "密码输入界面"
    while True:
        print()
        password = input("========请输入六位数密码！========\n：")
        if len(password) != 6:
            print("========输入密码有误！========\n")
        elif password.isdigit():
            if password == Account[member]["密码"]:
                return 1
            else:
                print("========输入密码有误！========\n")
        else:
            print("=======请输入正确的格式========\n")

# 界面3：用户操作界面
def operation(member):
    "用户操作界面"
    print("=" * 40)
    print("{}{}{}{}{}".format("1.存款\n", "2.取款\n", "3.查询\n", "4.转账\n", "5.退出"))
    cmd = input("=======请输入操作指令！========\n:")

    if cmd == "1":
        y = int(input("请输入存款金额！\n"))
        Account[member]["余额"] += y
        print("========存款成功========\n")
    elif cmd == '2':
        print("当前余额：{}".format(Account[member]["余额"]))
        y = int(input("请输入取款金额!\n:"))
        if y > Account[member]["余额"]:
            print("========您当前的余额不足！========\n")
        else:
            Account[member]["余额"] -= y
            print("取款成功！\n")
    elif cmd == "3":
        print("=" * 40)
        print("{:>10}{}|{}{}".format("姓名:", Account[member]["姓名"], "当前余额：", Account[member]["余额"]))
        print("=" * 40 + "\n")
    elif cmd == "4":
        accsum = [acc["账号"] for acc in Account]
        account = input("请输入对方账号！\n:")
        y = int(input("请输入转账金额！\n:"))
        if account not in accsum:
            print("========对方账户不存在！========\n")
        elif account == Account[member]["账号"]:
            print("========不能转账到自己账户！========\n")
        elif y > Account[member]["余额"]:
            print("========您当前的余额不足！========\n")
        else:
            for i in range(len(Account)):
                if account == Account[i]["账号"]:
                    Account[member]["余额"] -= y
                    Account[i]["余额"] += y
                    print("=========转账成功========\n")
                    break
    elif cmd == "5":
        return 5
    else:
        print("========请输入正确的命令========\n")

if xitongcaozuojiemian() == 1:
    while True:
        member = inputAccount()
        if member == -1:
            continue
        while True:
            if operation(member) == 5:
                break
            print("=" * 40)
            cmd = int(input("{:>15} {}".format("1.退出", "2.继续\n")))
            if cmd == 1:
                break
            elif cmd == 2:
                continue
            else:
                print("========请输入正确的指令！========\n")
else:
    print("系统正在退出中...\n以退出")