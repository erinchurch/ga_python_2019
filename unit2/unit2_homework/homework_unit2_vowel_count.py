"""

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

"""

#define the list that contains the population of valid vowel letters

#define the other string that captures the user's content
#create a counter for number of vowels, set it equal to zero, it cannot be negative or greater than the number of characters provided in the user content.
# write a loop that will assess if each position in the string contains a member of the vowel list.
#increment a counter as each vowel is found.
# as the review of the string's contents concludes, print a message with how many vowels were in their content

vowel = ["a", "e", "i", "o", "u"] #define the list that contains the population of valid vowel letters
user_string = "azcbobobegghakl" #define the other string that captures the user's content
vowel_counter = 0 #create counter variable, set to 0

for i in user_string: #loop to analyze content of user
    if i in vowel: #sub if loop to check if position in user content is also in vowel list.
        vowel_counter += 1 #if true, increment counter
print(vowel_counter, "Vowels have been found in your content.") #tell user how many vowels are in their content