# coding=utf-8

class Config(object):
    init_scale = 0.041  #
    learning_rate = 0.001
    max_grad_norm = 15  # https://blog.csdn.net/u013713117/article/details/56281715
    num_layers = 4  # depth
    num_steps = 30  # number of steps to unroll
    hidden_size = 800  # width of hidden layer of neurons
    iteration = 10
    save_freq = 5  # The step (counted by the number of iterations) at which the model is saved to hard disk.
    keep_prob = 0.5
    batch_size = 128
    model_path = './Model' # the path of model that need to save or load

    # parameters for generation
    save_time = 5  # load save_time saved models
    is_sample = True  # if true  using sampling, or not using max
    is_beams = True  # whether or not using beam search
    beam_size = 2  # size of beam search
    len_of_generation = 200 # The number of characters by generated
    start_sentence = u'如今且说林黛玉自在荣府以来，贾母万般怜爱，寝食起居，一如宝玉、迎春、探春、' \
                     u'惜春三个亲孙女倒且靠后。便是宝玉和黛玉二人之亲密友爱，亦自较别个不同，日则同行同坐，' \
                     u'夜则同息同止，真是言和意顺，略无参商。不想如今忽然来了一个薛宝钗，年岁虽大不多' \
                     u'，然品格端方，容貌丰美，人多谓黛玉所不及。'