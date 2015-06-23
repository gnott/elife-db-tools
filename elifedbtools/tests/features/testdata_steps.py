# -*- coding: utf-8 -*-
from lettuce import *
import testdata
        
@step(u'I count the list items')
def i_count_the_list_items(step):
    if world.list == None:
        world.count = None
    else:
        world.count = len(world.list)

@step(u'I count the total as (.*)')
def i_count_the_total_as(step, number):
    # Allow None because sometimes it is not a list returned
    if number == "None":
        assert world.count is None, \
            "Got %s" % world.count
    else:
        number = int(number)
        assert world.count == number, \
            "Got %d" % world.count
        
@step(u'I load the article test data')
def i_load_the_article_test_data(step):
    world.list = testdata.load_article_data()
    
@step(u'I load the related article test data')
def i_load_the_related_article_test_data(step):
    world.list = testdata.load_related_article_data()