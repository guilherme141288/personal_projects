from hashlib import sha256
import json
import time

chain = [
	{
		"remetente": "Pedro henrique",
       		"destinatario": "Teste",
       		"mensagem": "200 Reais"
	},
	{
		"remetente": "TESTE",
	       	"destinatario": "Joao",
       		"mensagem": "20000 Reais"
	}
]

block_chain = []

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        else:
            return super().default(obj)

def get_time():
	return time.time()

def Hashdif(hash, difficulty):
	count = 0
	for i in hash:
		count += 1
		if(i != '0'):
			break
	return count > difficulty

def generateHash(block):
	starts = 0
	block["nonce"] = starts
	hash = sha256(json.dumps(block, cls=CustomEncoder).encode()).hexdigest()
	while(not Hashdif(hash, 4)):
		starts = starts + 1
		block["nonce"] = starts
		hash = sha256(json.dumps(block, cls=CustomEncoder).encode()).hexdigest()
	return hash


def NewBlock(block):
	if(len(block_chain) == 0):
		block["timestamp"] = get_time()
		block["hash"] = generateHash(block)
	else:
		block["timestamp"] = get_time()
		last_block = block_chain[-1]
		block["last_hash"] = last_block["hash"]
		block["hash"] = generateHash(block)
	block_chain.append(block)

for c in chain:
	NewBlock(c)

print(block_chain)