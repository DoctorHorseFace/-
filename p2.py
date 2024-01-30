class queue():# 设置一个先进先出的队列，最大队列数为10
    def __int__(self):
        self.q = []
        self.max = 10
    def put(self,it):
        if len(self.q) == self.max:
            self.q.pop(0)
            self.q.append(it)
        else:
            self.q.append(it)
    def check(self,it):
        if it in self.q:
            return True
        else:
            return False

def transform(s):
    q = queue()
    q.__int__()
    res = ''
    for i in range(len(s)):
        if q.check(s[i]):
            res += '-'
        else:
            res += s[i]
        q.put(s[i])
    return res

if __name__ == '__main__':
    s = input()
    print(transform(s))