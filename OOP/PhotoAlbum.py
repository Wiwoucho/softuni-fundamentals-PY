import unittest


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        return cls(photos_count // 4 + (1 if photos_count % 4 != 0 else 0))

    def add_photo(self, label):
        page_cnt = 0
        if len(self.photos[page_cnt]) < 4:
            self.photos[page_cnt].append(label)
            return f"{label} photo added successfully on page {len(self.photos)} slot {len(self.photos[page_cnt])}"
        elif len(self.photos[page_cnt]) == 4 and len(self.photos) <= self.pages:
            try:
                page_cnt += 1
                self.photos[page_cnt].append(label)
                return f"{label} photo added successfully on page {len(self.photos)} slot {len(self.photos[page_cnt])}"
            except IndexError:
                return "No more free slots"
        else:
            return "No more free slots"

    def display(self):
        result = ""
        hyphens = "-" * 11

        for index, album in enumerate(self.photos):
            cur_result = []
            for _ in album:
                cur_result.append("[]")
            if index == 0:
                result += '{0}\n{1}\n{0}\n'.format(hyphens, (' '.join(cur_result)))
            else:
                result += '{1}\n{0}\n'.format(hyphens, (' '.join(cur_result)))
        return result




class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instance(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
