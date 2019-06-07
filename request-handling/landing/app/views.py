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
    counter_click[from_landing] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    landing_chosed = request.GET.get('ab-test-arg')
    counter_show[landing_chosed] += 1
    if landing_chosed == 'test':
        template = 'landing_alternate.html'
    elif landing_chosed == 'original':
        template = 'landing.html'
    return render_to_response(template)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if counter_show['test']:
        test_conversion = counter_click['test'] / counter_show['test']
    else:
        test_conversion = 0
    if counter_show['original']:
        original_conversion = counter_click['original'] / counter_show['original']
    else:
        original_conversion = 0
    return render_to_response('stats.html', context={
        'test_conversion': f'{test_conversion: .2f}',
        'original_conversion': f'{original_conversion: .2f}',
    })
