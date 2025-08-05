from wdsdk import client, error, request
import unittest


class ClientTests(unittest.TestCase):
  def format_query_params_test(self):
    formatted_single = request.format_query_params(["Test Lots Of Spaces"])
    self.assertEqual(formatted_single, "Test_Lots_Of_Spaces")

    formatted_multiple = request.format_query_params(["Test", "Multiple", "Params"])
    self.assertEqual(formatted_multiple, "Test!Multiple!Params")

    formatted_multiple_with_spaces = request.format_query_params(["Test Multiple", "With Spaces", "Params"])
    self.assertEqual(formatted_multiple_with_spaces, "Test_Multiple!With_Spaces!Params")

    formatted_none = request.format_query_params([])
    self.assertEqual(formatted_none, "")

    formatted_empty = request.format_query_params([""])
    self.assertEqual(formatted_empty, "")


  def create_request_test(self):
    auth_req = lambda: "auth"
    req = request.WorkdayRequest("https://test-endpoint.com", auth_req)
    self.assertDictEqual(req.params, {}) 
    self.assertEqual(req.endpoint, "https://test-endpoint.com")


  def send_methods_test(self):
    auth_req = lambda: "auth"
    req = request.WorkdayRequest("https://test-endpoint.com", auth_req)










  def is_token_expired_test(self):
    mock_not_expiring_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZXhwIjoiOTU2MzM0NDc0NjciLCJuYW1lIjoiSm9obiBEb2UiLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNzUxNjM5NTk1fQ.dIW0QVtqiw2P8TbGWeQxmnn9lw95ey4HNmRze_lfTHU"
    mock_expired_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZXhwIjoiMTEyMDQwMTA2NyIsIm5hbWUiOiJKb2huIERvZSIsImFkbWluIjp0cnVlLCJpYXQiOjE3NTE2Mzk1OTV9.PtkouBU0ktF6fCPTSqGqYXbxopTlmjQYe-tLsod-MaY"

    self.assertEqual(client.is_token_expired(mock_not_expiring_token), False)
    self.assertEqual(client.is_token_expired(mock_expired_token), True)
    self.assertRaises(error.InternalException, client.is_token_expired, "")

  def request_test(self):
    mock_client = client.RaasClient(client.IsuCredentials("id", "secret", "refresh token"), "endpoint")
    self.assertEqual(mock_client._authEndpoint, "endpoint")
    self.assertEqual(mock_client._isuCrecentials, { "client_id": "id", "client_secret": "secret", "refresh_token": "refresh_token" })

