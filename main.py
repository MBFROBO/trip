import pandas as pd
import numpy as np
import tensorflow as tf
import tensorboard, tensorboard_data_server, tensorboard_plugin_wit
from keras import optimizers
from collections import Counter, defaultdict
from matplotlib import pyplot as plt


class create_dataset:
    def __init__(self):

        self.data_ground = pd.read_csv('datasets/ground_data.csv', delimiter=';' )
        
        self.data_trip   = pd.read_csv('datasets/trip_data.csv', 
                                       on_bad_lines='skip', 
                                       delimiter=';',decimal=',')
        
    def data_ground_config(self):
        self.data_ground =np.array(self.data_ground).astype('float32')
        print(self.data_ground)
    def data_trip_config(self):

        data_trip = np.array(self.data_trip).astype('float32')
        y_train_trip = data_trip[:50,-1]
        y_test_trip = data_trip[50:,-1]
        x_train_trip = data_trip[0:50,[0,1,2]]
        x_test_trip  = data_trip[50:,[0,1,2]]
        print(x_train_trip)
        concat_x_train_trip = []
        for i in x_train_trip:
            concat_x_train_trip.append(list(i) + list(self.data_ground[0]))
        concat_x_train_trip = np.array(concat_x_train_trip).astype('float32')

        concat_x_test_trip = []
        for i in x_test_trip:
            concat_x_test_trip.append(list(i) + list(self.data_ground[0]))
        concat_x_test_trip = np.array(concat_x_test_trip).astype('float32')

        return concat_x_train_trip, concat_x_test_trip, y_train_trip, y_test_trip
    
    def print_data(self):

        print(self.data_ground)
        print(self.data_trip)

class neural_model:

    def __init__(self, X_test = None, X_train = None, 
                 y_train = None, y_test = None):

        self.input_num = 20
        self.num_hidden = 42
        self.num_hidden2 = 21
        self.num_out = 2
        self.batch_size = 15
        self.epoch = 100

        self.X_test = X_test
        self.X_train = X_train
        self.y_train = y_train
        self.y_test  = y_test

        tf.random.set_seed(5)

    def neural_model(self):

        self.weights = [
            tf.Variable(tf.random.normal([self.input_num, self.num_hidden2])),
            tf.Variable(tf.random.normal([self.num_hidden2, self.num_hidden])),
            tf.Variable(tf.random.normal([self.num_hidden, self.num_hidden2])),
            tf.Variable(tf.random.normal([self.num_hidden2, self.num_out]))
        ]

        self.biases = [ 
            tf.Variable(tf.random.normal([self.num_hidden2])),
            tf.Variable(tf.random.normal([self.num_hidden])),
            tf.Variable(tf.random.normal([self.num_hidden2])),
            tf.Variable(tf.random.normal([self.num_out]))
        ]
        
    def perceptron_model(self, dataset):

        h_l1 = tf.add(tf.matmul(dataset,self.weights[0]), self.biases[0])
        h_l1 = tf.nn.relu(h_l1)
        h_l2 = tf.add(tf.matmul(h_l1,self.weights[1]), self.biases[1])
        h_l2 = tf.nn.relu(h_l2)
        h_l3 = tf.add(tf.matmul(h_l2,self.weights[2]), self.biases[2])
        h_l3 = tf.nn.softmax(h_l3)
        out_layer = tf.add(tf.matmul(h_l3, self.weights[3]), self.biases[3])
        
        return out_layer

    def forward_pass(self,x):
        return self.perceptron_model(x)

    def loss(self):
        return tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=self.forward_pass(self.X_batch),labels=np.array(self.y_batch)))

    def learn(self):
        self.X_train = np.array(self.X_train).reshape(-1, 20)
        self.X_train = self.X_train.astype('float32')

        # self.y_train = np.array(self.y_train).reshape(-1,1)
        self.y_train = self.y_train.astype('int32')
        optimizer = optimizers.Adam(0.001)


        for epoch in range(self.epoch):

            for i in range(0,int(len(self.X_train) / self.batch_size - 1)):
                self.X_batch = self.X_train[i * self.batch_size:(i + 1) * self.batch_size]
                self.y_batch = self.y_train[i * self.batch_size: (i + 1) * self.batch_size]
                optimizer.minimize(self.loss, [self.weights,self.biases])

            self.X_batch = self.X_train[(i + 1) * self.batch_size:]
            self.y_batch = self.y_train[(i + 1) * self.batch_size:]
            optimizer.minimize(self.loss, [self.weights,self.biases])
            print('Epoch: ' + str(epoch + 1) + ' Loss: ' + str(self.loss()))

    def results(self):
        if self.X_test is not None:

            self.X_test = np.array(self.X_test).reshape(-1, 20)
            self.X_test = self.X_test.astype('float32')

            self.results = tf.nn.log_softmax(self.forward_pass(self.X_test))

            self.current_prediction = tf.argmax(self.results,1)
            self.current_prediction = np.array(self.current_prediction)
            print(self.current_prediction)

# if __name__ == '__main__':

#     cr_data = create_dataset()
#     data_ground = cr_data.data_ground_config()
#     x_train_trip, x_test_trip, y_train_trip, y_test_trip  = cr_data.data_trip_config()
#     _neural_model = neural_model(X_test=x_test_trip,
#                                  X_train= x_train_trip,
#                                  y_train= y_train_trip,
#                                  y_test= y_test_trip)
#     _neural_model.neural_model()
#     _neural_model.learn()
#     # cr_data.print_data()