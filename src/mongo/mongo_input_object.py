import graphene
from graphene.types.utils import yank_fields_from_attrs
from graphene.utils.subclass_with_meta import SubclassWithMeta_Meta
from graphene_mongo.registry import get_global_registry
from graphene_mongo.types import construct_fields


class PandoroMongoInputObjectType(graphene.InputObjectType):
    @classmethod
    def __init_subclass_with_meta__(  # pylint: disable=arguments-differ
        cls, model=None, registry=None, only_fields=(), exclude_fields=(),
        optional_fields=(), **options
    ):
        if not registry:
            registry = get_global_registry()

        fields = construct_fields(model=model, registry=registry, exclude_fields=exclude_fields, only_fields=only_fields),
        mongo_fields = yank_fields_from_attrs(
            fields[0][0],
            _as=graphene.Field,
        )

        for key, value in mongo_fields.items():
            if key in optional_fields:
                type_ = value.type if isinstance(
                    value.type, SubclassWithMeta_Meta) else value.type.of_type
                value = type_(
                    description=value.description
                )
            setattr(cls, key, value)

        super(PandoroMongoInputObjectType, cls).__init_subclass_with_meta__(
            **options
        )