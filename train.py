# via https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918

from textgenrnn import textgenrnn
t = textgenrnn()
t.train_from_file('inputs/goddess-name-wordlist.txt', num_epochs=5)


"""
https://en.wikipedia.org/wiki/List_of_goddesses
let l = [];Array.from(document.querySelectorAll('li')).filter(el => !/\d/.test(el.innerText)).forEach(i=> l.push(i.innerText));console.log(l)
"""
