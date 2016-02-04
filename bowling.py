score_chart = {'-': 0, 'X': 10, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def process_game(line):
  score = 0
  for _ in range(0,10):
    (turn_score, line) = process_turn(line)
    score += turn_score
  return score  
  
def process_turn(throws): 
  if throws[1] is '/':
    return (10 + bonus_point(1, throws[2:]), throws[2:])
  elif throws[0] is 'X':
    return (10 + bonus_point(2, throws[1:]), throws[1:])
  else:
    return (score_chart[throws[0]] + score_chart[throws[1]], throws[2:])
   
def bonus_point(extras, throws):
    return 0 if extras is 0 else 10 if extras == 2 and throws[1] is '/' else score_chart[throws[0]] + bonus_point(extras-1, throws[1:])
