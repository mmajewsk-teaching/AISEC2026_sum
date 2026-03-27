import unittest

from utils import create_fixed_size_chunks


class CreateFixedSizeChunksTests(unittest.TestCase):
    def test_empty_text_returns_empty_list(self):
        self.assertEqual(create_fixed_size_chunks("", chunk_size=5), [])

    def test_chunk_size_larger_than_text_returns_single_chunk(self):
        self.assertEqual(
            create_fixed_size_chunks("abc", chunk_size=10, overlap=0), ["abc"]
        )

    def test_chunks_without_overlap(self):
        text = "abcdefghij"
        self.assertEqual(
            create_fixed_size_chunks(text, chunk_size=4, overlap=0),
            ["abcd", "efgh", "ij"],
        )

    def test_chunks_with_overlap(self):
        text = "abcdefghij"
        self.assertEqual(
            create_fixed_size_chunks(text, chunk_size=4, overlap=2),
            ["abcd", "cdefgh", "ghij"],
        )

    def test_overlap_larger_than_chunk_size(self):
        text = "abcdefghij"
        self.assertEqual(
            create_fixed_size_chunks(text, chunk_size=3, overlap=5),
            ["abc", "", "bcdefghi", "efghij"],
        )


if __name__ == "__main__":
    unittest.main()
