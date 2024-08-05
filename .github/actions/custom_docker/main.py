import polars as pl
import os


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
    
if __name__ == "__main__":
    main()