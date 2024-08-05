import polars as pl
import os

top_k = os.getenv("INPUT_TOP_K")

env_file = os.getenv('GITHUB_ENV')

def main():
    df = pl.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [4, 5, 6],
        }
    )
    print()
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'shape={df.shape}', file=fh)
    
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'top_k={top_k}', file=fh)
        
    # print out top_k from env file
    with open(env_file, 'r') as fh:
        # look for the top_k value
        for line in fh:
            if line.startswith('TOP_K='):
                print(f"TOP_K={line}")
                break
    
    # write a csv file 
    df.head(3).write_csv('df.csv')
    
    # create a new text file called garbage.txt and save it 
    with open('garbage.txt', 'w') as fh:
        fh.write('this is garbage')    
    
if __name__ == "__main__":
    main()