# via https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918

from textgenrnn import textgenrnn
t = textgenrnn()

"""
t = textgenrnn()
is fine the first time you run the script, but if you’d like to come back to it later, enter the name 
of the .hdf5 file generated. 
t=textgenrnn('weights/textgenrnn_weights.hdf5')
"""

t.train_from_file('inputs/goddess-name-wordlist.txt', num_epochs=5)
"""
num_epochs is how many times you’d like to process the file. The neural network gets better the longer 
you let it study, so start with 2 or 5 to see how long that takes, and then go up from there.
It uses the default character-by-character model
"""

"""
wordlist source:
https://en.wikipedia.org/wiki/List_of_goddesses
let l = [];Array.from(document.querySelectorAll('li')).filter(el => !/\d/.test(el.innerText)).forEach(i=> l.push(i.innerText));console.log(l)
"""
