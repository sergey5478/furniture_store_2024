from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from goods.models import Products


def q_search(query):
    # Если это цифра и длинна меньше или равно 5, возвращает кверисет(данные)
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return Products().objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")

    # return Products.objects.annotate(search=SearchVector("name", "description")).filter(search=query)
    # return Products.objects.filter(description__search=query)
    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     # Добавляет условия через или, плюс еще или и тд(по описанию)
    #     q_objects |= Q(description__icontains=token)
    #     # Добавляет условия через или, плюс еще или и тд(по названию)
    #     q_objects |= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)