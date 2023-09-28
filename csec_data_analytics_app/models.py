import array


from mongoengine import (Document, StringField, EmbeddedDocument,
                         EmbeddedDocumentField, ListField, FloatField, connect)


class CVSSAttributes(EmbeddedDocument):
    version = FloatField()
    vectorString = StringField()
    accessVector = StringField()
    accessComplexity = StringField()
    authentication = StringField()
    confidentialityImpact = FloatField()
    integrityImpact = FloatField()
    availabilityImpact = FloatField()
    baseScore = FloatField()

class weakness_description(EmbeddedDocument):
    lang = StringField()
    value = StringField()
class weakneses(EmbeddedDocument):
    source = StringField()
    type = StringField()
    description = EmbeddedDocument(weakness_description)

class vulnerability_descriptions(EmbeddedDocument):
    lang = StringField()
    value = StringField()
class cpe_match(EmbeddedDocument):
    vulnerable = StringField()
    criteria = StringField()
    matchCriteria = StringField()

class cpe_nodes(EmbeddedDocument):
    operator = StringField()
    negate = StringField()
    cpeMatch = EmbeddedDocument(cpe_match)
class cpe_configurations(EmbeddedDocument):
    nodes = EmbeddedDocument(cpe_nodes)


class Vulnerability(Document):
    cve_id = StringField(required=True, unique=True)
    descriptions = EmbeddedDocument(vulnerability_descriptions)
    cpe_configurations = EmbeddedDocument(cpe_configurations)
    cwes = ListField(StringField())
    cvssData = EmbeddedDocumentField(CVSSAttributes)

    meta = {
        'collection': 'vulnerabilities'
    }

