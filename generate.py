from textgenrnn import textgenrnn
t = textgenrnn('weights/textgenrnn_goddesses_10its.hdf5')
generated_texts = t.generate(n=20, return_as_list=True, temperature=1.2)
print(*generated_texts, sep = "\n") 

# Using generate_samples() is a great way to test the model at different temperatures.
# textgen.generate_samples()
# https://github.com/minimaxir/textgenrnn/blob/master/docs/textgenrnn-demo.ipynb

"""
20 = number of things
The temperature, which is like a creativity dial. At 0.1, you’ll get very basic output that’s 
probably even more boring than what you fed in. At 1.0, the output will get so creative that 
often what comes out isn’t even real words. You can go higher than 1.0, if you dare.
"""
"""
first run at temp 1.5
Vancughā
Slivatle
Khiri Qabidhiku
Kr Cylzi
Phtsua Kusa
Vara-hime
Shat
Utt-tntak
Morgakne Axidanymena
Ccngaw
Taktara
Dragernahat
Mattenfá-tursidæneg Utt
Candesicalo
Nlahmith
e-qeleot-hime
Take-Mu
Pbhilu
Dziyigê Mabiena
Mrmi Arkala
"""
