import register
import tensorflow as tf
import logging
from tensor2tensor.bin import t2t_trainer


def main(argv):
    t2t_trainer.main(argv)


if __name__ == "__main__":
    tf.logging.set_verbosity(tf.logging.INFO)
    logging.getLogger("tensorflow").propagate = False
    tf.app.run()
