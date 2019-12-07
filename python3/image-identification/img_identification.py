#常用的构建神经网络模型的框架
import tensorflow as tf
#可以高效处理数组的的模块
import numpy as np
#python中用于记录时间的模块
import time
#用于对文件进行操作的模块
import os

#华为云ModelArts团队自研的分布式训练加速框架
## import moxing as mox
#将os的操作转换为moxing的操作，提高效率
## mox.file.shift('os', 'mox')

#tensorflow中用于快速构建模型的模块
slim=tf.contrib.slim
#根据自己情况进行修改，实验第一步生成的TFRecord文件存储位置
train_data='image_data/train(2055).tfre'
validation_data='image_data/validation(514).tfre'
test_data='image_data/test(1101).tfre'

#接收参数为解码后的图像数组，处理后的图像尺寸，即神经网络的输入大小
#然后是训练标签，针对训练和预测进行区分
def preprocess_for_train(image,height,width,is_train=True):
    
    #获取图像处理后需要的尺寸
    height=height
    width=width
    #获取图像数组
    image=image

    # (?, ?, ?)
    # print(">>> image: ", image.shape)
    
    #如果是训练，则先把图像处理成比神经网络输入更大的尺寸
    #然后从中随机截取神经网络要求的输入尺寸，这里选择尺寸比需要的大1.2倍
    crop_height=int(height*1.2)
    crop_width=int(width*1.2)
    #转换图像数组的类型，统一为float32，方便显卡进行高效计算
    if image.dtype !=np.float32:
        image=tf.image.convert_image_dtype(image,dtype=tf.float32)

    #当训练标签为真时，进行图像数据增强操作
    if is_train==True:
        #tensorflow提供了四种方法更改图像大小，随机选择一种
        random_image=tf.image.resize_images(image,[crop_height,crop_width],method=np.random.randint(4))

        #随机左右翻转图像
        random_image=tf.image.random_flip_left_right(random_image)

        #随机调整图像亮度
        random_image=tf.image.random_brightness(random_image,max_delta=63)

        #随机调整图像对比度
        random_image=tf.image.random_contrast(random_image,lower=0.2,upper=1.8)

        #随机截取我们要求的图像尺寸
        random_image=tf.random_crop(random_image,[height,width,3])
        # print(">>> random_image: ", type(random_image))
            
        #减去图像均值和除以方差，对图像归一化
        random_image=tf.image.per_image_standardization(random_image)

        #数值归一化，将所有数值限制在0-1之间，训练收敛速度更快
        return tf.clip_by_value(random_image,0.0,1.0)

    #当训练标签为假时，仅对图像进行标准化操作
    else:
        #更改图像大小
        random_image=tf.image.resize_images(image,[height,width],method=np.random.randint(4))
        #这一步的宽高与上一步一样，不会对图像进行裁剪
        #但是为了避免无关因素对模型的影响，还是加上这一步
        random_image=tf.random_crop(random_image,[height,width,3])
        #减去图像均值和除以方差，对图像归一化
        random_image=tf.image.per_image_standardization(random_image)
        #数值归一化，将所有数值限制在0-1之间，与训练过程一致
        return tf.clip_by_value(random_image,0.0,1.0)

#接收TFRecord文件存放位置以及训练标签
def read_and_decode(filename,is_train=False):
    #创建文件输入队列，可以接收多个文件列表，这里我们只有一个
    filename_queue=tf.train.string_input_producer([filename])
    #创建一个reader用来读取TFRecord文件
    reader=tf.TFRecordReader()
    #从TFRecord文件中读取数据
    _,serialized_example=reader.read(filename_queue)
    #使用预置的格式对数据进行解析
    features=tf.parse_single_example(serialized_example,
                                     features={
                                         'height': tf.FixedLenFeature([], tf.int64),
                                         'width': tf.FixedLenFeature([], tf.int64),
                                         'depth': tf.FixedLenFeature([], tf.int64),
                                         'label': tf.FixedLenFeature([], tf.int64),
                                         'image_raw': tf.FixedLenFeature([], tf.string),

                                    })
    '''
    数据在内存中是连续存储的，如果解码时数据类型不对的话，
    则解析出来的数据也不对，比如6个int类型数据，如果按float解析的话，
    可以解析出3个数据，不会报错，但是结果不是我们想要的
    
    '''
    #这里是第一部分实验使用Image打开的图像，数据类型为uint8
    image=tf.decode_raw(features['image_raw'],tf.uint8)
    #这里的话是单个数值，我们转化数据类型，不涉及解析
    height=tf.cast(features['height'],tf.int32)
    width=tf.cast(features['width'],tf.int32)
    depth=tf.cast(features['depth'],tf.int32)
    #根据图像宽高信息，还原图像
    image = tf.reshape(image, [height, width, depth])
    #获取图像标签
    label=features['label']
    #如果是训练数据，则进行图像增强，随后返回图像数据和标签数据
    if is_train==True:
        image=preprocess_for_train(image,128,128,True)
        return image,label

    #如果不是训练数据，只进行图像预处理，随后返回图像数据和标签数据
    elif is_train==False:
        image=preprocess_for_train(image,128,128,False)
        return image,label

