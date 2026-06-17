# Modified protocol demonstration

a = 3

alice_secret = 5
bob_secret = 7

alice_send = alice_secret ** a
bob_send = bob_secret ** a

print("Alice sends:", alice_send)
print("Bob sends:", bob_send)

# Shared key example
shared_key_alice = bob_send * alice_secret
shared_key_bob = alice_send * bob_secret

print("Alice key:", shared_key_alice)
print("Bob key:", shared_key_bob)

print("\nEve can easily find secrets using cube root.")