from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')
    if from_landing == 'test':
        counter_click['test'] += 1
    elif from_landing == 'original':
        counter_click['original'] += 1
    print(counter_click)
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    landing_chosed = request.GET.get('ab-test-arg')
    if landing_chosed == 'test':
        template = 'landing_alternate.html'
        counter_show['test'] += 1
    elif landing_chosed == 'original':
        template = 'landing.html'
        counter_show['original'] += 1
    print(counter_show)
    return render_to_response(template)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        test_conversion = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        test_conversion = 0
    try:
        original_conversion = counter_click['original'] / counter_show['original']
    except ZeroDivisionError:
        original_conversion = 0
    print(test_conversion)
    return render_to_response('stats.html', context={
        'test_conversion': f'{test_conversion: .2f}',
        'original_conversion': f'{original_conversion: .2f}',
    })
