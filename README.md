# my_store is one page of studies of django and django rest framework
# Example of the relationship many to many 
'''
# Shell session 1
# python manage.py shell
'''
from tags.models import Tag

qs = Tag.objects.all()
print(qs)

white = Tag.objects.last()
white.title
white.slug
white.active

# A saída é um gerenciador de muitos para muitos#
# many to many manager
white.products
"""
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager..ManyRelatedManager object at 0x7fa2e27707f0>
"""

white.products.all()
"""
Queryset de PRODUCTS, muito parecido com Products.objects.all (), 
mas, neste caso, são TODOS os produtos que estão relacionados à tag "White"
"""
white.products.all().first()
"""
returna a primeira instância, se tiver
"""
exit()
'''
# Shell session 2
# python manage.py shell
'''
from products.models import Product
qs = Product.objects.all()
qs
tshirt = qs.first()
tshirt

tshirt.title
tshirt.description

tshirt.tag  
"""
Lança um error porque o Product model não tem o campo "tag"
"""
tshirt.tags  
"""
Lança um error porque o Product model não tem o campo "tags"
"""
tshirt.tag_set
"""
  Isso funciona porque o modelo de Tag tem o campo "products" com o ManyToMany para o Product
  <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager..ManyRelatedManager object at 0x7fd2e9879f98>
"""

tshirt.tag_set.all()
"""
Retorna um Queryset do modelo Tag, relacionado a este produto
"""

tshirt.tag_set.filter(title__iexact='azul')'''
# Shell session 1
# python manage.py shell
'''
from tags.models import Tag

qs = Tag.objects.all()
print(qs)

white = Tag.objects.last()
white.title
white.slug
white.active

# A saída é um gerenciador de muitos para muitos#
# many to many manager
white.products
"""
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager..ManyRelatedManager object at 0x7fa2e27707f0>
"""

white.products.all()
"""
Queryset de PRODUCTS, muito parecido com Products.objects.all (), 
mas, neste caso, são TODOS os produtos que estão relacionados à tag "White"
"""
white.products.all().first()
"""
returna a primeira instância, se tiver
"""
exit()
'''
# Shell session 2
# python manage.py shell
'''
from products.models import Product
qs = Product.objects.all()
qs
tshirt = qs.first()
tshirt

tshirt.title
tshirt.description

tshirt.tag  
"""
Lança um error porque o Product model não tem o campo "tag"
"""
tshirt.tags  
"""
Lança um error porque o Product model não tem o campo "tags"
"""
tshirt.tag_set
"""
  Isso funciona porque o modelo de Tag tem o campo "products" com o ManyToMany para o Product
  <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager..ManyRelatedManager object at 0x7fd2e9879f98>
"""

tshirt.tag_set.all()
"""
Retorna um Queryset do modelo Tag, relacionado a este produto
"""

tshirt.tag_set.filter(title__iexact='azul')
