from typing import Optional

class OAuthUserInfo:
    def __init__(self, email: str, name: Optional[str], profile_image: Optional[str]):
        self.email = email
        self.name = name
        self.profile_image = profile_image
