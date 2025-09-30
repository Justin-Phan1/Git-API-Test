import unittest
from get_repos_and_commits import getReposAndCommits

class TestGetReposAndCommits(unittest.TestCase):
    def test_commit_counts(self):
        self.user = "richkempinski"
        actual = getReposAndCommits(self.user)
        
        expected = {
            "csp": 2,
            "hellogitworld": 30,
            "helloworld": 6,
            "Mocks": 10,
            "Project1": 2,
            "richkempinski.github.io": 9,
            "threads-of-life": 1,
            "try_nbdev": 2,
            "try_nbdev2": 5,
        }

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
