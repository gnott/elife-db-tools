


def related(doi):
    if doi == 'a':
        return [{'from_doi': 'a',
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
    else:
        return []
        
        
def article(doi):
    if doi == 'a':
        return {'title': 'a title',
                'doi': doi,
                'doi_id': doi,
                'pub_date': '2015-01-01',
                'article_type': 'research-article'}
    if doi == 'b':
        return {'title': 'b title',
                'doi': doi,
                'doi_id': doi,
                'pub_date': '2015-02-02',
                'article_type': 'research-article'}
    if doi == 'c':
        return {'title': 'c title',
                'doi': doi,
                'doi_id': doi,
                'pub_date': '2015-03-03',
                'article_type': 'research-article'}
    if doi == 'd':
        return {'title': 'd title',
                'doi': doi,
                'doi_id': doi,
                'pub_date': '2015-04-03',
                'article_type': 'research-article'}