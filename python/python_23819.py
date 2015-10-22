# ORs and AND in if statement in Python
if ((opponentBoard[row][col] == const.MISSED) or (opponentBoard[row][col] == const.HIT) or (row == 12)):
    if ((row &gt; 5) and (col &lt; 6)):
       exec_func();
