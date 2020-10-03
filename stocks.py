from nsetools import Nse
from app import db, Stock
nse = Nse()
all_stock_codes = nse.get_stock_codes()
print(123)
all_stock_codes=dict(all_stock_codes)
for k,v in all_stock_codes.items():
  try:
    x=Stock(name=v,symbol=k)
    db.session.add(x)
    db.session.commit()
  except Exception as e:
    print(e)
    pass
	
