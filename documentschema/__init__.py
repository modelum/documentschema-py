
from .documentschema import getEClassifier, eClassifiers
from .documentschema import name, nsURI, nsPrefix, eClass
from .documentschema import DocumentSchema, EntityType, Property, Attribute, Reference, Aggregate, Type, PrimitiveType, Array, DataType


from . import documentschema

__all__ = ['DocumentSchema', 'EntityType', 'Property', 'Attribute',
           'Reference', 'Aggregate', 'Type', 'PrimitiveType', 'Array', 'DataType']

eSubpackages = []
eSuperPackage = None
documentschema.eSubpackages = eSubpackages
documentschema.eSuperPackage = eSuperPackage

DocumentSchema.entities.eType = EntityType
DocumentSchema.types.eType = Type
EntityType.properties.eType = Property
Attribute.type.eType = Type
Reference.target.eType = EntityType
Reference.type.eType = Type
Aggregate.properties.eType = Property
Array.type.eType = PrimitiveType

otherClassifiers = [DataType]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
