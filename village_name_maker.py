'''Makes village names using pretrained model
prints to terminal using temp of 1
'''

from textgenrnn import textgenrnn
import argparse

parser = argparse.ArgumentParser(description="what's going on 'ere?")

parser.add_argument('-n', '--number', type=int, default=100),
parser.add_argument('-m', '--model', default='weights/villages_4e.hdf5')
parser.add_argument('-t', '--temperature', type=float, default=1.0)
parser.add_argument('-o', '--output', default='ai_villages')
parser.add_argument('-r', '--reference', 
						default='data/english_village_names.txt')

#Initialises
args=parser.parse_args()
output_filename = 'output/'+args.output+'_temp'+str(args.temperature)+'.txt'
real_villages = [village.strip() for village in
					open(args.reference).readlines()]

#Loads Neural Net and generates names
textgen = textgenrnn(args.model)
villages = textgen.generate(args.number, temperature=args.temperature,
							return_as_list=True)

#Saves Names
for ai_village in sorted(villages):
	if ai_village not in real_villages:
		print(ai_village)
		with open(output_filename ,'a') as village_file:
					village_file.write(ai_village +'\n')

#Tidies name file
out = sorted([v for v in open(output_filename).readlines()])
with open(output_filename,'w') as outfile:
	for o in out:
		outfile.write(o)
