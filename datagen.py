from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensor2tensor.bin import t2t_datagen
import logging
import register


def main(argv):
    t2t_datagen.main(argv)


if __name__ == "__main__":
    tf.logging.set_verbosity(tf.logging.INFO)
    logging.getLogger("tensorflow").propagate = False
    tf.app.run()
