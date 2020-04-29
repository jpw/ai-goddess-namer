# ai-goddess-namer

Just me messing around with [TensorFlow 2](https://www.tensorflow.org/) to generate goddess names based on the [Wikipedia List of goddesses](https://en.wikipedia.org/wiki/List_of_goddesses). Thanks Wikipedia!

Based on [How to Train Your Own Neural Network](https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918) by [Beth Skwarecki](https://kinja.com/bethskw).  What a lovely article. Thanks Beth!

## Hello python, my old friend

You will need to set up a virtualenv.

I used python3 and did this:
 - `python3 -m venv --system-site-packages env`
 - `source env/bin/activate`

then

`which python`

..should point at the python interpreter in the env dir.

`deactivate` when done.

## Prereqs

Once you've got your venv up and running:

 - `python -m pip install --upgrade pip`
 - `python -m pip install --upgrade tensorflow`
 - if it moans about sensortools, then `python -m pip install setuptools --upgrade` and rerun the previous tensorflow install step.
    
Check the TensorFlow install:

`python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`

More info on installing TensorFlow can be found in the [TensorFlow install docs](https://www.tensorflow.org/install).

Now install `textgenrnn`:

 - `python -m pip install textgenrnn`

Now you should be good to go.

## Running

`python generate.py`

It should output some debugging info from TensorFlow & textgenrnn, and then a list of new goddess names!

Have a look at the source for more clues on how to have fun with the output.

Don't forget to `deactivate` the venv when done playing around.

## Generating your own text

First, train it. Reference your wordlist in the `train.py` script.

Run the training:
`python train.py`

That will output a `.hdf5` file. Reference _that_ file in `generate.py` then run it:
`python generate.py`


