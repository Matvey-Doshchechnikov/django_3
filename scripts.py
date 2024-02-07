import random
from datacenter.models import Schoolkid, Mark, \
    Chastisement, Lesson, Commendation, Subject


RECOMMENDATIONS = [
    "Хвалю!",
    "Отлично!",
    "Молодец!",
    "Так держать!",
]


def fix_marks(child_name: str) -> None:
    schoolkid = get_schoolkid(child_name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    bad_marks.update(points=5)
    print("Оценки исправлены")


def remove_chastisements(child_name: str) -> None:
    schoolkid = get_schoolkid(child_name)
    bad_comments = Chastisement.objects.filter(schoolkid=schoolkid)
    bad_comments.delete()
    print("Замечания удалены")


def get_schoolkid(child_name: str) -> Schoolkid:
    try:
        children = Schoolkid.objects.filter(full_name__contains=child_name)
        if not children.exists():
            raise Schoolkid.DoesNotExist(f'Ученик с именем "{child_name}" не найден.')
        elif children.count() > 1:
            print(f'Найдено несколько учеников с именем "{child_name}".')
            return None
        else:
            child = children.first()
            print(f'Ученик "{child.full_name}" найден.')
            return child
    except Schoolkid.DoesNotExist as exception:
        print(exception)
        return None


def create_commendation(child_name, subject, commendations=RECOMMENDATIONS):
    schoolkid = get_schoolkid(child_name)
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject,
    )
    lesson_of_subject = lessons.order_by('-date').first()
    try:
        if not lesson_of_subject:
            raise Subject.DoesNotExist("В данный день не было урока.")
    except Subject.DoesNotExist as e:
        print(f"Ошибка: {e}")
        return
    commendation = random.choice(commendations)
    Commendation.objects.create(
        text=commendation,
        created=lesson_of_subject.date,
        schoolkid=schoolkid,
        subject=lesson_of_subject.subject,
        teacher=lesson_of_subject.teacher,
    )
    print("Похвала добавлена")
