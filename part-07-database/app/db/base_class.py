import typing as t

from sqlalchemy.ext.declarative import as_declarative, declared_attr


class_registry: t.Dict = {}

# This decorator will register the class in the class_registry
@as_declarative(class_registry=class_registry)
class Base:
    id: t.Any
    __name__: str

    # Generate __tablename__ automatically
    # This will generate the table name based on the class name and convert it to lowercase
    # then it will be used as the table name in the registered class
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
