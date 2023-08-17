## README for datasets
### 一、合成数据集(pairs)   # 38 ---  33.8  2-3
### 1、Rain200L
 - 数量：1800训练，200测试
 - 合成方式：高斯噪声模拟雨线
 - 雨量大小：小
 - 雨线方向: Random
### （2、Rain200H） 效果差
 - 数量：1800训练，200测试
 - 合成方式：高斯噪声模拟雨线
 - 雨量大小：大
 - 雨线方向: Random
### 3、RainCitySpace_OsBs
 - 数量：1400训练，175测试
 - 合成方式：雨模型合成雨线
 - 雨量大小：小
 - 雨线方向: Random
### 4、RainCitySpace_OtBt
 - 数量：1400训练，175测试
 - 合成方式：雨模型合成雨线
 - 雨量大小：小
 - 雨线方向: Vertical

### 5、Rain800L/Rain12600

### 二、真实数据集(unpairs)    # cyclegan pix2pix
### 1、RID&RIS
 - 数量：约2600张真实雨图, 缺少无雨图（想法：rain200无雨图+raincityspace无雨图）
 - 来源：真实拍摄
### 2、SPA
 - 数量：约26000张patch
 - 来源：真实拍摄
### 3、雨滴数据集(pairs)
 - 17年attention-gan论文

### 4、网上爬取

### 5、ai文生图
