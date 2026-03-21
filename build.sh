#!/usr/bin/env bash
# Render build script: install Python deps and collect static files.
# In the Render dashboard, set Build Command to: chmod +x build.sh && ./build.sh
# Set Release Command (separate) to: python manage.py migrate --noinput

set -o errexit
set -o pipefail

cd "$(dirname "$0")"

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Collectstatic loads Django settings; SECRET_KEY may be unset during build.
export SECRET_KEY="${SECRET_KEY:-render-build-placeholder-not-for-runtime}"

python manage.py collectstatic --noinput
