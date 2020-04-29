from textgenrnn import textgenrnn
t = textgenrnn('weights/textgenrnn_goddesses.hdf5')
t.generate(20, temperature=0.5)

"""
20 = number of things
The temperature, which is like a creativity dial. At 0.1, you’ll get very basic output that’s 
probably even more boring than what you fed in. At 1.0, the output will get so creative that 
often what comes out isn’t even real words. You can go higher than 1.0, if you dare.
"""
