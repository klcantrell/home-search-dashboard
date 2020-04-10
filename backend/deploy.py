import json
import hashlib
import boto3
from jinja2 import Environment, FileSystemLoader

jinja_env = Environment(
    loader=FileSystemLoader('./')
)

# CREATE TASK DEFINITION
ecs = boto3.client('ecs')

task_def_template = jinja_env.get_template('ecs-task-def.json')

ecs_task_def = task_def_template.render(version='latest')
ecs_task_def = json.loads(ecs_task_def)

ecs_response = ecs.register_task_definition(
    family=ecs_task_def['family'],
    executionRoleArn=ecs_task_def['executionRoleArn'],
    containerDefinitions=ecs_task_def['containerDefinitions'],
    placementConstraints=ecs_task_def['placementConstraints'],
    memory=ecs_task_def['memory'],
    requiresCompatibilities=ecs_task_def['requiresCompatibilities'],
    networkMode=ecs_task_def['networkMode'],
    cpu=ecs_task_def['cpu'],
    volumes=ecs_task_def['volumes']
)

revision = ecs_response['taskDefinition']['revision']
print(f'ECS revision: {revision}')

# CREATE DEPLOYMENT
code_deploy = boto3.client('codedeploy')

app_spec_template = jinja_env.get_template('app-spec.json')

app_spec = app_spec_template.render(revision=revision)

code_deploy_response = code_deploy.create_deployment(
    applicationName='AppECS-home-search-dashboard-home-search-dashboard-service',
    deploymentGroupName='DgpECS-home-search-dashboard-home-search-dashboard-service',
    revision={
        'revisionType': 'AppSpecContent',
        'appSpecContent': {
            'content': app_spec,
            'sha256': hashlib.sha256(app_spec.encode()).hexdigest()
        }
    }
)
print(f'Code deploy response: {code_deploy_response}')
