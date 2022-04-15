from django import forms
from .models import worker,workplace



class workerModelForm(forms.ModelForm):
    class Meta:
        model = worker
        fields = (
            '이름',
            '나이',
            '작업장1',
            '체온',
            '비상버튼',
        )


class workerForm(forms.Form):
    이름 = forms.CharField()
    나이 = forms.IntegerField(min_value=0)
    작업장1 = forms.CharField()
    체온 = forms.IntegerField(min_value=0)
    비상버튼 = forms.CharField()






class workplaceModelForm(forms.ModelForm):
    class Meta:
        model = workplace
        fields = (
            '작업장',
            '주소',
            '관리자',
        )

        
class workplaceForm(forms.Form):
    작업장 = forms.CharField()
    주소 = forms.CharField()
    관리자 = forms.CharField()
    


