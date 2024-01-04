import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_PROJECT_LIST_URL = 'https://lista.mercadolivre.com.br/hello'

# Create your views here.
def my_scraping_view(request):

    #Pull information from the search bar
    search=request.POST.get('search')
    
    # Make a GET request to the URL
    response = requests.get(BASE_PROJECT_LIST_URL)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract information using Beautiful Soup methods
    # For example, find all <a> tags
    post_listing = soup.find_all(True, {'class':
            'ui-search-result__wrapper'
        }
    )

    final_posting = []

    # display the results only
    for post in post_listing:
        post_title = post.find('h2',class_='ui-search-item__title').text
        post_image_url = post.find('img').get('data-src')
        price_span = post.find('span', class_='andes-money-amount__fraction')
        post_price = price_span.text.strip() if price_span else None
        final_posting.append((post_title, post_image_url, post_price))

    context = {
        'post_data': final_posting,
    }
    # Further process the extracted data or send it to a template
    return render(request, 'base.html', context)
