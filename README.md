[//]: # (Image References)

[image1]: ./images/sample_dog_output.png "Sample Output"
[image2]: ./images/vgg16_model.png "VGG-16 Model Keras Layers"
[image3]: ./images/vgg16_model_draw.png "VGG16 Model Figure"


## 项目概述

在卷积神经网络（CNN）项目中，将学到如何建立一个处理现实生活中的，用户提供的图像的算法。给你一个狗的图像，你的算法将会识别并估计狗的品种，如果提供的图像是人，代码将会识别最相近的狗的品种。在学习用于分类的最先进的 CNN 模型的同时，你将会为用户体验做出重要的设计与决定。

我们的目标是，通过将一系列模型拼接在一起，设计数据处理管道完成各式各样的任务所面临的挑战。了解每个模型都有它的优点与缺点，并且设计实际应用时，经常会面对解决许多没有最优解的问题。


## 项目指南

### 步骤

1. 克隆存储库并打开下载的文件夹。

 ```	
git clone https://github.com/udacity/cn-deep-learning.git
cd cn-deep-learning/dog-project
```

2. 下载[狗狗数据集](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/v4-dataset/dogImages.zip) ，并将数据集解压大存储库中，地点为`项目路径/dogImages`. 

3. 下载[人类数据集](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/v4-dataset/lfw.zip)。并将数据集解压大存储库中，位置为`项目路径/lfw `。

4. 为狗狗数据集下载 [VGG-16关键特征](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/v4-dataset/DogVGG16Data.npz) 并将其放置于存储库中，位置为`项目路径/bottleneck_features `。

5. 安装必要的 Python 依赖包


	对于 __Mac/OSX__：
	
	```bash
	conda env create -f requirements/dog-mac.yml
	source activate dog-project
	KERAS_BACKEND=tensorflow python -c "from keras import backend"
	```

	对于 __Windows__：
	
	```bash
	conda env create -f requirements/dog-windows.yml
	activate dog-project
	set KERAS_BACKEND=tensorflow
	python -c "from keras import backend"
	```
6. 打开 notebook

 ```
jupyter notebook dog_app.ipynb
```

### REFERENCE
**相关参考**
- [CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/)
- [Using Convolutional Neural Networks to Classify Dog Breeds](http://cs231n.stanford.edu/reports/2015/pdfs/fcdh_FinalReport.pdf)
- [Building an Image Classifier](https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Flearning-about-data-science-building-an-image-classifier-part-2-a7bcc6d5e825)
- [Tips/Tricks in CNN](http://lamda.nju.edu.cn/weixs/project/CNNTricks/CNNTricks.html)
- [Transfer Learning using Keras](https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Ftransfer-learning-using-keras-d804b2e04ef8)

**相关论文**
- [[VGG16] VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION](https://arxiv.org/abs/1409.1556)
- [[Inception-v1] Going deeper with convolutions](https://arxiv.org/abs/1409.4842)
- [[Inception-v3] Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567)
- [[Inception-v4] Inception-ResNet and the Impact of Residual Connections on Learning](https://arxiv.org/abs/1602.07261)
- [[ResNet] Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
- [[Xception] Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357)


### 项目反思

完成此项目的过程也是一个探索的过程，项目展现的是神经网络学习的冰山一角，剩下的还需要自己去探索和学习。  
















