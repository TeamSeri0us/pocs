import lmdb
env = lmdb.open("./train", map_size=1099511627776)
txn = env.begin(write=True)
txn.put(key = '1', value = 'aaa')
txn.put(key = '2', value = 'bbb')
txn.put(key = '3', value = 'ccc')
txn.delete(key = '1')
txn.put(key = '3', value = 'ddd')
txn.commit()
env.close()
