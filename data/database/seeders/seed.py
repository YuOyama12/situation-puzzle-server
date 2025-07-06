from data.database.seeders import favorite_seeder, sample_quizzes_seeder

if __name__ == "__main__":
    sample_quizzes_seeder.execute()
    favorite_seeder.execute()