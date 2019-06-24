from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара",
                                     min_value=1)
    rate = forms.IntegerField(label="Процентная ставка",
                              min_value=1)
    months_count = forms.IntegerField(label="Срок кредита в месяцах",
                                      min_value=1)

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть\
                                         отрицательной")
        return initial_fee

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if not rate or rate < 8:
            raise forms.ValidationError('Не обманывайте, не бывает таких низких\
                                         процентов. Введите реальные проценты.')
        return rate

    def clean_months_count(self):
        months_count = self.cleaned_data['months_count']
        if not months_count or months_count <= 2:
            raise forms.ValidationError('Зачем вам кредит на такой короткий\
                                         срок? Лучше подкопите.')
        return months_count

