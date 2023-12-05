all:
	@python3 dna.py databases/small.csv sequences/1.txt

check:
	@check50 cs50/problems/2023/x/dna
