import redis


redis_client = redis.Redis(
    host="redis-16734.crce219.us-east-1-4.ec2.cloud.redislabs.com:16734",
    port=11848,
    password="***",
)

try:
    connection_status = redis_client.ping()
    if connection_status:
        print("Connected to Redis!")
    else:
        print("The connection to Redis was unsuccessful!")
except redis.ConnectionError as ex:
    print("An error ocurred while connecting to Redis: ", ex)