def fix_marks(child_name: str) -> None:
    schoolkid = get_schoolkid(child_name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for bad_mark in bad_marks:
        mark = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).first()
        mark.points = 5
        mark.save()
    print("Оценки исправлены")


def remove_chastisements(child_name: str) -> None:
    schoolkid = get_schoolkid(child_name)
    bad_comments = Chastisement.objects.filter(schoolkid=schoolkid)
    bad_comments.delete()
    print("Замечания удалены")


def get_schoolkid(child_name: str) -> Schoolkid:
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
    except Schoolkid.DoesNotExist as exeption:
        print(f'{exeption}.Ученик не найден')
    else:
        print(f'Ученик  "{child.full_name}" найден.')
        return child


def create_commendation(child_name, subject):
    schoolkid = get_schoolkid(child_name)
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject,
    )
    lesson_of_subject = lessons.order_by('-date').first()
    Commendation.objects.create(
        text="Хвалю!",
        created=lesson_of_subject.date,
        schoolkid=schoolkid,
        subject=lesson_of_subject.subject,
        teacher=lesson_of_subject.teacher,
    )
    print("Похвала добавлена")
