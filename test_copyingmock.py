import unittest

from copyingmock import CopyingMock


class CopyingMockTest(unittest.TestCase):

    def test_copying_mock_copies_mutable_arg(self):
        mock = CopyingMock()
        list_ = ['x', 'y']
        mock(list_)
        list_.append('z')
        with self.assertRaises(AssertionError):
            mock.assert_called_with(list_)
        mock.assert_called_with(['x', 'y'])

    def test_dynamic_attributes_use_copyingmock(self):
        mock = CopyingMock()
        self.assertIsInstance(mock.foo, CopyingMock)


if __name__ == '__main__':
    unittest.main()
