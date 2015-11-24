for file in ~/yelp-challenge/datasets/all_reviews_by_user/*
do
  FILENAME=$(basename "$file")
  python3 ~/yelp-challenge/scripts/tokenize_reviews.py $file ~/yelp-challenge/datasets/all_reviews_by_user_tokenized/$FILENAME
done
