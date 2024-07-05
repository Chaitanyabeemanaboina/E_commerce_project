import os
import subprocess
import sys

# Ensure the PA_API_TOKEN is set
pa_api_token = os.getenv('PA_API_TOKEN')
if not pa_api_token:
    print('PA_API_TOKEN is not set!')
    sys.exit(1)

# Run the pa_autoconfigure_django.py script with the provided arguments
command = [
    sys.executable,
    'pa_autoconfigure_django.py',
    sys.argv[1],  # git-repo-url
    '--python', sys.argv[2],  # python-version
    '--domain', sys.argv[3],  # domain
]

# Include the --nuke argument if specified
if len(sys.argv) > 4 and sys.argv[4] == '--nuke':
    command.append('--nuke')

# Execute the command
result = subprocess.run(command, env=os.environ)

# Exit with the same code as the subprocess
sys.exit(result.returncode)
