
import database
import json


def load_related_article_data(data):
    """
    Temporary loading of data 
    """
    related_articles = []
    
    for item in data:
        status = add_item("RelatedArticle", item, related_articles)
    
    return related_articles

def load_article_data(data):
    """
    Temporary loading of data 
    """
    articles = []
    
    for item in data:
        status = add_item("Article", item, articles)
    
    return articles
    

def add_item(object_type, item, collection):
    #database_object = None
    #if hasattr(database, type):
    #    database_object = getattr(database, type)
    
    database_object = None
    if object_type == "Article":
        if len(article(item.get("doi"))) <= 0:
            database_object = database.Article(item.get("doi"))
            
    if object_type == "RelatedArticle":
        if len(related(item.get("from_doi"), item.get("to_doi"))) <= 0:
            database_object = database.RelatedArticle(item.get("from_doi"), item.get("to_doi"))

    if not database_object:
        return False

    for property in dir(database_object):
        if property not in database_object.primary_keys:
            setattr(database_object, property, item.get(property))
    
    collection.append(database_object)
    
    return True
    
    
def related(from_doi, to_doi = None):
    """
    Get related article items by doi
    """
    if 'related_articles' not in globals():
        return []
    records = filter(lambda item: item.from_doi == from_doi, related_articles)
    if to_doi:
        records = filter(lambda item: item.to_doi == to_doi, records)
    return records
 
        
def article(doi):
    """
    Get article meta and details by doi
    """
    if 'articles' not in globals():
        return []
    return filter(lambda item: item.doi == doi, articles)
    
    
    
    
    
def build_schema():
    pass
    
def load_data():
    """ TDB """
    pass

def load_test_data():
    import testdata
    
    global articles, related_articles
    articles = []
    related_articles = []
    
    data = testdata.related_article_data()
    related_articles = load_related_article_data(data)
    
    data = testdata.article_data()
    articles = load_article_data(data)


if __name__ == '__main__':

    build_schema()
    load_test_data()


    records = related("a")
    print "\n"
    print "Found " + str(len(records)) + " matching related article records"
    for item in records:
        print json.dumps(item.as_json(), indent=4)
        print item

    records = article("a")
    print "\n"
    print "Found " + str(len(records)) + " matching article records"
    for item in records:
        print json.dumps(item.as_json(), indent=4)
        print item

