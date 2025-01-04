import hashlib

def generate_hash(temp_id):
    """
    Gera um hash único com base em campos específicos.
    """
    hash_input = f"{temp_id}"
    return hashlib.md5(hash_input.encode()).hexdigest()