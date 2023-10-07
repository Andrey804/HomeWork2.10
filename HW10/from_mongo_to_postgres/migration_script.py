import django, sys, os
from mongoengine import connect
from mmodels import Authors as A, Quotes as Q

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'HW10.settings')
django.setup()

from quotes.models import Author, Quote, Tag

client = connect(host='mongodb+srv://andrey:Password@homework8.wbd6jdu.mongodb.net/homework?retryWrites=true&w=majority')


authors_array = A.objects()

for one_author in authors_array:

    a1 = Author.objects.get_or_create(fullname=one_author.fullname, born_date=one_author.born_date,
                                      born_location=one_author.born_location, description=one_author.description)

    for one_quote in Q.objects(author=one_author.id):

        q1 = Quote.objects.get_or_create(quote_text=one_quote.quote, author=a1[0])

        if bool(one_quote.tags):
            for one_tag in one_quote.tags:
                t1 = Tag.objects.get_or_create(name=one_tag)
                q1[0].tags.add(t1[0])



