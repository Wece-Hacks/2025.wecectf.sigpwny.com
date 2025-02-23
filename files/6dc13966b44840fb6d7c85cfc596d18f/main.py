
# to learn more about RSA encryption, check out the following link: 
# https://www.youtube.com/watch?v=wcbH4t5SJpg

# HINT: use "pip install sympy" to use the mod_inverse function
from sympy import mod_inverse 

# given values p, q, and e for RSA encryption
p = 61
q = 53
e = 17

# decrypt each character in the message to get the flag
# HINT: it should be a link
encrypted_chars = [2170, 884, 884, 612, 1230, 436, 501, 501, 487, 2185, 2160, 884, 2160, 2825, 2570, 1313, 501, 669, 2653, 1632, 2570, 2160, 1627, 2578, 2718, 1369, 1830, 1230]