import datetime
import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404

files_dir = settings.FILES_PATH

def file_list(request, date=None):
    template_name = 'index.html'
    files = os.listdir(files_dir)
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': [],
        'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    }
    if date:
        filter_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    for file in files:
        file_stat = os.stat(os.path.join(files_dir, file))
        name = file
        ctime = datetime.datetime.fromtimestamp(file_stat.st_ctime)
        if date:
            if filter_date != ctime.date():
                continue
        mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)
        file_data = {'name': name,
                     'ctime': ctime,
                     'mtime': mtime}
        context['files'].append(file_data)
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = os.path.join(files_dir, name)
    try:
        with open(file_path) as f:
            file_content = f.read()
    except FileNotFoundError:
        raise Http404("File does not exist. Don't type your own url, just click on links omg")
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )

