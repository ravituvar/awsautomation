import boto3
import click

session = boto3.Session(profile_name='awscli_ravituwar')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS s3"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket_name')
def list_bucket_objects(bucket_name):
    "List all bucket objects"
    for obj in s3.Bucket(bucket_name).objects.all():
        print(obj)
if __name__ == '__main__':
    cli()
