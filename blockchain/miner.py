import hashlib
import requests
import json
import sys

from uuid import uuid4

from timeit import default_timer as timer
import time
import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """
    print(f"last_proof: {last_proof}")
    start = timer()

    print("Searching for next proof")
    proof = 0
    #  TODO: Your code here
    while valid_proof(last_proof, proof) is False:
        proof  += 1
    end_time = time.time()
    print(f"TIME: {end_time - start}")

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """
    print(f"last_hash: {last_hash}")
    # TODO: Your code here!
    guess = f'{last_hash}{proof}'
    print(f"guess: {guess}")
    #check_guess = hashlib.sha256(guess.encode()).hexdigest()
    check_guess = hash(guess)
    print(f"check_guess: {check_guess}")
    last_six = json.dumps(last_hash)[-6:]
    print(f"last_six: {last_six}")
    check_guess_str = json.dumps(check_guess)
    print(f"cg_fs: {check_guess_str[:6]}")
    if check_guess_str[:6] == last_six:
        
        print(f"sending combination... block_string: {last_hash} + proof: {proof}  = {check_guess}")
        
        return check_guess
    else:
        return False


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
            break
        else:
            print(data.get('message'))
