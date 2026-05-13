"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-10604.c267.us-east-1-4.ec2.cloud.redislabs.com',
    port=10604,
    decode_responses=True,
    username="default",
    password="SeUni1y3w1FMoIBYomtiuv5wZCuvs975",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

