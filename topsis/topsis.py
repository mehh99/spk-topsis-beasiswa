import numpy as np

class Topsis():
    evaluation_matrix = np.array([])  # Matrix
    weighted_normalized = np.array([])  # Weight matrix
    normalized_decision = np.array([])  # Normalisation matrix
    M = 0  # Number of rows
    N = 0  # Number of columns

    def __init__(self, evaluation_matrix, weight_matrix, criteria):
        self.evaluation_matrix = np.array(evaluation_matrix, dtype="float")
        self.row_size = len(self.evaluation_matrix)
        self.column_size = len(self.evaluation_matrix[0])
        self.weight_matrix = np.array(weight_matrix, dtype="float")
        self.weight_matrix = self.weight_matrix #/ sum(self.weight_matrix) #sum(self.weight_matrix) untuk membagi matrik dengan jumlah
        self.criteria = np.array(criteria, dtype="float")

    def step_2(self):
        self.normalized_decision = np.copy(self.evaluation_matrix)
        sqrd_sum = np.zeros(self.column_size)
        for i in range(self.row_size):
            for j in range(self.column_size):
                sqrd_sum[j] += self.evaluation_matrix[i, j]**2
        for i in range(self.row_size):
            for j in range(self.column_size):
                self.normalized_decision[i,j] = self.evaluation_matrix[i, j] / (sqrd_sum[j]**0.5)

    def step_3(self):
        self.weighted_normalized = np.copy(self.normalized_decision)
        for i in range(self.row_size):
            for j in range(self.column_size):
                self.weighted_normalized[i, j] *= self.weight_matrix[j]

    def step_4(self):
        self.worst_alternatives = np.zeros(self.column_size)
        self.best_alternatives = np.zeros(self.column_size)
        for i in range(self.column_size):
            if self.criteria[i]:
                self.worst_alternatives[i] = min(
                    self.weighted_normalized[:, i])
                self.best_alternatives[i] = max(
                    self.weighted_normalized[:, i])
            else:
                self.worst_alternatives[i] = max(
                    self.weighted_normalized[:, i])
                self.best_alternatives[i] = min(
                    self.weighted_normalized[:, i])

    def step_5(self):
        self.worst_distance = np.zeros(self.row_size)
        self.best_distance = np.zeros(self.row_size)
        self.worst_distance_mat = np.copy(self.weighted_normalized)
        self.best_distance_mat = np.copy(self.weighted_normalized)

        for i in range(self.row_size):
            for j in range(self.column_size):
                self.worst_distance_mat[i][j] = (
                    self.weighted_normalized[i][j] - self.worst_alternatives[j]) ** 2
                self.best_distance_mat[i][j] = (
                    self.weighted_normalized[i][j] - self.best_alternatives[j]) ** 2

                self.worst_distance[i] += self.worst_distance_mat[i][j]
                self.best_distance[i] += self.best_distance_mat[i][j]

        for i in range(self.row_size):
            self.worst_distance[i] = self.worst_distance[i] ** 0.5
            self.best_distance[i] = self.best_distance[i] ** 0.5

    def step_6(self):
        # digunakan untuk mengabaikan semua kesalahan titik mengambang selama perhitungan. Baris ini dimaksudkan untuk menangani situasi di mana kode mungkin mengalami operasi matematika yang dapat menghasilkan kesalahan titik mengambang, seperti pembagian oleh nol atau pengambilan akar kuadrat dari angka negatif.
        np.seterr(all='ignore')
        self.worst_similarity = np.zeros(self.row_size)
        self.best_similarity = np.zeros(self.row_size)
        # self.relative_closeness = self.calculate_relative_closeness()
        
        for i in range(self.row_size):
            self.best_similarity[i] = self.worst_distance[i] / \
                (self.worst_distance[i] + self.best_distance[i])

            self.worst_similarity[i] = self.best_distance[i] / \
                (self.worst_distance[i] + self.best_distance[i])

    # def calculate_relative_closeness(self):
    #     relative_closeness = np.zeros(self.row_size)
    
    #     for i in range(self.row_size):
    #         relative_closeness[i] = self.worst_distance[i] / (self.worst_distance[i] + self.best_distance[i])

    #     return relative_closeness
    
    # def calculate_ci_plus(self):
    #     ci_plus = np.zeros(self.row_size)

    #     for i in range(self.row_size):
    #         ci_plus[i] = self.best_similarity[i] / (self.best_similarity[i] + self.worst_similarity[i])

    #     return ci_plus

    # def ranking(self, data):
    #     return [i + 1 for i in data.argsort()]

    # def rank_to_worst_similarity(self):
    #     return self.ranking(self.worst_similarity)

    # def rank_to_best_similarity(self):
    #     return self.ranking(self.best_similarity)

    def ranking(self, similarity_data, reverse=False):
        ranked_indices = np.argsort(similarity_data)
        if reverse:
            ranked_indices = ranked_indices[::-1]

    # Buat mapping dari indeks ke peringkat
        rank_mapping = {ranked_indices[i]: i + 1 for i in range(len(ranked_indices))}
    
    # Terapkan mapping ke semua data
        ranks = [rank_mapping[i] for i in range(len(ranked_indices))]
    
        return ranks


    def rank_to_worst_similarity(self):
        return self.ranking(self.worst_similarity)

    def rank_to_best_similarity(self):
        return self.ranking(self.best_similarity)
    

    def calculate_ranking(self, similarity_data, reverse=False):
        if not np.any(similarity_data) or len(similarity_data) == 1:
            return []

        ranked_indices = np.argsort(similarity_data)
        if reverse:
            ranked_indices = ranked_indices[::-1]

    # Buat mapping dari indeks ke peringkat
        rank_mapping = {ranked_indices[i]: i + 1 for i in range(len(ranked_indices))}

    # Terapkan mapping ke semua data
        ranks = [rank_mapping[i] for i in range(len(ranked_indices))]

        return ranks

    def calc(self):
        self.step_2()
        self.step_3()
        self.step_4()
        self.step_5()
        self.step_6()

        self.worst_distance= np.around(self.worst_distance,decimals=4)
        self.best_distance = np.around(self.best_distance,decimals=4)
        self.worst_similarity = np.around(self.worst_similarity, decimals=4)
        self.best_similarity = np.around(self.best_similarity, decimals=4)

 

