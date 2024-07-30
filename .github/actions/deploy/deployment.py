import requests
import polars as pl

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status() 
    return response.json()

def create_dataframe(data):
    return pl.DataFrame(data)

def main():

  # Get inputs from GitHub Actions
  bucket = os.environ['INPUT_BUCKET']
  bucket_region = os.environ['INPUT_BUCKET-REGION']
  dist_folder = os.environ['INPUT_DIST-FOLDER']

  print(bucket)
  print(bucket_region)
  print(dist_folder)

  url = "https://jsonplaceholder.typicode.com/users"
  
  try:
      user_data = fetch_data(url)
      
      df = create_dataframe(user_data)
      
      print("\nDataFrame info:")
      print(df.schema)
      
      filtered_df = df.filter(pl.col("id") <= 5).select(["name", "email", "company.name"])
      
      print(filtered_df)
      
  except requests.RequestException as e:
      print(f"Error fetching data: {e}")
  except Exception as e:
      print(f"An error occurred: {e}")

if __name__ == '__main__':
  main()
