'''
Created on 8 ago. 2017

@author: Val
'''
import unittest, os
from pyGeni.data_models import geni_union
from pyGeni.immediate_family import immediate_family
from tests.FIXTURES import *


class testpyGeniNoProfile(unittest.TestCase):
 
    def setUp(self):
        self.token = os.environ['GENI_KEY']
        

    def testgenerateunion(self):
        '''
        This test checks that a union is properly registered in the data model
        when introduced as input from geni
        '''
        union_test = geni_union(UNION_EXAMPLE, UNION_EXAMPLE_ID)
        assert(union_test.union_id == UNION_EXAMPLE_ID)
        #Check of the parent
        assert(union_test.is_profile_parent(UNION_EXAMPLE_PARENT))
        self.assertFalse(union_test.is_profile_child(UNION_EXAMPLE_PARENT))
        
        #Check the children
        self.assertFalse(union_test.is_profile_parent(UNION_EXAMPLE_CHILD))
        assert(union_test.is_profile_child(UNION_EXAMPLE_CHILD))
        
        #Check random profile
        self.assertFalse(union_test.is_profile_parent(UNION_EXAMPLE_NOT_INCLUDED))
        self.assertFalse(union_test.is_profile_child(UNION_EXAMPLE_NOT_INCLUDED))
        
        #Check the number of children
        assert(len(union_test.children) == UNION_EXAMPLE_NUMBER_CHILDREN)
        
    def testimmediatefamily(self):
        '''
        This test confirms that the immediate family gets the right values
        '''
        philip_family = immediate_family(self.token, PHILIPIVid)
        
        assert (len(philip_family.parents) == 2)
        assert(len(philip_family.sibligns) == 8)
        assert(len(philip_family.partner) == 3)
        assert(len(philip_family.children) == 16)
        assert(philip_family.union_extracted)
        
    def test_immediatefamily_not_operational(self):
        '''
        I do not know why, but this profile is failing when providing
        the immediate family
        '''
        failing_family = immediate_family(self.token, PROFILE_NOT_WORKING)
        
        assert (len(failing_family.parents) == 0)
        assert(len(failing_family.sibligns) == 0)
        assert(len(failing_family.partner) == 0)
        assert(len(failing_family.children) == 0)
        self.assertFalse(failing_family.union_extracted)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()