from wdsdk import client, error
import unittest


class ClientTests(unittest.TestCase):
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

