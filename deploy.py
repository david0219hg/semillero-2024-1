import subprocess


bucket_for_template = "semillero-2024-1-ejemplo"
stack_name = "semillero-stack"


build_command = ["sam", "build"]
try:
    subprocess.run(build_command, check=True, shell=True)
    print("Build successful!")
except subprocess.CalledProcessError as e:
    print(f"Build failed. Error: {e}")
    exit(1)

# Step 2: Run 'sam deploy'
deploy_command = [
    "sam",
    "deploy",
    "--stack-name",
    stack_name,
    "--s3-bucket",
    bucket_for_template,
    "--capabilities",
    "CAPABILITY_IAM",
]

try:
    subprocess.run(deploy_command, check=True, shell=True)
    print("Deployment successful!")
except subprocess.CalledProcessError as e:
    print(f"Deployment failed. Error: {e}")
    exit(1)
