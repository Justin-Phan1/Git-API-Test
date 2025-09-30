import unittest
from unittest import mock
from unittest.mock import patch, Mock
from get_repos_and_commits import getReposAndCommits

class TestGetReposAndCommits(unittest.TestCase):
    @mock.patch("requests.get")
    def test_commit_counts_with_side_effect(self, mocked_get):
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

        repo_list = [{'name': name} for name in expected]
        commit_lists = [
            [{'sha': 'dummy'}] * count for count in expected.values()
        ]
        mocked_get.side_effect = [Mock(json=lambda: repo_list)] + [
            Mock(json=lambda data=commits: data) for commits in commit_lists
        ]

        actual = getReposAndCommits("richkempinski")
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