#在gpu环境下，batch_size越大，训练越快，属于超参数，可根据实际情况调整
batch_size=32
#定义队列执行出栈操作后队列最小保留数据
min_after_dequeue=1000
#定义队列容量
capacity=min_after_dequeue+6*batch_size
#创建默认会话，config这里是为了更好的兼容性，
#可以在gpu不可用的情况下，把gpu上的运算放到cpu上
sess=tf.InteractiveSession(config=tf.ConfigProto(allow_soft_placement=True))

#读取训练数据和验证数据
x_train_,y_train_=read_and_decode(train_data,True)
x_validation_,y_validation_=read_and_decode(validation_data,False)
x_test_,y_test_=read_and_decode(test_data,False)

#将数据变为可训练的batch并打乱
x_train_batch,y_train_batch=tf.train.shuffle_batch([x_train_,y_train_],batch_size=batch_size,
                                                   capacity=capacity,min_after_dequeue=min_after_dequeue,num_threads=32)
x_validation_batch,y_validation_batch=tf.train.batch([x_validation_,y_validation_],batch_size=batch_size,capacity=capacity,num_threads=32)

x_test_batch,y_test_batch=tf.train.batch([x_test_,y_test_],batch_size=batch_size,capacity=capacity,num_threads=32)

#模型可以理解为一个复杂函数，函数需要一个输入，inputs
#同时函数会给出一个输出，labels代表正确输出
#train，regularizer用于控制函数的结构
def inception(inputs,labels,train,regularizer):
    #获取输入参数
    inputs=inputs
    labels=labels
    train=train
    regularizer=regularizer

    #创建一个变量空间，reuse用来保证在变量空间没有当前变量的时候新建变量，存在的时候复用变量
    with tf.variable_scope('inception',reuse=tf.AUTO_REUSE):

        #创建一个slim的参数空间，包括卷积，最大池化，平均池化操作，默认步长为1，padding为same
        with slim.arg_scope([slim.conv2d,slim.max_pool2d,slim.avg_pool2d],stride=1,padding='SAME'):

            #创建第一个分支，卷积核为1x1的卷积层，因为输入的图像为128x128，
            #故此处输出为None x128x128x64，None表示输入的图像个数，即batch_size大小
            with tf.variable_scope('branch_0'):
                # branch_0=slim.conv2d(inputs,64,[1,1],scope='conv_1')
                branch_0=slim.conv2d(inputs,64,[3,3],scope='conv_1')

            #创建第二个分支，一个卷积层的卷积核为1x1，另一个为3x3，因为步长为1，输出还是None x128x128x64
            with tf.variable_scope('branch_1'):
                # net=slim.conv2d(inputs,64,[1,1],scope='conv_2')
                net=slim.conv2d(inputs,64,[3,3],scope='conv_2')
                branch_1=slim.conv2d(net,64,[3,3],scope='conv_3')

            #创建第三个分支，还是两个卷积层，输出同上
            with tf.variable_scope('branch_2'):
                net=slim.conv2d(inputs,64,[3,3],scope='conv_4')
                # net=slim.conv2d(inputs,64,[1,1],scope='conv_4') 
                branch_2=slim.conv2d(net,64,[5,5],scope='conv_5')

            #创建第四个分支，包含一个最大池化和一个卷积层，因为步长为1，所以池化层不会缩减图像大小，输出同上
            with tf.variable_scope('branch_3'):
                net=slim.max_pool2d(inputs,[3,3],scope='maxpool_1')
                branch_3=slim.conv2d(net,64,[3,3],scope='conv_6')

            #创建一个主支，将前面分支合到一起
            with tf.variable_scope('main_1'):
                #融合前面的四个分支，注意要指定链接维度，这里的输出为None x128x128x（64x4）
                mixed=tf.concat([branch_0, branch_1,branch_2,branch_3], 3)

                #卷积的同时缩减feature map厚度，此处输出为None x128x128x128
                net=slim.conv2d(mixed,128,[1,1],scope='conv_7')

                #指定步长，使用最大池化进行缩减，此处输出为None x32x32x128
                net=slim.max_pool2d(net,[4,4],stride=4,scope='maxpool_2')

                #指定步长，卷积的同时缩减feature map大小，此处输出为None x16x16x128
                net=slim.conv2d(net,128,[5,5],stride=2,scope='conv_8')

                #输出为None x8x8x128
                net=slim.conv2d(net,128,[3,3],stride=2,scope='conv_9')

                #输出为None x8x8x64
                net=slim.conv2d(net,64,[1,1],scope='conv_10')

                #将输出维度转换为列表
                net_shape=net.get_shape().as_list()

                #第一个维度为None，从第二个维度开始，nodes为8x8x64=4096
                nodes=net_shape[1]*net_shape[2]*net_shape[3]

                #打印输出形状
                print(net_shape[1],net_shape[2],net_shape[3])
                #获取将feature map展开之后的数据个数，这里输出为None，4096

                reshaped=tf.reshape(net,[-1,nodes])
                #打印展开之后的feature map形状
                print('shape of reshaped:',reshaped.shape)

            #定义第一层全连接层
            with tf.variable_scope('fc1'): 
                #定义第一层全连接层的权重，形状为feature map展开之后的nodes与512相乘，512为这一层的节点数
                fc1_weights = tf.get_variable("weight", [nodes, 512],initializer=tf.truncated_normal_initializer(stddev=0.1))  

                # 给全连接层的权重添加正则项，tf.add_to_collection函数可以把变量放入一个集合，把很多变量变成一个列表
                if regularizer != None: tf.add_to_collection('losses', regularizer(fc1_weights))                                

                #设置偏置项，对应节点数
                fc1_biases = tf.get_variable("bias", [512], initializer=tf.constant_initializer(0.1))  
                #添加激活函数
                fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)

                #如果是训练过程，加入dropout，保留70%的节点，防止过拟合
                if train: fc1 = tf.nn.dropout(fc1, 0.7)                                                                        

            #定义第二层全连接层，基本同上
            with tf.variable_scope('fc2'):
                fc2_weights = tf.get_variable("weight", [512, 256],initializer=tf.truncated_normal_initializer(stddev=0.1))
                if regularizer != None: tf.add_to_collection('losses', regularizer(fc2_weights))
                fc2_biases = tf.get_variable("bias", [256], initializer=tf.constant_initializer(0.1))
                fc2 = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)
                if train: fc2 = tf.nn.dropout(fc2, 0.7)

            #定义输出层
            with tf.variable_scope('fc3'):
                #因为预测结果为5类，因此这里输出层节点数为5
                fc3_weights = tf.get_variable("weight", [256, 5],
                                              initializer=tf.truncated_normal_initializer(stddev=0.1))
                if regularizer != None: tf.add_to_collection('losses', regularizer(fc3_weights))
                fc3_biases = tf.get_variable("bias", [5], initializer=tf.constant_initializer(0.1))
                #得到最终预测结果
                logits = tf.matmul(fc2, fc3_weights) + fc3_biases

        #为后面模型结构保存做准备
        if labels==None:
            return logits
        else:
            #定义损失函数 
            #将预测结果与实际标签进行比较后计算损失函数，这里损失函数将softmax与交叉熵融合
            #得到符合该模型结构的损失函数
            ince_loss=tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=labels)
            #将损失函数加入losses集合，实现正则化
            tf.add_to_collection("losses",ince_loss)
            #获取包含了权重值的损失函数
            loss=0
            for each in tf.get_collection("losses"):
                loss+=each
                #返回预测结果和损失函数
            return logits ,loss 


