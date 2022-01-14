N = int(input())
secret = input()
answer = ""
for i in range(len(secret)):
    if i % N == 0:
        answer += secret[i]
print(answer)