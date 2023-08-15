import unittest
import homework_assignment

class TestSimpleStockMarket(unittest.TestCase):
    
    def setUp(self):
        stock_data= homework_assignment.SimpleStockMarket('test_data.csv')

    def test_calculate_dividend_yield(self):
        self.assertEqual(2.6, self.stock_data.calculate_dividend_yield(stock= 'JOE', price= 5))
        self.assertEqual(0.4, self.stock_data.calculate_dividend_yield(stock= 'GIN', price= 5))
        self.assertEqual(0, self.stock_data.calculate_dividend_yield(stock= 'DUMMY', price= 5))

    def test_calculate_pe_ratio(self):
        self.assertAlmostEqual(0.307,self.stock_data.calculate_pe_ratio(stock= 'JOE', price= 2), places= 3)
        self.assertEqual(2.0,self.stock_data.calculate_pe_ratio(stock= 'GIN', price= 2))
        self.assertIsNone(self.stock_data.calculate_pe_ratio(stock= 'DUMMY', price= 5))

    def test_add_record(self):
        self.stock_data.add_record(stock= 'POP', quantity= 10, action= "sell", price= 5)
        self.assertEqual(1, len(self.stock_data.trade_records))

    def test_volume_weighted_stock_price(self):
        self.stock_data.add_record(stock= 'POP', quantity= 10, action= 'buy', price= -1)
        self.stock_data.add_record(stock= 'POP', quantity= 15, action= 'sell', price= 5)
        self.stock_data.add_record(stock= 'TEA', quantity= 20, action= 'buy', price= 2)
        self.stock_data.add_record(stock= 'TEA', quantity= 50, action= 'sell', price= 10)

        self.assertEqual(2.6, self.stock_data.volume_weighted_stock_price('POP'))
        self.assertAlmostEqual(7.714, self.stock_data.volume_weighted_stock_price('TEA'), places= 3)

    def test_gbce_share_index(self):
        self.stock_data.add_record(stock= 'POP', quantity= 10, action= 'buy', price= -1)
        self.stock_data.add_record(stock= 'POP', quantity= 15, action= 'sell', price= 5)
        self.stock_data.add_record(stock= 'TEA', quantity= 20, action= 'buy', price= 2)
        self.stock_data.add_record(stock= 'TEA', quantity= 50, action= 'sell', price= 10)
        
        self.assertAlmostEqual(3.16, stock_data.gbce_share_index(), places= 2)

if __name__ == '__main__':
    unittest.main()
