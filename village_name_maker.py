'''Makes 10 village names using pretrained model
prints to terminal using temp of 1
'''

from textgenrnn import textgenrnn

textgen = textgenrnn('data/villages_2e.hdf5')
villages = textgen.generate(10, temperature=1, return_as_list=True)

for village in villages:
	print(village)
 