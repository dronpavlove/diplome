from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.template.defaultfilters import filesizeformat
from .models import Banners


class BannersForm(ModelForm):
    """
    Форма создания баннеров для рекламы
    """

    def clean_photo(self):
        # Ограничение размера файла не более 3Мбайт
        MAX_FILE_SIZE = 3145728
        photo = self.files.get('photo')
        if photo:
            if photo.size > MAX_FILE_SIZE:
                err_msg = 'Размер файла не должен превышать {}'.format(filesizeformat(MAX_FILE_SIZE))
                raise ValidationError(err_msg)
        return photo

    class Meta:
        model = Banners
        fields = '__all__'
