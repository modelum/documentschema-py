
from .documentschema import getEClassifier, eClassifiers
from .documentschema import name, nsURI, nsPrefix, eClass
from .documentschema import DocumentSchema, EntityType, Property, Attribute, Reference, Aggregate, Type, PrimitiveType, DataType, NamedElement, Propertied, Bounded


from . import documentschema

__all__ = ['DocumentSchema', 'EntityType', 'Property', 'Attribute', 'Reference',
           'Aggregate', 'Type', 'PrimitiveType', 'DataType', 'NamedElement', 'Propertied', 'Bounded']

eSubpackages = []
eSuperPackage = None
documentschema.eSubpackages = eSubpackages
documentschema.eSuperPackage = eSuperPackage

DocumentSchema.entities.eType = EntityType
Attribute.type.eType = Type
Reference.target.eType = EntityType
Reference.type.eType = Type
Propertied.properties.eType = Property

otherClassifiers = [DataType]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
