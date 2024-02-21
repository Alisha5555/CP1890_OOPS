from dataclasses import dataclass
from datetime import datetime, timedelta
@dataclass
class Countdown:
    now = datetime.now()
    target_datetime:datetime
    def time_left(self):
        return self.now - self.target_datetime

    def is_expired(self):
        if self.time_left() < timedelta():
            return True
        else:
            return False


