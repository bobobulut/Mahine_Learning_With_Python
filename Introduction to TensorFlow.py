import tensorflow as tf
print("--------\n")

print(tf.version)


print("--------\n")

i = tf.ones([2,5,8])
print(i)

print("--------\n")

t = tf.zeros([9,7,5])
print(t)
print("--------\n")
t = tf.reshape(t,[3,-1])
print(t)