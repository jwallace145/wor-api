import pytest
from dataclasses import dataclass
from mypy_boto3_dynamodb import DynamoDBClient

from src.aws_gateways.dynamodb_gateway import DynamoDbGateway


@dataclass
class TestDynamoDbGateway:

    TEST_DYNAMODB_TABLE = "testtable"
    TEST_USER_EMAIL = "testuser@test.com"

    @pytest.fixture(autouse=True)
    def init_test_dynamodb_gateway(self, mock_dynamodb: DynamoDBClient):
        mock_dynamodb.create_table(
            AttributeDefinitions=[{"AttribueName": "email", "AttributeType": "S"}],
            TableName=self.TEST_DYNAMODB_TABLE,
            KeySchema=[{"AttributeName": "email", "KeyType": "HASH"}],
        )
        mock_dynamodb.put_item(
            TableName=self.TEST_DYNAMODB_TABLE,
            Item={
                "phone_number": {"S": "0123456789"},
                "strike_prices": {
                    "L": [
                        {
                            "M": {
                                "symbol": {"S": "MSFT"},
                                "sell_price": {"N": "350"},
                                "buy_price": {"N": "300"},
                            }
                        },
                        {
                            "M": {
                                "symbol": {"S": "AAPL"},
                                "sell_price": {"N": "200"},
                                "buy_price": {"N": "150"},
                            }
                        },
                    ]
                },
                "email": {"S": self.TEST_USER_EMAIL},
            },
        )
        self.dynamodb_gateway = DynamoDbGateway(client=mock_dynamodb)

    def test_get_strike_prices(self):
        strike_prices = self.dynamodb_gateway.get_strike_prices(
            email=self.TEST_USER_EMAIL
        )
        assert len(strike_prices) == 2
