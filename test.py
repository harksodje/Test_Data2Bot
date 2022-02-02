import unittest

from assessment import load_json, indexing, tag_and_discription, json_convert


"============================================================================="

json_data_1 = load_json('data/data_1.json')   # load json 1
json_data_2 = load_json('data/data_2.json') # load json 2

class json_converter (unittest.TestCase):

    
    def test_schema_1(self):
        '''
        Testing function for data 1
        '''
        self.assertTrue(isinstance(json_data_1 ,dict),True) #checking json loaded 
        self.assertEqual('data/data_1.json', 'data/data_1.json') #checking the path for data 1
        self.assertEqual(len(tag_and_discription(json_data_1["message"])[0]),17) #len of tags
        self.assertEqual(len(tag_and_discription(json_data_1["message"])[1]),17)  # len of discriptions
        
        
        self.assertTrue(isinstance(json_convert(json_data_1, 
                         tag_and_discription(json_data_1["message"])[0], 
                        tag_and_discription(json_data_1["message"])[1], 
                        indexing(len(tag_and_discription(json_data_1["message"])[0])) ),dict), True)

    def test_schema_2(self):
        '''
        Testing function for data 2
        '''
        self.assertTrue(isinstance(json_data_2 ,dict),True) #checking json loaded 
        self.assertEqual('env/data/data_2.json', 'env/data/data_2.json') #checking the path for data 2
        self.assertEqual(len(tag_and_discription(json_data_2["message"])[0]),11) #len of tags
        self.assertEqual(len(tag_and_discription(json_data_2["message"])[1]),11) # len of discriptions
        
        self.assertEqual(isinstance(json_convert(json_data_2, 
                        tag_and_discription(json_data_2["message"])[0], 
                        tag_and_discription(json_data_2["message"])[1], 
                        indexing(len(tag_and_discription(json_data_2["message"])[0])) ),dict),
                         True)

if __name__ == "__main__":
    unittest.main()

