import requests
from typing import Optional, Dict, Any, Union

class MiRouter:
    def __init__(self, host: str, username: str, password: str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.token: Optional[str] = None

    def login(self) -> bool:
        url = f"http://{self.host}/cgi-bin/luci/api/xqsystem/login"
        payload = {
            "username": self.username,
            "password": self.password
        }
        response = self.session.post(url, data=payload)
        if response.status_code == 200:
            self.token = response.json().get('token')
            return True
        return False

    def get_device_list(self) -> Optional[Dict[str, Any]]:
        if not self.token:
            raise Exception("Not authenticated")
        url = f"http://{self.host}/cgi-bin/luci/;stok={self.token}/api/misystem/devicelist"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def reboot(self) -> bool:
        if not self.token:
            raise Exception("Not authenticated")
        url = f"http://{self.host}/cgi-bin/luci/;stok={self.token}/api/xqsystem/reboot"
        response = self.session.post(url)
        return response.status_code == 200

    def get_internet_status(self) -> Optional[Dict[str, Any]]:
        if not self.token:
            raise Exception("Not authenticated")
        url = f"http://{self.host}/cgi-bin/luci/;stok={self.token}/api/misystem/status"
        response = self.session.get(url)
        status = response.json()
        if status:
            return status
        return None

    def logout(self) -> None:
        if not self.token:
            raise Exception("Not authenticated")
        
        url = f"http://{self.host}/cgi-bin/luci/;stok={self.token}/api/xqsystem/logout"
        response = self.session.post(url)
        if response.status_code == 200:
            self.token = None

        return True