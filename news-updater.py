#Your API key is: 760d32d30f664d54921e94f8e295651e
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='760d32d30f664d54921e94f8e295651e')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en')
# print(top_headlines)
# dt=top_headlines['articles']
# for x,y in enumerate(dt):
#     print(f'{x} {y["description"]}')














dt = top_headlines['articles']
for x,y in enumerate(dt):
    print(f'')
