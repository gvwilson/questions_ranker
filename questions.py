import csv
from django.db import transaction
from questions_ranker.ranker.models import Category, Question
from questions_ranker.users.models import User


@transaction.atomic
def bulk_add_questions(filename):
    admin = User.objects.get(username="admin")
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"')
        results = []
        for row in reader:
            cat, _ = Category.objects.get_or_create(name=row['Category'],
                                                    defaults=dict(author=admin))
            res = Question.objects.create(
                id=int(row['ID']),
                content=row['Question'],
                category=cat,
                author=admin,
            )
            results.append(res)
    return results
