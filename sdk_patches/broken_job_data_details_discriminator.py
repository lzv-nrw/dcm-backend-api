import sys


def broken_job_data_details_discriminator(sdk):
    """
    Backend SDK - broken `discriminator` for JobDataDetails-schema

    sdk-patch required to mitigate problems with deserialization of
    JobDataDetails: the (default?) generator logic for resolving a
    discriminator is broken.
    """

    print(
        "\033[0;31mRUNNING BACKEND-SDK-PATCH 'broken_job_data_details_discriminator'\033[0m",
        file=sys.stderr,
    )

    @classmethod
    def patched_get_discriminator_value(cls, obj):
        return obj.get("archiveApi")

    sdk.models.job_data_details.JobDataDetails.get_discriminator_value = patched_get_discriminator_value
