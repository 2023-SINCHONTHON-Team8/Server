from django.shortcuts import render

# Create your views here.

import pandas as pd
import numpy as mp
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_absolute_error

# 이 평점이 가장 높은 순서대로 post objects를 반환해준다

from recommandation import find_sim_user
import random

# recommendation.py를 사용하여서 likes의 유사도가 비슷한 post들을 내림차순으로 list형식으로 전달해준다
def post_user_recommendation(user_id):
    base_movie = Post.objects.get(user__id = user_id)
    model