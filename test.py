import unittest
import datetime

def format_date(year,month,day):
  date = datetime.date(year, month, day).strftime("%Y%m%d")
  print(date)
  return date


class TestCSVParserConverter(unittest.TestCase):

	def test_formatdate(self):
			self.assertEqual(format_date(2016,2,2), '20160202')

	@unittest.expectedFailure
	def test_formatdate_OutOfRange(self):
			self.assertEqual(format_date(2016,13,2), '20161302', 'Value for month is out of range')

if __name__ == '__main__':
		unittest.main()