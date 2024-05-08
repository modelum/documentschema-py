"""Definition of meta model 'documentschema'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'documentschema'
nsURI = 'http://www.modelum.es/documentschema'
nsPrefix = 'documentschema'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
DataType = EEnum('DataType', literals=['BOOLEAN', 'INTEGER', 'DOUBLE', 'STRING'])


class DocumentSchema(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    entities = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    types = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, entities=None, types=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if entities:
            self.entities.extend(entities)

        if types:
            self.types.extend(types)


class EntityType(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    properties = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, properties=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if properties:
            self.properties.extend(properties)


@abstract
class Property(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


@abstract
class Type(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Attribute(Property):

    isKey = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, isKey=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if isKey is not None:
            self.isKey = isKey

        if type is not None:
            self.type = type


class Reference(Property):

    target = EReference(ordered=True, unique=True, containment=False, derived=False)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, target=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if target is not None:
            self.target = target

        if type is not None:
            self.type = type


class Aggregate(Property):

    isMany = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    aggregates = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, aggregates=None, isMany=None, **kwargs):

        super().__init__(**kwargs)

        if isMany is not None:
            self.isMany = isMany

        if aggregates is not None:
            self.aggregates = aggregates


class PrimitiveType(Type):

    datatype = EAttribute(eType=DataType, unique=True, derived=False, changeable=True)

    def __init__(self, *, datatype=None, **kwargs):

        super().__init__(**kwargs)

        if datatype is not None:
            self.datatype = datatype


class Array(Type):

    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type
