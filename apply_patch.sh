#!/bin/bash

cp -r "sdk_patches" "$1"
echo '
#######################
# SDK-PATCHES

from .sdk_patches import patch
import sys

patch(sys.modules[__name__])

# SDK-PATCHES-END
#######################' >> "$1/__init__.py"