#进一步封装函数，调用该函数可直接获取给定输入值的模型损失函数
#最小化损失函数的过程即模型训练过程
def get_inception_model(x_batch,y_batch):
    #获取传递参数
    x_batch=x_batch
    y_batch=y_batch

    #定义正则化参数
    regularizer = tf.contrib.layers.l2_regularizer(0.001)  

    #传递正则化参数之后得到预测结果和损失函数
    logits ,loss= inception(x_batch,y_batch,True,regularizer) 

    #tf.argmax取得预测值中概率最大的角标，比如[0.1,0.2,0.7]则取2,1代表维度为1，
    #因为0维是None，代表样本数量
    #然后将角标转换为int64格式之后与标签值进行比较，因为标签值类型为int64
    #返回布尔型的列表
    correct_prediction = tf.equal(tf.cast(tf.argmax(logits,1),tf.int64), y_batch) 
    #True转换为1，False为0，得到最终模型准确率
    acc= tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    #返回损失函数和准确率
    return loss,acc


#获取训练模型所需的损失值，准确率为次要的
train_loss_,train_acc_=get_inception_model(x_train_batch,y_train_batch)
#获取验证模型所需的准确率，评估模型好坏，损失值次要的
validation_loss_,validation_acc_=get_inception_model(x_validation_batch,y_validation_batch)
#定义优化器
optimizer=tf.train.AdamOptimizer(learning_rate=0.001)

