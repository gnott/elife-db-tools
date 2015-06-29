# -*- coding: utf-8 -*-
from lettuce import *
import testdata
import memdb

@step(u'I count the list total as (.*)')
def i_count_the_total_as(step, number):
    # Allow None because sometimes it is not a list returned
    if number == "None":
        assert world.list is None, \
            "Got %s" % world.list
    else:
        number = int(number)
        count = len(world.list)
        assert count == number, \
            "Got %d" % count

@step(u'I have the database (.*)')
def i_have_the_database(step, database):
    if database == "memdb":
        world.database = memdb

@step(u'I load the article test data')
def i_load_the_article_test_data(step):
    data = testdata.article_data()
    world.list = world.database.load_article_data(data)
    
@step(u'I load the related article test data')
def i_load_the_related_article_test_data(step):
    data = testdata.related_article_data()
    world.list = world.database.load_related_article_data(data)
    
@step(u'I load the test data')
def i_load_the_test_data(step):
    world.database.load_test_data()
    
@step(u'I have the doi (.*)')
def i_have_the_doi(step, doi):
    world.doi = doi
    
@step(u'I get article records by doi')
def i_get_article_records_by_doi(step):
    world.list = world.database.article(world.doi)
    
@step(u'I get related article records by doi')
def i_get_related_article_records_by_doi_doi(step):
    world.list = world.database.related(from_doi = world.doi)