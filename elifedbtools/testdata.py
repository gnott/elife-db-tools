
def related_article_data():

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

    return data

def article_data():

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

    return data


