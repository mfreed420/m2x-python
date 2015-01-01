from m2x.resource import Collection, Item


class Trigger(Item):
    PATH = 'devices/{device_id}/triggers/{id}'

    def test(self):
        return self.api.post(self.path(self.PATH + '/test'))


class Triggers(Collection):
    PATH = 'devices/{device_id}/triggers'
    ITEMS_KEY = 'triggers'
    ITEM_CLASS = Trigger

    def item(self, entry):
        return self.ITEM_CLASS(self.api, device_id=self.device_id, **entry)
