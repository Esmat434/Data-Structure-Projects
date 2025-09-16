class Calculator:
    def __init__(self):
        self.operators = {'+':1,'-':1,'*':2,'/':2}
        self.infix=''
        self.postfix=''
        self.stack=[]

    def InfixToPostfix(self,nums):
        nums = [i for i in nums if i]
        for i in nums:
            if i not in self.operators:
                self.postfix+=i
            else:
                if not self.stack:
                    self.stack.append(i)
                else:
                    status=False
                    while self.stack:
                        if self.operators[i]>self.operators[self.stack[-1]]:
                            self.stack.append(i)
                            status=True
                            break
                        elif self.operators[i]<self.operators[self.stack[-1]] or self.operators[i] == self.operators[self.stack[-1]]:
                            self.postfix+=self.stack.pop()
                    if not status:
                        self.stack.append(i)
        self.postfix+="".join(self.stack)
        return self.postfix
    
    def Calc(self,nums):
        self.postfix = self.InfixToPostfix(nums)
        self.stack=[]
        for i in self.postfix:
            if i not in self.operators:
                self.stack.append(i)
            else:
                if len(self.stack)<2:
                    raise ValueError("Your nums was wrong")
                else:
                    num1 = self.stack.pop()
                    num2 = self.stack.pop()
                    if i == '+':
                        self.stack.append(str(int(num1)+int(num2)))
                    elif i == '-':
                        self.stack.append(str(int(num1)-int(num2)))
                    elif i == '*':
                        self.stack.append(str(int(num1)*int(num2)))
                    elif i == '/':
                        self.stack.append(str(int(num1)//int(num2)))
        return int(''.join(self.stack))


calc=Calculator()
print(calc.Calc("1+3/4*6/8-4"))