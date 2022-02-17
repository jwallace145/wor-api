import boto3
import moto
import pytest

AWS_REGION = "us-east-1"


@pytest.fixture
def mock_dynamodb():
    mock_dynamodb = moto.mock_dynamodb2()
    mock_dynamodb.start()
    return boto3.client("dynamodb", region_name=AWS_REGION)
