from src.celery_app import add

if __name__ == "__main__":
    r = add.delay(4, 5, 6)
    print(r)
