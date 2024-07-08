1. 训练cd yolov5文件夹下，使用如下代码进行训练，其余选项见train.py

   ```python
   python train.py --weights yolov5s.pt --data  <文件路径.yaml> --batch-size 10 --epochs 100 
   # 选择预训练权重为yolov5s.pt，一批次选择十张照片（这个可以大一些，可以修改数值多次尝试，4G1050TI训练200+KB照片放入10已经占了80%+），训练轮次可以设置100轮（中途发现增长不大可以停止，数据会保存在yolov5中的run/trains文件夹下）
   ```

2. 对1中的--data  <文件路径.yaml>特别说明

   ```python
   path: ../datasets
   train: images
   val: images
   nc: 1
   names:
     0: zu
   
   ##path为train和val文件夹存在的路径，使用相对地址，/和\都可以使用；
   
   ##特别注意：train为训练集，val为验证集两个可以相同，YOLO自动寻找标签，格式为将train对应的images替换为labels，所以images和labels应该在同一文件夹下，两者内文件名字一一对应，图像文件对应txt文件。
   
   ##txt文件内容为：0 0.4665492957746479 0.5172413793103449 0.4964788732394366 0.5862068965517241,0为标签值，后四位为图片坐标的相对值。
   
   ##特别注意：names内文件格式一定这么写，names：后另起一行再空格，0： zu，多个标签另起一行，1： bing（也可能存在['zu','bing'...]形式，猜测这样对应标签可以直接为zu不需要用0替换）
   ```

3. 小tips尽量不要在pycharm终端口里进行，单独出来，使用cmd命令，在管理员权限下进行；

4. 推理

   ```python
   (base) PS E:\YOLO\yolov5> python detect.py --weights E:\YOLO\yolov5\runs\train\exp16\weights\best.pt --source 0 --nosave
   
   ##--weights使用自己训练好的权重，文件中有best.pt和last.pt，分别对应最好和最新
   
   ##--sources 0表示使用摄像头进行侦测
   
   ##nosave为可选项可以对刚刚侦测的图片或是视频或是其他进行保存，保存内容中对应会被标记
   ```

5. 训练中存在训练多少轮次后进行保存的选项。