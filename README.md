# ai-tensorflow
messing around with tensorflow

Based on [How to Train Your Own Neural Network](https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918) by [Beth Skwarecki](https://kinja.com/bethskw).

What a lovely article. Thanks Beth!

## hello python, my old friend

`source env/bin/activate`

then

`which python`

..should point at the python interpreter in the env dir.

`deactivate` when done.

## prereqs

    - `source env/bin/activate`
    - `pip install --upgrade pip`
    - `pip install --upgrade tensorflow` or, if you are having pip problems,
    - `python -m pip install --upgrade tensorflow`
    - if it moans about sensortools, then `python -m pip install setuptools --upgrade` and rerun the tensorflow install.
    
Finally check the tensorflow install:

`python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`

Re-do the tensorflow install dance, but with `textgenrnn`.

Now you should be good to go.

## running

`python generate.py`

It should output some debugging info from TensorFlow & textgenrnn, and then a list of new goddess names!

## generating your own text

First, train it. Reference your wordlist in the `train.py` script.

Run the training:
`python train.py`

That will output a `.hdf5` file. Reference _that_ file in `generate.py` then run it:
`python generate.py`