from typing import List, Optional, Dict


class Utils:

    @staticmethod
    def get_biggest_image_size(image_sizes: List) -> Optional[Dict]:
        best_img: Optional[Dict] = None
        best_size: int = 0
        best_type: int = 0

        for image_size in image_sizes:
            size = image_size["width"] * image_size["height"]

            _type = image_size["type"] if "type" in image_size.keys() else None
            if size < best_size and (_type is None or _type < best_type):
                continue

            best_img = image_size["url"]
            best_size = size
            best_type = _type

        return best_img
