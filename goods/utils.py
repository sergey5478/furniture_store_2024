from django.db.models import Q

from goods.models import Products


def q_search(query):
    # Если это цифра и длинна меньше или равно 5, возвращает кверисет(данные)
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        # Добавляет условия через или, плюс еще или и тд(по описанию)
        q_objects |= Q(description__icontains=token)
        # Добавляет условия через или, плюс еще или и тд(по названию)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)