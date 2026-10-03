import unittest
from unittest.mock import patch, MagicMock
from secretMessage import print_secret_message

class TestSecretMessage(unittest.TestCase):
    @patch("secretMessage.requests.get")
    def test_print_secret_message(self, mock_get):
        # Sample HTML table with x, char, y coordinates representing letter 'F'
        sample_html = """
        <html>
            <body>
                <table>
                    <tr><th>x-coordinate</th><th>Character</th><th>y-coordinate</th></tr>
                    <tr><td>0</td><td>█</td><td>2</td></tr>
                    <tr><td>1</td><td>█</td><td>2</td></tr>
                    <tr><td>0</td><td>█</td><td>1</td></tr>
                    <tr><td>0</td><td>█</td><td>0</td></tr>
                </table>
            </body>
        </html>
        """
        mock_response = MagicMock()
        mock_response.text = sample_html
        mock_get.return_value = mock_response

        # Capture output printed to console
        with patch("builtins.print") as mock_print:
            print_secret_message("http://fake-url.com")
            
            # Print calls should output the grid line by line from y=2 down to y=0
            printed_lines = ["".join(call.args[0]) for call in mock_print.call_args_list]
            self.assertEqual(printed_lines, ["██", "█ ", "█ "])

if __name__ == "__main__":
    unittest.main()
