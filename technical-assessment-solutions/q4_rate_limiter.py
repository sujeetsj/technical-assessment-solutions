import time
from threading import Lock


class RateLimiter:
    def __init__(self, limit=5, window=60):
        self.limit = limit
        self.window = window
        self.user_requests = {}
        self.lock = Lock()

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            if user_id not in self.user_requests:
                self.user_requests[user_id] = []

            self.user_requests[user_id] = [
                timestamp for timestamp in self.user_requests[user_id]
                if current_time - timestamp <= self.window
            ]

            if len(self.user_requests[user_id]) < self.limit:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False


if __name__ == "__main__":
    rate_limiter = RateLimiter()

    for i in range(7):
        user_id = "user1"
        if rate_limiter.allow_request(user_id):
            print(f"Request {i + 1} allowed for {user_id}")
        else:
            print(f"Request {i + 1} denied for {user_id} (rate limit exceeded)")

        time.sleep(0.1)