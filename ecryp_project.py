import numpy as np
import math
import time                                                                                              # We are using this library just to presentate the output with some delays (calculation time).

print("________________________________________________________________________________________________________________________________________________________\n")
print("\t\t\tWe will find all the prime numbers less than N\n")
time.sleep(1)

                ###.     Assign values in our tools    .###

n = int(input("Give the number n: "))                                                                     # User must give the number n.
sq = math.floor(math.sqrt(n))                                                                             # Compute the square root of our given number.
marked_numbers = np.zeros(n+1)                                                                            # Create an array with n+1 zeros which we will use it to mark.
primes = []                                                                                               # Create an array to put all the prime numbers inside.

                ###.     Processing Part    .###

for i in range(n + 1):
    if(i < 2):                                                                                            # We are using an if statement to pass numbers smaller than 2 which is the first prime number.
        continue                                                                                          # If we have a number smaller number than 0 then we skip the next steps and increase the number to reach the number 2.

    if(marked_numbers[i] == 0):                                                                           # We check if we have marked number (we mark a number in the table with 1) in the array of zeros.
        primes.append(i)                                                                                  # If the number is not marked, we have a prime number so we add it in the list.

        if i <= sq + 1:                                                                                   # We are checking if the number is smaller/ equal to the square root of the given number n...
            num = 2 * i                                                                                   # then num take the value of the counter (i) multiplied by 2, which is a pointer to mark a number.  

            while num <= n:                                                                               # Because we have to check every number that is multiplied with the number that is marked, while the pointer is smaller/ equal to given number...       
                marked_numbers[num] = 1                                                                   # mark the number in the marked_numbers list (1) and...
                num = num + i                                                                             # add the pointer with the number that we know that is not a prime.

                ###.     Results    .###

time.sleep(1)
print(f"\nPrimes that are smaller or equal than n: {primes}\n")                                           # Print the output.
print("________________________________________________________________________________________________________________________________________________________\n")
