from pymongo import MongoClient

# 레플리카 셋의 연결 문자열 구성
replica_set = "rs0"
username = "keti_root"
password = "madcoder"
auth_source = "admin"


# MongoDB 클라이언트 생성
# client = MongoClient("mongodb://bigsoft.iptime.org:55427,bigsoft.iptime.org:55428/?replicaSet=rs0")
# MongoDB 클라이언트 생성
client = MongoClient(
    "mongodb://keti_root:madcoder@bigsoft.iptime.org:55427,bigsoft.iptime.org:55428/?replicaSet=rs0&authSource=admin"
)

# 'testdb' 데이터베이스 선택
db = client.testdb

# 'sample_collection' 컬렉션 선택
collection = db.sample_collection

# 삽입할 데이터
data = {"name": "Alice", "age": 30, "city": "New York"}

# 데이터 삽입
result = collection.insert_one(data)