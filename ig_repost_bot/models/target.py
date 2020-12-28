from typing import Dict, Optional

from pydantic import BaseModel


class Target(BaseModel):
    id: int
    username: str
    latest_timestamp: Dict[str, Optional[int]] = {"feed": None, "stories": None}

    def get_ig_tag(self):
        return f"<a href='https://instagram.com/{self.username}'>{self.username}</a>"
