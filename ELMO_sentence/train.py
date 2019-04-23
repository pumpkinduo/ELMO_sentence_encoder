import tensorflow as tf
from ELMO_sentence.data_util import get_data,_genVocabFile,padSentence
import os
from ELMO_sentence.bilm import TokenBatcher, BidirectionalLanguageModel, weight_layers, dump_token_embeddings
import json
import numpy as np
k = open("PICO_elmo_train.json","a")
# Dump the token embeddings to a file. Run this once for your dataset.
token_embedding_file = 'elmo_token_embeddings.hdf5'
vocab_file = "../ELMO_sentence/vocab.txt"
_genVocabFile(vocab_file)
options_file = "../ELMO_sentence/elmo_options.json"
weight_file = "../ELMO_sentence/elmo_weights.hdf5"
dump_token_embeddings(
    vocab_file, options_file, weight_file, token_embedding_file
)
tf.reset_default_graph()

# Build the biLM graph.
bilm = BidirectionalLanguageModel(
    options_file,
    weight_file,
    use_character_inputs=False,
    embedding_weight_file=token_embedding_file
)
context_token_ids = tf.placeholder(tf.int32,[None,None],"context_token_ids")
# Get ops to compute the LM embeddings.
context_embeddings_op = bilm(context_token_ids)

elmo_context_input = weight_layers('input', context_embeddings_op, l2_coef=0.0)

# run
dataset = get_data()
data = padSentence(dataset)
batcher = TokenBatcher(vocab_file)
with tf.Session() as sess:
    # It is necessary to initialize variables once before running inference.
    sess.run(tf.global_variables_initializer())

    # Create batches of data.
    batchdata = batcher.batch_sentences(data[200:])

    step = 1
    for i in range(0, len(batchdata), 128):
        elmo_input = []
    # Compute ELMo representations (here for the input only, for simplicity).
        elmo_context_input_ = sess.run(
            [elmo_context_input['weighted_op']],
            feed_dict={context_token_ids: batchdata[i:min(i+128,len(batchdata))]}
        )
        print(step)
        for input in elmo_context_input_[0]:
            elmo_input.append(np.mean(input,axis=0))
        step+=1

        count = 0
        sentenceembedding = {}
        for i in elmo_input:
            sentenceembedding[count] = i.tolist()
            json.dump(sentenceembedding[count], k)
            k.write("\n")
            count+=1