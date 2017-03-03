import tensorflow as tf
node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0)
print(node1,node2)
sess = tf.Session()
print(sess.run([node1,node2]))
'''
run result:
a@a:~/tfsrc$ python hello3.py 
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcurand.so locally
(<tf.Tensor 'Const:0' shape=() dtype=float32>, <tf.Tensor 'Const_1:0' shape=() dtype=float32>)
NVIDIA: no NVIDIA devices found
E tensorflow/stream_executor/cuda/cuda_driver.cc:491] failed call to cuInit: CUDA_ERROR_UNKNOWN
I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:140] kernel driver does not appear to be running on this host (a): /proc/driver/nvidia/version does not exist
[3.0, 4.0]
'''
