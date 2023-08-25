import pandas as pd
import warnings; warnings.filterwarnings('ignore')
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

from .Post.models import *


# post user likes  저장하기
post_file_path = "post.csv"
with open(post_file_path, "w", newline='') as csv_file:
    csv_posts = csv.writer(csv_file)
    csv_posts.writerow([])
    for post in posts:
        csv_writer.writerow()


# 데이터 전처리
user_post_list = pd.read_csv(post_file_path, encoding='utf-8')



count_vect = CountVectorizer(min_df =0, ngram_range=(1,2))
like_mat = count_vect.fit_transform(post_file_path['likes'])

like_sim = cosine_similarity(like_mat, like_mat)
like_sim_sorted_ind = like_sim.argsort()[:, ::-1]
percentile = 0.6
m = post_file_path['likes'].quantile(percentile)
c = post_file_path['likes'].mean()


def find_sim_user(id, top_n=5):
    df = post_file_path
    sorted_ind = like_sim_sorted_ind
    

