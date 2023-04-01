from src.db.sqlite import SQLiteWrapper
from src.utility import gen_token


class NodeManager:
    def __init__(self, db, table_name):
        self.node_db_wrapper = SQLiteWrapper(db=db, table_name=table_name)

    def create(self, name: str, description: str):
        token = gen_token()
        self.node_db_wrapper.insert(token, name, description, commit=True)
        return token

    def get(self, token):
        return self.node_db_wrapper.fetch(token=token)

    def delete(self, token):
        return self.node_db_wrapper.delete(token=token, commit=True)

    def search(self):
        return self.node_db_wrapper.filter()

    def __del__(self):
        self.node_db_wrapper.__del__()

