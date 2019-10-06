'''Makes 10 village names using pretrained model
prints to terminal using temp of 1
'''

from textgenrnn import textgenrnn
import argparse

parser = argparse.ArgumentParser(description="what's going on 'ere?")

parser.add_argument('-n', '--number', type=int, default=100),
parser.add_argument('-m', '--model', default='weights/villages_2e.hdf5'),
parser.add_argument('-t', '--temperature', type=int, default=1)
parser.add_argument('-o', '--output', default='ai_villages')

args=parser.parse_args()

textgen = textgenrnn(args.model)
villages = textgen.generate(args.number, temperature=args.temperature,
							return_as_list=True)

filename = args.output+'_temp'+str(args.temperature)+'.txt'

for ai_village in villages:
	print(ai_village)
	with open(filename ,'a') as village_file:
				village_file.write(ai_village +'\n')
