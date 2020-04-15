import json
import argparse
import subprocess
import docker
from jinja2 import Environment, FileSystemLoader

ECR_REGISTRY = '815742652454.dkr.ecr.us-east-2.amazonaws.com/home-search-dashboard'

# RECEIVE COMMAND LINE ARGUMENT
parser = argparse.ArgumentParser()
parser.add_argument('--version', '-v', type=str)
args = parser.parse_args()

# GET AWS ECR PASSWORD
ecr_password = subprocess.run(['aws', 'ecr', 'get-login-password', '--region', 'us-east-2'],
                              stdout=subprocess.PIPE).stdout.decode('utf-8')

# BUILD AND UPLOAD DOCKER IMAGE
docker_client = docker.from_env()
print('Docker client created')

docker_image, _ = docker_client.images.build(
    tag='home-search-dashboard', path='.')
print('Docker image created: ', docker_image)

docker_tag = docker_image.tag(
    ECR_REGISTRY, tag=args.version)
print('Docker image tagged: ', docker_tag)

docker_login = docker_client.login(username='AWS', password=ecr_password,
                                   registry=ECR_REGISTRY)
print('Response from docker login: ', docker_login)

for docker_push_line in docker_client.images.push(ECR_REGISTRY, tag=args.version, stream=True, decode=True):
    print(docker_push_line)

# CREATE TASK DEF FILE
jinja_env = Environment(
    loader=FileSystemLoader('./')
)

task_def_template = jinja_env.get_template('ecs-task-def.json')
ecs_task_def = task_def_template.render(version=args.version)

with open(f'ecs-task-def-{args.version}.json', 'w') as f:
    f.write(ecs_task_def)
