"""This file runs tests for all functions in marketmechanims"""
import pytest
from numpy.testing import assert_equal
from stockmarket.marketmechanisms import *
from stockmarket.agents import *
from stockmarket.firms import *
from stockmarket.setup import *
from stockmarket.functions import *
from stockmarket.valuationfunctions import *

@pytest.fixture()
def set_up_agents():
    demander = Trader(name='demander', money=10, bid_ask_spread=0, memory_size=2, function=valuation_extrapolate_average)
    supplier = Trader(name='supplier', money=10, bid_ask_spread=0, memory_size=1, function=valuation_extrapolate_average)
    agents = [demander, supplier]
    firm = Firm(name='firm', book_value=200, profit=0, profit_history=[0, 5, 0], seed=1, dividend_rate=1)
    stocks = setup_stocks([firm], face_value=50)
    # distribute stocks
    stocks, agents = distribute_initial_stocks(stocks, agents)
    return {'demander': demander, 'supplier': supplier, 'agents': agents, 'firm': firm, 'stocks': stocks}


def test_suitable_trade(set_up_agents):
    assert_equal(suitable_trade(set_up_agents['demander'], set_up_agents['supplier'],
                                (None, math.inf), set_up_agents['stocks'][0]),
                                False)
    assert_equal(suitable_trade(set_up_agents['demander'], set_up_agents['supplier'],
                                (None, math.inf), set_up_agents['stocks'][0]),
                                False)
