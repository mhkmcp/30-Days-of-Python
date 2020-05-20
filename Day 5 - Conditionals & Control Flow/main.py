# Conditions

if True:
    print('Hi There')

if False:
    print('Nothing')

if not False:
    print('WhatsApp')

if 10 > 32 or 10 < 32:
    print('True')

if not 10 > 32:
    print('True')

if not(10 > 32):
    print('True')

if str(True).lower() == "true":
    print('Str True')

print(bool(str("true").title()))


# Control Flow

nums = [1, 2, 3, 5, 6]
nums_sq = []
for num in nums:
    number = num ** 2
    nums_sq.append(number)
print(nums_sq)

odds, evens = [], []
for num in nums_sq:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print(evens)
print(odds)

# Control Flow with While Loop

i = 0
x = 5
while i < x:
    print(i)
    i = i + 1