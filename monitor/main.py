import time
import requests
import threading
from logger import get_logger
from prometheus_client import start_http_server, Gauge

logger = get_logger()

URLS = [
    "https://httpstat.us/503",
    "https://httpstat.us/200"
]

url_up = Gauge('sample_external_url_up', 'Whether the external URL is up (1) or down (0)', ['url'])
url_response_ms = Gauge('sample_external_url_response_ms', 'Response time of the external URL in ms', ['url'])

def check_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        elapsed_ms = (time.time() - start) * 1000
        url_up.labels(url=url).set(1 if response.status_code == 200 else 0)
        url_response_ms.labels(url=url).set(elapsed_ms)
        logger.info(f"Checked {url} - Status: {response.status_code}, Time: {elapsed_ms:.2f} ms")
    except requests.RequestException as e:
        url_up.labels(url=url).set(0)
        url_response_ms.labels(url=url).set(0)
        logger.error(f"Error checking {url}: {e}")

def run_checks():
    while True:
        for url in URLS:
            check_url(url)
        time.sleep(10)

if __name__ == '__main__':
    start_http_server(8000)
    thread = threading.Thread(target=run_checks)
    thread.start()
