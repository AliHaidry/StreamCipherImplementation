import random

# Stream Cipher coder
def stream_cipher(aray,seed):
    n = len(aray)
    random.seed(seed)
    ascii_chars = [chr(i) for i in range(255)]
    keys = random.choices(ascii_chars,k = n)
    return [chr(ord(a) ^ ord(b)) for a, b in zip(aray, keys)]

seed = 12
message = "The Sun is Moony"

msg_ciphered = stream_cipher(list(message),seed)
print(msg_ciphered)

msg_unciphered = stream_cipher(msg_ciphered,seed)
print(msg_unciphered)