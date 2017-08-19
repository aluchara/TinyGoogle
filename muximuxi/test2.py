class Read():
    def __init__(self,num,base):
        self.num = num
        self.sumup = 0
        self.base=int(base)
        
    def sum_up(self):
        for i in self.num:
            n=int(i)
            self.sumup=n+self.sumup
        print(self.num,'的各位数总和是',self.sumup)

    def print_it(self) :
        d={'0':'ling','1':'yi','2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu'}
        strsum=str(self.sumup)
        print(self.sumup,'的拼音是',end='')
        for s in strsum:
            print(d[s],'',end='')
        print('\n')  #为啥这里加了这个换行会换两行？但是不加又不行，会跟下一个函数并排……

    def change(self) :
        print(self.sumup,'转化为',self.base,'进制是',end='')
        L=[]
        x=self.sumup
        quo=1
        while quo>0:
            quo=x//self.base
            mod=x%self.base
            if mod>9:
                mod=chr(65+mod-10)
            L.append(mod)
            x=quo
        while len(L)>0:
            sev=str(L.pop())
            print(sev,end='')
          

if __name__ == '__main__' :
    number = Read(input("输入一个尽可能长的数字\n"),input("输入你想要转换的进制"))
    number.sum_up()
    number.print_it()
    number.change()
