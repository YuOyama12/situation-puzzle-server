from data.database.seeders import sample_quizzes_seeder, favorite_seeder

if __name__ == "__main__":
    sample_quizzes_seeder.execute()
    favorite_seeder.execute()