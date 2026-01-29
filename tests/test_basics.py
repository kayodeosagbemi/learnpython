import unittest
import tempfile
import os

from basics import read_file_lines


class TestReadFileLines(unittest.TestCase):
    def test_reads_lines_correctly(self):
        content = "line1\nline2\n"
        # Create a temporary file with known content
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tf:
            tf.write(content)
            temp_name = tf.name

        try:
            lines = read_file_lines(temp_name)
            # read_file_lines preserves newline characters per-line
            self.assertEqual(lines, content.splitlines(keepends=True))
        finally:
            os.remove(temp_name)

    def test_raises_on_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file_lines("file_that_does_not_exist_98765.txt")


if __name__ == "__main__":
    unittest.main()
