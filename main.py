from search import search_object

class CRUDMixin:
    def _get_or_set_objects_and_id(self):
        try:
            if(self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0
    
    def __init__(self):
        self._get_or_set_objects_and_id()

    def create(self, **kwargs):
        self.id += 1
        object_ = dict(id = self.id, **kwargs)
        self.objects.append(object_)
        return object_

    def list(self):
        res = []
        for obj in self.objects:
            res.append({'id': obj['id'], 'brand': obj['brand'], 'price': obj['price'], 'model': obj['model'], 'year': obj['year'], 'eng': obj['eng'], 'color': obj['color'], 'kuzov': obj['kuzov'], 'probeg': obj['probeg']})
        return res
    
    @search_object
    def retrieve(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return obj
        return 'Not found!'

    @search_object
    def update(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return obj
        return 'Not found!'

    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs.get('object_')
        if obj:
            self.objects.remove(obj)
            return 'Deleted!'
        return 'Not found!'

    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved!'

cars = CRUDMixin()
print(cars.create(brand = 'Mercedes', model = 'W140', year = 2018, eng = 5.5, color = 'Black', kuzov = 'Sedan', probeg = 20000, price = 40000.50))
print(cars.create(brand = 'BMW', model = 'M3', year = 2020, eng = 6.1, color = 'Dark Blue', kuzov = 'Sedan', probeg = 60000, price = 35000.50))
print()
print(cars.list())
print()
print(cars.retrieve(1))
print(cars.retrieve(2))
print()
print(cars.update(2, price = 22000))
print()
print(cars.delete(1))
print(cars.list())
print(cars.save())
