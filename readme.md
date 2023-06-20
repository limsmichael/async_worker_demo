# Introduction
This is an async producer-consumer template that uses a queue to hand off the work.

# Usage
Run the `main.py`.  Experiment with the variable `n_workers` and the `Producer.limit`.

In order to adapt to more specific purposes, change the data placed in the queue by `Producer.put_work` method.
Likewise change the `Consumer.process_work` method.
