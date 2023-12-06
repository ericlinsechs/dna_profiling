import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python3 dna.py database sequence")
        sys.exit(1)

    # Read database file into a list
    databases = []
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for STR in reader:
            databases.append(STR)
    
    # Read DNA sequence file into a variable
    seq = ""
    with open(sys.argv[2]) as f:
        reader = csv.reader(f)
        for row in reader:
            seq = row[0]

    # Read STR into a list
    sub_seq =[]
    with open(sys.argv[1]) as f:
        reader = csv.reader(f)
        sub_seq = next(reader, None)
        sub_seq = sub_seq[1:] # omit 'name'

    # Find longest match of each STR in DNA sequence
    counts = {}
    for i in range(len(sub_seq)):
        longest_run = longest_match(seq, sub_seq[i])
        counts[sub_seq[i]] = longest_run

    # Check database for matching profiles
    for profile in databases:
        name = profile['name']

        # Check if all key-value pairs match
        if all(int(profile[key]) == counts.get(key, -1) for key in profile if key != 'name'):
            print(f"{name}")
            return
    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
