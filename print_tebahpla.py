# Print the ASCII alphabet in reverse order, alternating between lowercase and uppercase
for i in range(25, -1, -1):
    if i % 2 == 1:
        # Odd index -> Uppercase letter
        print(chr(90 - i), end='')
    else:
        # Even index -> Lowercase letter
        print(chr(122 - i), end='')

# Print the final uppercase 'A' after the loop
print(chr(65), end='')