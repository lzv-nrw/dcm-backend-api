import sys


def broken_job_config_data_selection_one_of_schema(sdk):
    """
    Backend SDK - broken `oneOf` for JobConfig.dataSelection-
    schema

    sdk-patch required to mitigate problems with deserialization of
    JobConfig.dataSelection: there is no `actual_instance` generated
    when methods like `config_sdk.create_job_config` are called with
    JSON.
    """

    print(
        "\033[0;31mRUNNING BACKEND-SDK-PATCH 'broken_job_config_data_selection_one_of_schema'\033[0m",
        file=sys.stderr,
    )

    unpatched___init__ = sdk.models.JobConfigurationDataSelection.__init__

    def new_init(self, *args, **data):
        if (
            "identifiers" in data
            or "sets" in data
            or "from" in data
            or "until" in data
        ):  # oai-type
            instance = (
                sdk.models.OAISelectionDetails(
                    **data
                )
            )
        elif "path" in data:  # hotfolder-type
            instance = (
                sdk.models.HotfolderSelectionDetails(
                    **data
                )
            )
        else:
            instance = {}
        unpatched___init__(self, actual_instance=instance, *args, **data)

    sdk.models.JobConfigurationDataSelection.__init__ = new_init


def ambiguous_job_config_data_selection_schema(sdk):
    """
    Backend SDK - "Multiple matches" for dataSelection-schemas

    sdk-patch required to mitigate problems with deserialization of
    dataSelection-variants (multiple matches found when ..)
    """

    print(
        "\033[0;31mRUNNING BACKEND-SDK-PATCH 'ambiguous_job_config_data_selection_schema'\033[0m",
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
        (
            sdk.models.OAISelectionDetails,
            ["identifiers", "sets", "from", "until"],
        ),
        (
            sdk.models.HotfolderSelectionDetails,
            ["path"],
        ),
    ]:
        Model.from_dict = create_patched_model(
            keys, Model.from_dict
        ).from_dict
