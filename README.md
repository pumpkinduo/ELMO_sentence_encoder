# ELMO_sentence_encoder
ELMO模型来自于论文[Deep contextualized word representations](https://arxiv.org/abs/1802.05365?context=cs)<br>
本文采用的数据集来自论文[PICO Element Detection in Medical Text via Long Short-Term Memory Neural Networks](https://www.aclweb.org/anthology/W18-2308),整理自PubMeb数据库，主要任务是医学摘要序列句子分类。
## 配置参数
在[allennlp](https://allennlp.org/elmo)下载配置文件，在这里选择small规格的模型，生成的词向量维度为256。
>elmo_options.json <br>
>elmo_weights.hdf5 <br>

## 数据处理
1.对dataset文件夹中的原始数据通过dataset_txt_to_json.py文件处理为json格式（根据个人下游任务需求处理）<br>
2.训练集验证集生成vocab.txt词表文件<br>
3.对数据进行padding处理
## 参考文献
[ELMo词向量中文训练过程](https://blog.csdn.net/sinat_26917383/article/details/81913790)

