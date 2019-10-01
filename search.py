"""This is the algorithm implementation"""
#Zihang Zhou
#xx/xx/2019
import csv
import argparse

#Here start importing reads.csv file
def read_data(filename1):
    seq_d, seq_l = {}, []
    with open(filename1, mode = 'r') as csvfile1:
        reader1 = csv.reader(csvfile1)
        next(reader1)
        for rows in reader1:
            start, end = int(rows[0]), int(rows[0]) + int(rows[1])
            if (start, end) in seq_d:
                seq_d[(start, end)] += 1
            else:
                seq_d[(start, end)] = 1
        for key, value in seq_d.items():
            seq_l.append([key[0], key[1], value])
        seq_l.sort()
    return seq_l

#Here start importing loci.csv file
def read_request(filename2):
    target = []
    with open(filename2, mode='r') as csvfile2:
        reader2 = csv.reader(csvfile2)
        header = next(reader2)
        for rows in reader2:
            target.append([int(rows[0]), 0])
    return header, target

#Here start calculation
def calculation(targets, seq):
    count = 0
    for pos in targets:
    #brutal force here, maybe can find a better sort algorithm??
        for candidate in seq:
            if candidate[0] <= pos[0]:
                if candidate[1] > pos[0]:
                    count += candidate[2]
            #slight runtime improvement
            else:
                break
        pos[1] = count
        count = 0
    return targets

def write_data(filename2, title, outcome):
    with open(filename2, mode='w') as csvfile3:
        writer = csv.writer(csvfile3)
        writer.writerow(title)
        writer.writerows(outcome)

def dna_repetition_frequency(sequence, position):
    data = read_data(sequence)
    header, target = read_request(position)
    outcome = calculation(target, data)
    write_data(position, header, outcome)

if __name__  == '__main__':
    parser = argparse.ArgumentParser(description='Find dna repetition frequency')
    parser.add_argument('sequence', help='file contains dna sequence')
    parser.add_argument('position', help='file contains interest of positions')
    args = parser.parse_args()
    dna_repetition_frequency(sequence=args.sequence, position=args.position)

#optimazation and debugging
#add comment to explain everything
#Unit testing

