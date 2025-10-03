import sys
import string
# E -> (T+E) | (T-E) | (T)
# T -> (F*T) | (F/T) | (F)
# F -> N | (E)

def calc(expr):
    res=expression(expr)
    print(f'RES: {res}')
    return


def getToken(stack):
  return stack[:1]


def isOperation(tok):
  return any(operation in tok for operation in '+-/*')


def isDigit(tok):
  return tok in string.digits


def isBraces(expr):
  return ('(' in expr)+(')' in expr)

# tok = token's index in expr line
def expression(expr):
    expr+='+'
    if expr[0]!='-':
        expr='+'+expr
        tok=1
        lastOp=0
    else:
        tok=0
        # lastOp = индекс последней операции
        lastOp=-1
    first=0
    # Перебор символов выражения от OP до OP ==> вызов term (OP = + | -)
    summand=''
    while tok < len(expr):
        if expr[tok] in '+-':
              if summand=='':
                summand = term(expr[lastOp+1:tok])
                   
              match expr[lastOp]:
                  case '+': first+=summand
                  case '-': first-=summand  
              lastOp=tok 
              summand=''
        tok+=1
    return first

# !!! Обработка выражений с вложенными скобками

def term(expr):
  expr='*'+expr+'*'
  second = 1
  tok = 1
  lastOp=0
  while tok < len(expr):
    if expr[tok] in '*/':
      if isDigit(expr[lastOp+1:tok]):
        summand = float(expr[lastOp+1:tok])
      else:
        summand = factor(expr[lastOp+1:tok])
      match expr[tok]:
        case '*': second*=summand
        case '/': second/=summand  
      lastOp=tok 
    tok+=1
  return second


def factor(expr):
  print(expr)
  return (eval(expr))

def main():
  for line in sys.stdin:
    calc(line.rstrip().replace(' ', ''))


if __name__ == '__main__':
  main()
