import unittest
from app import app

class TestBankAPI(unittest.TestCase):
    
    #To define a class method
    @classmethod               
    def setUpClass(cls):
        cls.client = app.test_client()

    #for checking the response of banks endpoint
    def test_get_banks(self):
        response = self.client.get('/banks')
        self.assertEqual(response.status_code, 200)
        self.assertIn('banks', response.json)

    #for checking the response of branches endpoint
    def test_get_branches_for_bank(self):
        response = self.client.get('/banks/1/branches')
        self.assertEqual(response.status_code, 200)
        self.assertIn('branches', response.json)
        self.assertEqual(response.json['branches'][0]['bank_id'], 1)

    #for checking the response of endpoint for a non-existing bank
    def test_get_branches_for_non_existing_bank(self):
        response = self.client.get('/banks/999/branches')  # Non-existing bank ID
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Not Found')
        self.assertEqual(response.json['message'], 'The requested URL is not present at the moment. Please check the endpoint and try once again.')


#main function
if __name__ == '__main__':
    unittest.main()
