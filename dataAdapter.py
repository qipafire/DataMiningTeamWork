import numpy as np
import json
import joblib
def generate_sample_data():
    # 作者数据
    authors = [f'作者{i}' for i in range(1, 11)]
    author_views = np.random.randint(1000, 100000, size=10)
    author_cumulative = np.cumsum(np.random.randint(1000, 5000, size=30))
    
    # 用户数据
    users = [f'用户{i}' for i in range(1, 101)]
    user_views = np.random.randint(0, 500, size=100)
    user_likes = np.random.randint(0, 200, size=100)
    
    # 聚类特征数据
    features = np.random.randn(100, 5)  # 100个样本，5个特征
    
    return {
        'authors': authors,
        'author_views': author_views,
        'author_cumulative': author_cumulative,
        'users': users,
        'user_views': user_views,
        'user_likes': user_likes,
        'features': features
    }

def get_user_data():
    user_data = json.load(open('data/visualize.json',encoding="utf-8"))
    return user_data
def get_author_data():
    author_data = json.load(open('data/visualize_author.json',encoding="utf-8"))
    return author_data
def get_artwork_data():
    artwork_data = json.load(open('data/visualize_artwork.json',encoding="utf-8"))
    return artwork_data
def cluster_data():
    user = joblib.load("data/用户聚类指标.score")
    author = joblib.load("data/作者聚类指标.score")
    clst = dict({"user":user,"author":author})
    return clst
def data_prepare():
    user = get_user_data()
    author = get_author_data()
    artwork = get_artwork_data()
    clst = cluster_data()
    data = dict({"user_data":user,"author_data":author,"artwork_data":artwork,"clst_data":clst})
    return data


if __name__ == "__main__":
    data = data_prepare()
    for i in data.keys():
        print(data[i].keys())