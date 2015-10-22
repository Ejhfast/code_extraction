# Python newbie @patch decorator issue
@patch('provider.Provider', autospec=True)
def test_init(self, mock_provider):
    pass
