from django.forms import ModelForm
from app.models import Produto

# Create the form class.
class ProdutosForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'trabalhadores', 'fertilizantes', 'lucro']

