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


@abstract
class Type(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class NamedElement(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


@abstract
class Propertied(EObject, metaclass=MetaEClass):

    properties = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, properties=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if properties:
            self.properties.extend(properties)


@abstract
class Bounded(EObject, metaclass=MetaEClass):

    upperBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    lowerBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, upperBound=None, lowerBound=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if upperBound is not None:
            self.upperBound = upperBound

        if lowerBound is not None:
            self.lowerBound = lowerBound


class DocumentSchema(NamedElement):

    entities = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entities=None, **kwargs):

        super().__init__(**kwargs)

        if entities:
            self.entities.extend(entities)


@abstract
class Property(NamedElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PrimitiveType(Type):

    datatype = EAttribute(eType=DataType, unique=True, derived=False, changeable=True)

    def __init__(self, *, datatype=None, **kwargs):

        super().__init__(**kwargs)

        if datatype is not None:
            self.datatype = datatype


class EntityType(NamedElement, Propertied):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Attribute(Property, Bounded):

    type = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class Reference(Property, Bounded):

    target = EReference(ordered=True, unique=True, containment=False, derived=False)
    type = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, target=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if target is not None:
            self.target = target

        if type is not None:
            self.type = type


class Aggregate(Property, Propertied, Bounded):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
