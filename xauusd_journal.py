trade=[]
def add_trades(date,direction,entry,exit):
  profit= entry - exit
  trades.append([date,direction,entry,exit,profit])
  print(f"Trade Added: {date}, {direction}, {entry} -> {exit}, Profit/Loss:{profit}")
#Add your Trades Below
add_trade("2025-12-06","Buy",4165.67,4161.42)
add_trade("2025-12-04","Sell",4180.70,4136.68)
add_trade("2025-12-02","Sell",4166.17,4187.43)
#Print Full Journal
print("\nMy Trading XAUUSD Journal:")
for trade in trades:
  print(trade)
  
  
