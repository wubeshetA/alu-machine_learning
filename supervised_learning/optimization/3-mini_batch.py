#!/usr/bin/env python3
""" Train Mini-Batch"""

import tensorflow as tf
import numpy as np
shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32,
                     epochs=5, load_path="/tmp/model.ckpt",
                     save_path="/tmp/model.ckpt"):
    """ trains a loaded neural network model using mini-batch gradient descent

    Args:
        X_train (np.array): matrix of shape (m, 784) containing
        the training data
        Y_train (np.array): one-hot matrix of shape (m, 10)
        containing the training labels
        X_valid (np.array): matrix of shape (m, 784) containing
        the validation data
        Y_valid (np.array): one-hot matrix of shape (m, 10) containing the
        validation labels
        batch_size (int): number of data points in a batch
        epochs (int): number of times the training should pass through the
        whole dataset
        load_path (str): path from which to load the model
        save_path (str): path to where the model should be saved
    Returns:
        str: the path where the model was saved
    """

    tf.reset_default_graph()
    with tf.Session() as sess:

        # load graph
        saver = tf.train.import_meta_graph(load_path + '.meta')
        saver.restore(sess, load_path)

        # Get tensors and ops
        x = tf.get_collection('x')[0]
        y = tf.get_collection('y')[0]
        accuracy = tf.get_collection('accuracy')[0]
        loss = tf.get_collection('loss')[0]
        train_op = tf.get_collection('train_op')[0]

        batch = X_train.shape[0] // batch_size
        if X_train.shape[0] % batch_size != 0:
            batch += 1  # add 1 if there are remaining data points
        for epoch in range(epochs+1):

            train_cost, train_accuracy = sess.run(
                [loss, accuracy], feed_dict={x: X_train, y: Y_train})
            valid_cost, valid_accuracy = sess.run(
                [loss, accuracy], feed_dict={x: X_valid, y: Y_valid})

            print("After {} epochs:".format(epoch))
            print("\tTraining Cost: {}".format(train_cost))
            print("\tTraining Accuracy: {}".format(train_accuracy))
            print("\tValidation Cost: {}".format(valid_cost))
            print("\tValidation Accuracy: {}".format(valid_accuracy))

            if epoch < epochs:
                X_train, Y_train = shuffle_data(X_train, Y_train)
                for i in range(batch):
                    # # print every 100 steps
                    # if step % 100 == 0:
                    #     print(i)
                    start = i * batch_size
                    end = start + batch_size
                    x_batch = X_train[start:end]
                    y_batch = Y_train[start:end]
                    # Train the model
                    step_cost, step_accuracy = sess.run(
                        [loss, accuracy], feed_dict={x: x_batch, y: y_batch})
                    if i % 100 == 0 and i > 0:

                        print("\tStep {}: ".format(i))
                        print("\t\tCost: {}".format(step_cost))
                        print("\t\tAccuracy: {}".format(step_accuracy))

        save_path = saver.save(sess, save_path)
    return save_path
