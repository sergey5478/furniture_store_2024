from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchHeadline,
    SearchRank,
)
from goods.models import Products


def q_search(query):
    # Если это цифра и длинна меньше или равно 5, возвращает кверисет(данные)
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    # Записываем в резулт кверисэт
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    # В квери сэте по имени ищет и выделяет от и до
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result
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
