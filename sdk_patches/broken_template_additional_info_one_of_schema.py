import sys


def broken_template_additional_info_one_of_schema(sdk):
    """
    Backend SDK - broken `oneOf` for Template.additionalInformation-
    schema

    sdk-patch required to mitigate problems with deserialization of
    Template.additionalInformation: there is no `actual_instance`
    generated when methods like `config_sdk.create_template` are called
    with JSON.
    """

    print(
        "\033[0;31mRUNNING BACKEND-SDK-PATCH 'broken_template_additional_info_one_of_schema'\033[0m",
        file=sys.stderr,
    )

    unpatched___init__ = sdk.models.TemplateAdditionalInformation.__init__

    def new_init(self, *args, **data):
        if "plugin" in data or "args" in data:  # plugin-type
            instance = (
                sdk.models.PluginTemplateInfo(
                    **data
                )
            )
        elif (
            "url" in data
            or "metadataPrefix" in data
            or "transferUrlFilters" in data
        ):  # oai-type
            instance = (
                sdk.models.OAITemplateInfo(
                    **data
                )
            )
        elif "sourceId" in data:  # hotfolder-type
            instance = (
                sdk.models.HotfolderTemplateInfo(
                    **data
                )
            )
        else:
            raise TypeError(
                "No match for any option of 'additionalArguments' with given "
                + f"arguments {args}, {data}."
            )
        unpatched___init__(self, actual_instance=instance, *args, **data)

    sdk.models.TemplateAdditionalInformation.__init__ = new_init


def ambiguous_template_additional_info_schema(sdk):
    """
    Backend SDK - "Multiple matches" for AdditionalInformation-schemas

    sdk-patch required to mitigate problems with deserialization of
    AdditionalInformation-variants: the original sdk ignores unknown
    input
    """

    print(
        "\033[0;31mRUNNING BACKEND-SDK-PATCH 'ambiguous_template_additional_info_schema'\033[0m",
        file=sys.stderr,
    )

    def create_patched_model(accepted_keys, unpatched_from_dict):
        """Factory is used to avoid cell-variable problems in loop."""
        class PatchedModel(Model):
            """Patched Model."""

            @classmethod
            def from_dict(cls, obj):
                """Patched `from_dict` that does not accept unknown keys."""
                if any(
                    key not in accepted_keys
                    for key in obj.keys()
                ):
                    return None

                return unpatched_from_dict(obj)

        return PatchedModel

    # pylint: disable=invalid-name
    for Model, keys in [
        (sdk.models.PluginTemplateInfo, ["plugin", "args"]),
        (
            sdk.models.OAITemplateInfo,
            ["url", "metadataPrefix", "transferUrlFilters"],
        ),
        (sdk.models.HotfolderTemplateInfo, ["sourceId"]),
    ]:
        Model.from_dict = create_patched_model(
            keys, Model.from_dict
        ).from_dict
