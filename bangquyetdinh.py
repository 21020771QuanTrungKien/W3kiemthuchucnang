import unittest

# Import hàm cần kiểm tra
from kiemthu import tien_tro_cap

class TestTroCapCalculator(unittest.TestCase):

    def test_tien_tro_cap_tre(self):
        # Kiểm tra tính đúng đắn của hàm cho dân IT trẻ
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)  # Không có phụ thuộc
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  # 30% phụ thuộc
        self.assertEqual(tien_tro_cap(1000, 2, 't'), 1500)  # 50% phụ thuộc
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)  # 80% phụ thuộc

    def test_tien_tro_cap_gia(self):
        # Kiểm tra tính đúng đắn của hàm cho dân IT già
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 300)  # 30%
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)  # 50% phụ thuộc
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800)  # 80% phụ thuộc
        self.assertEqual(tien_tro_cap(1000, 3, 'g'), 2000)  # 100% phụ thuộc

    def test_tien_tro_cap_gia_am(self):
        # Kiểm tra hàm trả về -1 nếu số phụ thuộc là số âm
        self.assertEqual(tien_tro_cap(1000, -1, 'g'), -1)
        self.assertEqual(tien_tro_cap(1000, -2, 't'), -1)
        
    def test_tien_tro_cap_nhap_sai(self):
        # Kiểm tra hàm trả về -1 nếu nhập sai định dạng dữ liệu
        self.assertEqual(tien_tro_cap("abc", 2, 't'), -1)
        self.assertEqual(tien_tro_cap(1000, 'abc', 't'), -1)

if __name__ == "__main__":
    unittest.main()
