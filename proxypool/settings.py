# Redis host
REDIS_HOST = '127.0.0.1'

# Redis port
REDIS_PORT = 6379

# Redis password
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# Proxy score
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 5

VALID_STATUS_CODES = [200, 302]

# Proxy amount threshold
POOL_UPPER_THRESHOLD = 50000

# Test cycle
TESTER_CYCLE = 20
# Getter cycle
GETTER_CYCLE = 300

# Test API
# It depends on which website to crawl
TEST_URL = 'http://www.baidu.com'

# API settings
API_HOST = '127.0.0.1'
API_PORT = 5555

# Switch
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# Maximum for each batch of tests
BATCH_TEST_SIZE = 10