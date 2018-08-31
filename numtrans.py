while True:
    number = input('请输入一个整数(输入Q退出程序)：') 
    if number in ['q','Q']:
        break                #如果输入的是q或Q,结束退出
    elif not number.isdigit():
        print('您的输入有误！只能输入整数(输入Q退出程序)！请重新输入')
        continue         #如果输入的数字不是十进制,结束循环,重新开始
    else :
            number = int(number)
            print('十进制 --> 十六进制 ：%d -> 0x%x' %(number,number))
            print('十进制 -->   八进制 ：%d -> 0o%o' %(number,number))
            print('十进制 -->   二进制 ：%d ->'%number,bin(number))