#利用优化器来最小化训练误差，完成模型训练
train_op=optimizer.minimize(train_loss_) 
#定义训练周期，所有训练数据训练一遍为一个周期

n_epoch=20
#定义一个周期需要训练几个batch_size，即训练几个batch_size能过完一遍训练数据，
#需要知道样本数量，存储的时候样本数量写在文件名上了，2055
n_step_epoch=int(2055/batch_size)
#整个训练需要训练几个batch_size
n_step=n_epoch*n_step_epoch
#打印频率，即多久打印一次训练信息
print_freq=1
#初始化全局变量
sess.run(tf.global_variables_initializer())
#启动多线程协同模块
coord=tf.train.Coordinator()
#启动所有线程
threads=tf.train.start_queue_runners(sess=sess,coord=coord)
#定义全局训练步数
step=0

# create for to use tf board
# tf.summary.FileWriter("summary_dir", sess.graph)
# print("graph writed")

#根据epoch数量开始循环进行训练
for epoch in range(n_epoch):
    #记录每个epoch的训练时长
    start_time=time.time()
    #用于记录每个epoch的损失，准确率和batch_size数量
    train_loss, train_acc, n_batch = 0, 0, 0 
    #根据每个epoch的batch_size数量开始循环进行训练
    for s in range(n_step_epoch):
        #run后面的train_op为训练过程，其余两个获取当前batch_size的损失值和准确率，用于显示训练过程
        _,err,ac=sess.run([train_op,train_loss_,train_acc_])
        #每完成一个batch_size,全局步数step加一，当前epoch内步数加一，累加损失值和准确率
        train_loss += err; train_acc += ac; n_batch += 1;step+=1
        #第一轮和符合打印频率的epoch打印训练信息
    if epoch==0 or (epoch+1)%print_freq==0:
        #显示训练的第几个epoch，总步数的几步到几步，以及耗费时间
        print('epoch%d step%d-%d of %d took %fs'%(epoch,step-n_step_epoch,step,n_step,time.time()-start_time))
        #取平均，显示当前epoch内的平均损失值和准确率
        print("   train loss: %f" % (np.sum(train_loss)/ n_batch))                          
        print("   train acc: %f" % (np.sum(train_acc)/ n_batch)) 

        #显示验证集的损失值和准确率
        validation_loss,validation_acc,n_batch=0,0,0
        for _ in range(int(514/batch_size)):
            err,ac=sess.run([validation_loss_,validation_acc_])
            validation_loss+=err;validation_acc+=ac;n_batch+=1
            print('validation loss:%f' % (np.sum(validation_loss)/n_batch))
            print("validation_acc: %f" % (np.sum(validation_acc)/ n_batch))
