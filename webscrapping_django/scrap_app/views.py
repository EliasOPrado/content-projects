import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_PROJECT_LIST_URL = 'https://lista.mercadolivre.com.br/{}'

# Create your views here.
def my_scraping_view(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            encoded_search = search.encode('utf-8')
            final_url = BASE_PROJECT_LIST_URL.format(quote_plus(encoded_search))
            
            response = requests.get(final_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            post_listing = soup.find_all(True, {'class': 'ui-search-result__wrapper'})

            final_posting = []
            for post in post_listing:
                post_title = post.find('h2', class_='ui-search-item__title').text
                post_image_url = post.find('img').get('data-src')
                price_span = post.find('span', class_='andes-money-amount__fraction')
                post_price = price_span.text.strip() if price_span else None
                final_posting.append((post_title, post_image_url, post_price))

            context = {'post_data': final_posting}
            return render(request, 'base.html', context)
    
    # Render the same template for GET requests or when search is empty
    return render(request, 'base.html')
