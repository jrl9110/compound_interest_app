'''
This programme will be used to test my compound interest calculator
'''

from calc import monthly_compounding

def test_tautology():
    assert 3 == 2 + 1

def test_zeros_in_zeros_out():
    #establish input values
    initial = 0
    monthly = 0
    annual_rate = 0
    years = 0
    #calculate an output
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    #test output via an assertion
    assert final_sum == 0
    
    
def test_int_calc():
     #establish input values
     initial = 1000
     monthly = 100
     annual_rate = 0
     years = 1
     #calculate an output
     final_sum = monthly_compounding(initial, monthly, annual_rate, years)
     #test output via an assertion
     assert final_sum == 1100
     