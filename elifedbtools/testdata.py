
from database import *



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
        data_item = RelatedArticle(item.get("from_doi"), item.get("to_doi"))
        for property in dir(data_item):
            if property not in data_item.primary_keys:
                setattr(data_item, property, item.get(property))
        related_articles.append(data_item)
    
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
        data_item = Article(item.get("doi"))
        for property in dir(data_item):
            if property not in data_item.primary_keys:
                setattr(data_item, property, item.get(property))
        articles.append(data_item)
    
    return articles
    