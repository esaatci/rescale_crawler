import unittest
import utils
from unittest.mock import patch

# This should be problably be inside the testcase.
# For better readibility its placed here
mock_html = """
<div>
 <h1>
  Hello World
 </h1>
 <p1>
  This is a mock html Website for testing
 </p1>
 <div>
  <div>
   <div>
    <a href="https://google.com">
     google
    </a>
    <a href="/pictures">
     Pics
    </a>
    <a href="https://www.python.org">
     Pics
    </a>
    <a href="/cart">
     Pics
    </a>
    <a href="https://developer.mozilla.org">
     Pics
    </a>
    <a href="https://my.website.com">
     Pics
    </a>
   </div>
  </div>
 </div>
</div>
"""


class UtilsTest(unittest.TestCase):
    """
    I added a unit test for get_absolute_links
    Arguably it's the most important function in the project
    and testing it would give a high confidence
    that the project is working.

    get_html function is mocked to remove the network request and make the
    test less brittle.
    """

    @patch("utils.get_html")
    def test_getting_absolute_links_from_a_url(self, mock_get_html):
        mock_get_html.return_value = mock_html
        expected_urls = [
            "https://google.com",
            "https://www.python.org",
            "https://developer.mozilla.org",
            "https://my.website.com",
        ]
        test_url = "https://test-website.com"

        urls = utils.get_absolute_links(test_url)

        self.assertCountEqual(urls, expected_urls)
        mock_get_html.assert_called_with(test_url)


if __name__ == "__main__":
    unittest.main()
