import array

from mongoengine import (Document, StringField, EmailField, EmbeddedDocument,
                         IntField, EmbeddedDocumentField, DateTimeField, BooleanField,
                         ListField, URLField, FloatField)


class UserAddress(EmbeddedDocument):
    street = StringField(required=True)
    city = StringField(required=True)
    state = StringField(required=True)
    country = StringField(required=True)
    zip = IntField(required=True)


class User(Document):
    # mongoengine defaults to allow null
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    address = EmbeddedDocumentField(UserAddress, required=True)

class LangString(EmbeddedDocument):
    lang = StringField(required=True)
    value = StringField(required=True, max_length=4096)
class Reference(EmbeddedDocument):
    url = URLField(required=True, max_length=500)

class MetricsList(EmbeddedDocument):
    version = StringField(required=True)
    vectorString = StringField(required=True)
    baseScore = StringField(required=True)
    baseSeverity = StringField(required=True)

class CreditString(EmbeddedDocument):
    lang = StringField(required=True)
    value = StringField(required=True, max_length=4096)

class Vulnerability(Document):
    cve_id = StringField(required=True)
    attack_vector_type = StringField(required=True)
    published = DateTimeField(required=True)
    lastModified = DateTimeField()
    sourceIdentifier = StringField()
    vulnerabilityStatus = StringField()
    credits = ListField(EmbeddedDocumentField(CreditString), required=True)
    descriptions = ListField(EmbeddedDocumentField(LangString), required=True, min_length=1)
    references = ListField(EmbeddedDocumentField(Reference), required=True)
    metrics = ListField(EmbeddedDocumentField(MetricsList), required=True)