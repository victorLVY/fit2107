from tests.MyEventManagerTest import MyEventManagerTest
from event import Event

class TestEvent(MyEventManagerTest):
    def test_example(self):
        self.assertNotEqual("a", "b")