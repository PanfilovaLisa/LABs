import sys
import string
import itertools

def CheckGrammar(expr):
  ''' Check the correctness of a given expression '''
  # проверка на правильный порядок ввода оператора
  if any(''.join(doubleOp) in expr for doubleOp in itertools.product('+-*/', repeat=2)):
    raise SyntaxError('Double Operation')
  
  # проверка на отсутствие лишней операции в конце выражения
  if isOperation(expr[-1]):
     raise SyntaxError('Excess operation')
  
  # проверка на отсутствие символов отличных от чисел и +-*/
  if (not all(isOperation(symbol) or isDigit(symbol) for symbol in expr)):
     raise SystemError('Unknown symbol')
  
  # Выражение записано верно
  return (True)


def calc(expr):
  """ Calculator. Work only if expression is correct.

  Arguments:
    res -- the result of calculations
  """
  if CheckGrammar(expr):
    res=expression(expr)
    print(f'RES: {res}')
    return


def isDigit(tok):
  """ Return True if the symbol is a number

  Arguments:
    tok -- the checking symbol
  """
  return tok in string.digits


def isOperation(tok):
  """ Return True if the symbol is an operation

  Arguments:
    tok -- the checking symbol
  """
  return (tok in '+-/*()')

# Check all braces are closed
def isBraces(expr):
  """ Return True if all braces are closed.

  If expression doesn't has braces - return True
  Arguments:
    tok -- the checking symbol
  """
  return (expr.count('(') == expr.count(')'))


# tok = token's index in expr line
def expression(expr):
  """ First step of recursion

  Arguments:
    tok -- the checking symbol
  """

  expr+='+'
  if expr[0]!='-':
      expr='+'+expr
  tok=1
  # lastOp = индекс последней операции
  lastOp=0
  # First = результат
  first=0
  # Перебор символов выражения от OP до OP ==> вызов term (OP = + | -)
  while tok < len(expr):
      if expr[tok] in '+-':
            line1 = expr[lastOp+1:tok]
            # Проверка на то, что все скобки закрыты (если их нет, то кол-во = 0 => всё корректно работает)
            if isBraces(line1):
              summand = term(line1)
            else:
              tok+=1
              continue
            # Выполнение операции сложения/вычитания
            match expr[lastOp]:
                case '+': first+=summand
                case '-': first-=summand  
            # Перезапись индекса последней выполненной операции
            lastOp=tok
      tok+=1
  return first


def term(expr):
  expr='*'+expr+'*'
  second = 1
  tok = 1
  lastOp=0
  while tok < len(expr):
    if expr[tok] in '*/':
      line2 = expr[lastOp+1:tok]
      if isBraces(line2):
        summand = factor(line2)
      else:
         tok+=1
         continue
      match expr[tok]:
        case '*': second*=summand
        case '/': second/=summand
      lastOp=tok 
    tok+=1
  return second


def factor(expr):
  if '(' in expr:
    return expression(expr[1:-1])
  if isDigit(expr):
      return float(expr)


def main():
  for line in sys.stdin:
    calc(line.rstrip().replace(' ', ''))


if __name__ == '__main__':
  main()
