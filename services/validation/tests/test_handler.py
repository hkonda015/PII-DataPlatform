from services.validation.handler import lambda_handler

def test_lambda_handler_smoke():
    assert lambda_handler({}, None)['statusCode'] == 200
