
import database
import json

# The data itself
articles = None
related_articles = None

def load_related_article_data():
    """
    Temporary loading of data 
    """
    related_articles = []
    
    data = [{'from_doi': 'a',
                 'to_doi':   'b',
                 'ext_link_type': 'doi',
                 'related_article_type': 'commentary-article',
                 'xlink_href': 'b'
                 },
            
                {'from_doi': 'a',
                 'to_doi':   'c',
                 'ext_link_type': 'doi',
                 'related_article_type': 'commentary-article',
                 'xlink_href': 'c'
                 }
                ]
    for item in data:
        add_item("RelatedArticle", item, related_articles)
    
    return related_articles

def load_article_data():
    """
    Temporary loading of data 
    """
    articles = []
    
    data = []
    
    data.append({'doi': 'a', 'doi_id': 'a_id',
                 'title': 'a title',
                 'pub_date': '2015-01-01', 'article_type': 'research-article'})
    data.append({'doi': 'b', 'doi_id': 'b_id',
                 'title': 'b title',
                 'pub_date': '2015-02-01', 'article_type': 'research-article'})
    data.append({'doi': 'c', 'doi_id': 'c_id',
                 'title': 'c title',
                 'pub_date': '2015-03-01', 'article_type': 'research-article'})
    data.append({'doi': 'd', 'doi_id': 'd_id',
                 'title': 'd title',
                 'pub_date': '2015-04-01', 'article_type': 'research-article'})

    for item in data:
        add_item("Article", item, articles)
    
    return articles
    

def add_item(object_type, item, collection):
    #database_object = None
    #if hasattr(database, type):
    #    database_object = getattr(database, type)
    
    database_object = None
    if object_type == "Article":
        database_object = database.Article(item.get("doi"))
    if object_type == "RelatedArticle":
        database_object = database.RelatedArticle(item.get("from_doi"), item.get("to_doi"))

    for property in dir(database_object):
        if property not in database_object.primary_keys:
            setattr(database_object, property, item.get(property))
    
    collection.append(database_object)

    
    
def related(from_doi, to_doi = None):
    """
    Get related article items by doi
    """
    records = filter(lambda item: item.from_doi == from_doi, related_articles)
    return records
 
        
def article(doi):
    """
    Get article meta and details by doi
    """
    return filter(lambda item: item.doi == doi, articles)
    
    
    
    
    
    
    
    
    
def load_data():
    global articles, related_articles
    
    related_articles = load_related_article_data()
    articles = load_article_data()


if __name__ == '__main__':

    import testdata
    testdata.load_data()


    records = testdata.related("a")
    print "\n"
    print "Found " + str(len(records)) + " matching related article records"
    for item in records:
        print json.dumps(item.as_json(), indent=4)
        print item

    records = testdata.article("a")
    print "\n"
    print "Found " + str(len(records)) + " matching article records"
    for item in records:
        print json.dumps(item.as_json(), indent=4)
        print item

