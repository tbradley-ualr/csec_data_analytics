from mongoengine import Document, StringField, EmailField, EmbeddedDocument, IntField, EmbeddedDocumentField


class UserAddress(EmbeddedDocument):
    street = StringField(required=True, null=False)
    city = StringField(required=True, null=False)
    state = StringField(required=True, null=False)
    country = StringField(required=True, null=False)
    zip = IntField(required=True, null=False)


class User(Document):
    # mongoengine defaults to allow null
    first_name = StringField(required=True, null=False)
    last_name = StringField(required=True, null=False)
    email = EmailField(required=True, null=False)
    address = EmbeddedDocumentField(UserAddress, required=True)
