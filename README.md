# ai-tensorflow
messing around with tensorflow

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

Re-do the tensorflow install dance, but with `textgenrnn`

