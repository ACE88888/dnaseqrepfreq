"""
This is the dna sequence frequency search algorithm implementation
Zihang Zhou
10/02/2019
"""
import csv
import argparse

class Dnafreq:
    """
    Contain methods to extract and pre-process data, search target position's appearance
    frequency, and export result.
    """
    @classmethod
    def read_data(cls, filename1):
        """Here start importing reads.csv file"""
        seq_d, seq_l = {}, []
        with open(filename1, mode='r') as csvfile1:
            reader1 = csv.reader(csvfile1)
            next(reader1) # Skip first row because it does not contain dna position data
            for rows in reader1:
                start, end = int(rows[0]), int(rows[0])+int(rows[1])-1
                if (start, end) in seq_d:
                    seq_d[(start, end)] += 1
                else:
                    seq_d[(start, end)] = 1 # Use dictionary to extract data
            for key, value in seq_d.items():
                seq_l.append([key[0], key[1], value]) # Convert data from dict to list
            seq_l.sort() # Sort data based on dna starting position first, then ending position
        return seq_l

    @classmethod
    def read_request(cls, filename2):
        """Here start importing loci.csv file"""
        target = []
        with open(filename2, mode='r') as csvfile2:
            reader2 = csv.reader(csvfile2)
            header = next(reader2) # Store info of dna data variable
            for rows in reader2:
                target.append([int(rows[0]), 0]) # Set coverage initially to 0
        return header, target

    @classmethod
    def calculation(cls, targets, seq):
        """Here start calculation"""
        count = 0
        for pos in targets:
            for candidate in seq:
                if candidate[0] <= pos[0]:
                    if candidate[1] >= pos[0]:
                        count += candidate[2] # Coverage updating
                else: # When finished for a candidate, go for the next candidate
                    break
            pos[1] = count # Update target dna coverage
            count = 0
        return targets

    @classmethod
    def write_data(cls, filename2, title, outcome):
        """Here start exporting data"""
        with open(filename2, mode='w') as csvfile3:
            writer = csv.writer(csvfile3)
            writer.writerow(title)
            writer.writerows(outcome)

    @classmethod
    def dna_repetition_frequency(cls, sequence, position):
        """This is main()"""
        data = cls.read_data(sequence)
        header, target = cls.read_request(position)
        outcome = cls.calculation(target, data)
        cls.write_data(position, header, outcome)

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Find dna repetition frequency')
    PARSER.add_argument('sequence', help='file contains dna sequence')
    PARSER.add_argument('position', help='file contains interest of positions')
    ARGS = PARSER.parse_args()
    DNAFREQ = Dnafreq()
    DNAFREQ.dna_repetition_frequency(sequence=ARGS.sequence, position=ARGS.position)
