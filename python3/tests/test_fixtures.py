import fixtures
import os


class TestEnviron(fixtures.TestWithFixtures):
    def test_environ(self):
        fixture = self.useFixture(
            fixtures.EnvironmentVariable("FOOBAR", "42"))
        self.assertEqual(os.environ.get("FOOBAR"), "42")

    def test_environ_no_fixture(self):
        self.assertEqual(os.environ.get("FOOBAR"), None)

