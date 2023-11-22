from itertools import permutations
import copy
def solution(expression):
    answer = 0
    arr =set([])

    def calc(x, a, b):
        # print(f'here,{a},{b}')
        a, b = int(a), int(b)
        if x == '-':
            return a - b
        elif x == '+':
            return a + b
        else:
            return a * b

    expressions = []
    tmp = ""
    for i in expression:
        if i.isdigit() == True:
            tmp += i
        else:
            expressions.append(tmp)
            expressions.append(i)
            arr.add(i)
            tmp = ""
    expressions.append(tmp)
    # print(expressions)
    # print(arr)

    def operations(oper, expressions):
        answer = []
        op = ''
        # print('--current',oper,expressions)
        for x in expressions:
            # print(answer, x,x.isdigit())
            # x = x.split('-')[-1]
            if x.split('-')[-1].isdigit():
                if op == '':
                    answer.append(x)
                else:
                    answer.append(str(calc(op, answer.pop(), x)))
                    op = ''
            else:
                if x == oper:
                    # print(x,oper)
                    op = x
                else:
                    answer.append(x)
                continue

        # print('--',answer)
        return answer
    answer = 0
    for order in permutations(arr, len(arr)):
        tmp_ = copy.deepcopy(expressions)
        # print(order)
        for oper in order:
            # print(oper)
            tmp_ = operations(oper, tmp_)
        # print('&&&&&&&&&&&&&&',tmp_)
        answer = max(answer, abs(int(tmp_[0])))

    return answer