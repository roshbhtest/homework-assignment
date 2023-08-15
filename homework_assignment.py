import pandas as pd
import datetime

class SimpleStockMarket:
    def __init__(self,input_data_file):
        self.input_stock_data = pd.read_csv(input_data_file)
        trade_columns = ['StockSymbol','timestamp', 'quantity', 'indicator', 'price']
        self.trade_records = pd.DataFrame(columns = trade_columns)
        
    def checkisvalidstock(self,stocksymbol):
        return stocksymbol in self.input_stock_data['StockSymbol'].values
        
    def calculate_dividend_yield(self,stock,price):
        if self.checkisvalidstock(stock):
            print('valid stock')
            stockdata= self.input_stock_data[self.input_stock_data['StockSymbol'] == stock]
            type_stock = list(stockdata['Type'])[0] 
            if type_stock == 'Common':
                dividend = list(stockdata['Last_Dividend'])[0] 
                return dividend / price
            elif list(stockdata['Type'])[0] == 'Preferred':
                dividend = int((list(stockdata['Fixed_Dividend'])[0])[:-1])*0.01
                return (dividend * list(stockdata['Par_Value'])[0]) / price
        else:
            print('stock information not available')
            return 0

    def calculate_pe_ratio(self, stock, price):
        dividend= self.calculate_dividend_yield(stock, price)
        try:
            return price / dividend
        except ZeroDivisionError as e:
            print('Zero dividend')

    def add_record(self, stock, quantity, action, price):
        if action == "buy":
            indicator_value = "buy"
        elif action == "sell":
            indicator_value = "sell"
        else:
            indicator_value = ""
        new_trade= {'StockSymbol': stock,
                'timestamp': datetime.datetime.now(), 
                'quantity': quantity,
                'indicator': indicator_value,
                'price': price}
        self.trade_records = pd.concat([self.trade_records, pd.DataFrame([new_trade])], ignore_index=True)
        print("New record added")

    def volume_weighted_stock_price(self, stock):
        stock_to_consider = self.trade_records[self.trade_records['StockSymbol'] == stock]
        check_15mins=(datetime.datetime.now() - datetime.timedelta(minutes=15))
        trades_in_last_15mins = stock_to_consider[(stock_to_consider['timestamp'] > check_15mins) & (stock_to_consider['timestamp'] <= datetime.datetime.now())]
        print(trades_in_last_15mins)
        return sum(trades_in_last_15mins['price'] * trades_in_last_15mins['quantity']) / sum(trades_in_last_15mins['quantity'])
        
    def gbce_share_index(self):
        if len(self.trade_records) != 0:
            gbce_index= 1
            count= 0
            for price in (self.trade_records['price']):
                gbce_index *= price
                count += 1
            return abs(gbce_index) ** (1 / count)
